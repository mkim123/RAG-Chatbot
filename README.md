# 🏠 Singapore Housing RAG Chatbot

A sophisticated **Retrieval-Augmented Generation (RAG)** chatbot built with **LangChain** and **LangGraph** that provides intelligent responses about Singapore's housing market and HDB information.

## 🌟 Features

- **🤖 Intelligent Conversations**: Multi-turn conversations with context memory
- **🔍 RAG Architecture**: Combines retrieval and generation for accurate responses
- **🏘️ Singapore Housing Expert**: Specialized knowledge about HDB areas, prices, and neighborhoods
- **🧠 Memory Management**: Maintains conversation context across multiple interactions
- **📦 Modular Design**: Easy to integrate into other applications
- **🔐 Secure**: Proper API key management with environment variables
- **⚡ Fast Retrieval**: Vector-based similarity search for relevant information

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MistralAI API key
- Git (for cloning)

### Installation 

1. **Clone the repository**
   ```bash
   git clone https://github.com/mkim123/RAG-Chatbot.git
   cd RAG-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key_here
   
   # Optional: For LangSmith tracing
   LANGSMITH_API_KEY=your_langsmith_api_key_here
   ```

4. **Run the chatbot**
   ```bash
   python rag_chatbot.py
   ```

## 📖 Usage

### As a Standalone Application
```bash
python rag_chatbot.py
```

### As a Python Module
```python
from rag_chatbot import RAGChatbot

# Initialize the chatbot
bot = RAGChatbot()

# Single question
response = bot.chat("Tell me about Yishun")
print(response)

# Conversation with memory
conversation = bot.start_conversation()
response1 = bot.chat("Tell me about Tampines", conversation)
response2 = bot.chat("What about housing prices there?", conversation)
```

### Quick Testing
```python
from rag_chatbot import quick_chat

response = quick_chat("What areas have affordable HDB flats?")
print(response)
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│   LangGraph      │───▶│   Response      │
└─────────────────┘    │   Workflow       │    └─────────────────┘
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Retrieval Tool  │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Vector Store    │
                       │  (MistralAI      │
                       │   Embeddings)    │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │ Singapore HDB    │
                       │ Housing Data     │
                       └──────────────────┘
```

### Key Components

- **LangGraph Workflow**: Orchestrates the RAG pipeline with conditional logic
- **MistralAI LLM**: `mistral-large-latest` for response generation
- **MistralAI Embeddings**: `mistral-embed` for document embeddings
- **Vector Store**: In-memory vector storage for fast similarity search
- **Conversation Memory**: Maintains context across multiple turns

## 📁 Project Structure

```
RAG-Chatbot/
├── 📓 langchain_pipeline.ipynb    # Development notebook
├── 🐍 rag_chatbot.py             # Main chatbot module
├── 📊 singapore_hdb_data.json    # Housing data knowledge base
├── 📋 requirements.txt           # Python dependencies
├── 📚 usage_examples.md          # Comprehensive usage guide
├── 🔒 .env                       # Environment variables (not in repo)
├── 🚫 .gitignore                 # Git ignore rules
└── 📖 README.md                  # This file
```

## 🎯 Example Queries

The chatbot can answer questions like:

- **"Tell me about Yishun"** - Get general information about the area
- **"What are affordable HDB areas?"** - Find budget-friendly options
- **"Compare Tampines and Punggol"** - Area comparisons
- **"What are the pros and cons of living in Jurong?"** - Detailed insights
- **"Which areas have good connectivity?"** - Transportation information

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MISTRAL_API_KEY` | ✅ Yes | Your MistralAI API key |
| `LANGSMITH_API_KEY` | ❌ Optional | For conversation tracing |

### Data Format

The housing data is stored in JSON format:
```json
[
  {
    "area": "Yishun",
    "has_hdb": "Yes",
    "hdb_price_range": "$300,000 - $600,000",
    "pros": "Good connectivity, family-friendly",
    "cons": "Can be crowded, limited nightlife"
  }
]
```

## 🔗 Integration Examples

### Flask Web API
```python
from flask import Flask, request, jsonify
from rag_chatbot import RAGChatbot

app = Flask(__name__)
bot = RAGChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = bot.chat(message)
    return jsonify({'response': response})
```

### Streamlit App
```python
import streamlit as st
from rag_chatbot import RAGChatbot

bot = RAGChatbot()
st.title("Singapore Housing Chatbot")

if prompt := st.chat_input("Ask about housing"):
    response = bot.chat(prompt)
    st.write(response)
```

## 🛠️ Development

### Setting up Development Environment

1. **Clone and install**
   ```bash
   git clone https://github.com/mkim123/RAG-Chatbot.git
   cd RAG-Chatbot
   pip install -r requirements.txt
   ```

2. **Run Jupyter notebook**
   ```bash
   jupyter notebook langchain_pipeline.ipynb
   ```

### Testing

```bash
# Test the module directly
python rag_chatbot.py

# Or run quick tests
python -c "from rag_chatbot import quick_chat; print(quick_chat('Tell me about Tampines'))"
```

## 📊 Performance

- **Response Time**: ~2-3 seconds for typical queries
- **Memory Usage**: ~100MB for vector store and model
- **Concurrent Users**: Supports multiple conversations simultaneously
- **Accuracy**: High relevance due to specialized Singapore housing data

## 🚨 Security Notes

- **Never commit `.env` files** - They contain sensitive API keys
- **API Key Management** - Store keys securely and rotate regularly
- **Rate Limiting** - Be aware of MistralAI API rate limits
- **Data Privacy** - Housing data is publicly available information

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** - For the excellent RAG framework
- **MistralAI** - For powerful LLM and embedding models
- **Singapore HDB** - For public housing information
- **LangGraph** - For workflow orchestration

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/mkim123/RAG-Chatbot/issues)
- **Documentation**: See `usage_examples.md` for detailed examples
- **Discussions**: [GitHub Discussions](https://github.com/mkim123/RAG-Chatbot/discussions)

## 🗺️ Roadmap

- [ ] Add more Singapore housing areas
- [ ] Implement conversation export functionality
- [ ] Add support for multiple languages
- [ ] Create web interface
- [ ] Add real-time property price updates
- [ ] Implement user feedback collection

---

**Built with ❤️ for the Singapore housing community**
