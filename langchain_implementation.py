from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the document
loader = TextLoader("example.txt")
documents = loader.load()

# Create embeddings and store in a vector database
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
# Set up the retrieval QA chain
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever 
)

# Simulate a conversation
queries = [
    "Who invented the Analytical Engine?",
    "Did it influence modern computers?",
    "What came after the Analytical Engine?",
    "What improvements did the transistor bring?"
]


for query in queries:
    response = qa_chain.invoke(query)
    print(f"Query: {query}\nResponse: {response}\n")