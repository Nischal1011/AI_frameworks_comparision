# 🌟 LangGraph vs LangChain Demo

A demonstration project comparing LangGraph and LangChain approaches for building conversational AI systems with context awareness and state management. This project showcases how to build intelligent Q&A systems using computer history as an example domain.

## 🎯 Overview

This repository demonstrates two different approaches to building conversational AI systems:
- A **LangGraph-based** implementation featuring stateful, graph-based processing
- A **LangChain-based** implementation using traditional linear processing

Both systems interact with a document about computer history, from Babbage's Analytical Engine to modern computing, to showcase their capabilities and architectural differences.

## ✨ Key Features

### LangGraph Implementation
- 📝 Stateful conversation management with persistent memory
- 🔄 Sophisticated context retention across multiple queries
- 🌐 Graph-based workflow for complex reasoning paths
- 🧠 Enhanced reasoning capabilities through state management
- 🔗 Flexible node-based architecture for easy expansion

### LangChain Implementation
- 🔍 Simple RAG (Retrieval-Augmented Generation)
- 📚 Efficient document-based retrieval
- 🔄 Straightforward linear processing workflow
- 🚀 Quick setup and implementation
- 📊 Direct question-answer mapping

## 💡 Use Cases

This demo is particularly useful for:
- Building context-aware chatbots
- Implementing document Q&A systems
- Understanding state management in AI conversations
- Comparing different LLM framework architectures
- Learning about RAG implementations

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Basic understanding of LLMs and RAG systems

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

### Project Structure
```
├── README.md
├── requirements.txt
├── example.txt              # Sample computer history document
├── langgraph_temp.py       # LangGraph implementation
├── langchain_temp.py       # LangChain implementation
└── .env                    # Environment variables
```

## 📊 Implementation Details

### LangGraph Implementation
The LangGraph version implements a stateful graph with three main nodes:
1. **Retrieve Context**: Fetches relevant information from the document
2. **Generate Response**: Processes the query with context
3. **Update History**: Maintains conversation state

### LangChain Implementation
The LangChain version uses a simpler RAG approach:
1. Document loading and embedding
2. Vector store creation
3. Direct query-response processing

## 🔬 Sample Queries and Results

The demo includes example queries about computer history:

```python
queries = [
    "Who invented the Analytical Engine?",
    "Did it influence modern computers?",
    "What came after the Analytical Engine?",
    "What improvements did the transistor bring?"
]
```

### Example Response Flow:
1. **Query**: "Who invented the Analytical Engine?"
   - *System retrieves information about Charles Babbage*
   - *Provides context about the early 19th century invention*

2. **Query**: "What improvements did the transistor bring?"
   - *System recalls previous context about early computers*
   - *Explains the transition from vacuum tubes to transistors*

## 🔍 Key Differences

| Feature | LangGraph | LangChain |
|---------|-----------|-----------|
| Context Retention | ✅ Maintains context across queries | ❌ Limited context awareness |
| Processing Model | 🌐 Graph-based | ➡️ Linear |
| State Management | ✅ Stateful | ❌ Stateless |
| Response Detail | 🎯 Comprehensive, connected | 📝 Direct, isolated |
| Setup Complexity | 🔧 More complex | ✨ Simple |
| Flexibility | 🎛️ Highly customizable | 📦 More rigid |

## 📚 Learn More

For a deep dive into the evolution of NLP frameworks and the emergence of graph-based approaches:

[From NLTK to LangGraph: How LangChain's Limitations Paved the Way for Graph-Based AI](https://datascientistinsights.substack.com/p/from-nltk-to-langgraph-how-langchains)

## 🛠️ Technical Requirements

```
python-dotenv
langchain
langchain-openai
langchain-community
chromadb
langgraph
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⭐ Show your support

If you find this project useful, please give it a star! It helps others discover this resource.

---

Made with ❤️ by Nischal Subedi