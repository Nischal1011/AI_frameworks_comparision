from typing import TypedDict, Annotated, Sequence
from typing_extensions import TypedDict
from langgraph.graph import Graph, StateGraph
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import operator

# Load environment variables
load_dotenv()

# Load and prepare the document
loader = TextLoader("example.txt")
documents = loader.load()
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
llm = OpenAI(temperature=0)

# Define the state structure
class State(TypedDict):
    query: str
    context: str
    response: str
    history: list[str]

# Define the nodes (functions that will process our data)
def retrieve_context(state: State) -> State:
    """Retrieve relevant context from the vector store."""
    docs = retriever.get_relevant_documents(state["query"])
    state["context"] = docs[0].page_content if docs else ""
    return state

def generate_response(state: State) -> State:
    """Generate a response using the LLM."""
    prompt = f"""
    Based on the following context, answer the query.
    Context: {state['context']}
    Query: {state['query']}
    """
    state["response"] = llm.invoke(prompt)
    return state

def update_history(state: State) -> State:
    """Update conversation history."""
    state["history"].append({
        "query": state["query"],
        "response": state["response"]
    })
    return state

# Create the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("retrieve", retrieve_context)
workflow.add_node("generate", generate_response)
workflow.add_node("update_history", update_history)

# Add edges
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "update_history")

# Set entry and end points
workflow.set_entry_point("retrieve")
workflow.set_finish_point("update_history")

# Compile the graph
app = workflow.compile()

# Test queries
queries = [
    "Who invented the Analytical Engine?",
    "Did it influence modern computers?",
    "What came after the Analytical Engine?",
    "What improvements did the transistor bring?"
]

# Process queries
for query in queries:
    # Initialize state for each query
    state = State(
        query=query,
        context="",
        response="",
        history=[]
    )
    
    # Run the workflow
    result = app.invoke(state)
    
    # Print results
    print(f"\nQuery: {query}")
    print(f"Response: {result['response']}\n")
