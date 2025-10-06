# Singapore Housing RAG Chatbot - Usage Examples

This document shows you how to use the RAG chatbot module in different scenarios.

## Installation

1. Copy the `rag_chatbot.py` file to your project
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure you have:
   - A `.env` file with `MISTRAL_API_KEY=your_api_key`
   - The `singapore_hdb_data.json` file

## Basic Usage Examples

### Example 1: Simple Question-Answer
```python
from rag_chatbot import RAGChatbot

# Initialize the chatbot
bot = RAGChatbot()

# Ask a single question
response = bot.chat("Tell me about Yishun")
print(response)
```

### Example 2: Conversation with Memory
```python
from rag_chatbot import RAGChatbot

# Initialize the chatbot
bot = RAGChatbot()

# Start a conversation
conversation = bot.start_conversation()

# Multi-turn conversation
response1 = bot.chat("Tell me about Yishun", conversation)
print(f"Bot: {response1}")

response2 = bot.chat("What about housing prices there?", conversation)
print(f"Bot: {response2}")

response3 = bot.chat("Any cons about living there?", conversation)
print(f"Bot: {response3}")
```

### Example 3: Interactive Chat Loop
```python
from rag_chatbot import RAGChatbot

bot = RAGChatbot()
conversation = bot.start_conversation()

print("Chat with the Singapore Housing Bot (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        break
    
    response = bot.chat(user_input, conversation)
    print(f"Bot: {response}")
```

### Example 4: Using the Quick Chat Function
```python
from rag_chatbot import quick_chat

# For testing or one-off questions
response = quick_chat("What areas have affordable HDB flats?")
print(response)
```

### Example 5: Getting Conversation History
```python
from rag_chatbot import RAGChatbot

bot = RAGChatbot()
conversation = bot.start_conversation()

# Have some conversation
bot.chat("Tell me about Tampines", conversation)
bot.chat("What about the pros and cons?", conversation)

# Get the conversation history
history = bot.get_conversation_history(conversation)
for msg in history:
    print(f"{msg['type']}: {msg['content']}")
```

### Example 6: Error Handling
```python
from rag_chatbot import RAGChatbot

try:
    bot = RAGChatbot()
    response = bot.chat("Tell me about Orchard")
    print(response)
except FileNotFoundError as e:
    print(f"Missing file: {e}")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Example 7: Custom Data File Location
```python
from rag_chatbot import RAGChatbot

# If your data file is in a different location
bot = RAGChatbot(
    data_file="/path/to/your/housing_data.json",
    env_file="/path/to/your/.env"
)

response = bot.chat("Tell me about Punggol")
print(response)
```

### Example 8: Integration with Web Framework (Flask)
```python
from flask import Flask, request, jsonify
from rag_chatbot import RAGChatbot

app = Flask(__name__)
bot = RAGChatbot()

# Store conversations per session (in production, use proper session management)
conversations = {}

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    user_id = data.get('user_id', 'default')
    message = data.get('message', '')
    
    # Get or create conversation for this user
    if user_id not in conversations:
        conversations[user_id] = bot.start_conversation()
    
    # Get response
    response = bot.chat(message, conversations[user_id])
    
    return jsonify({
        'response': response,
        'user_id': user_id
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Example 9: Integration with Streamlit
```python
import streamlit as st
from rag_chatbot import RAGChatbot

# Initialize the chatbot (cached)
@st.cache_resource
def load_chatbot():
    return RAGChatbot()

bot = load_chatbot()

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = bot.start_conversation()

st.title("Singapore Housing Chatbot")

# Chat interface
if prompt := st.chat_input("Ask about Singapore housing"):
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get bot response
    response = bot.chat(prompt, st.session_state.conversation)
    
    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)
```

## Configuration Options

### Environment Variables
Create a `.env` file with:
```
MISTRAL_API_KEY=your_mistral_api_key_here

# Optional: LangSmith tracing
LANGSMITH_API_KEY=your_langsmith_api_key_here
```

### Data File Format
The JSON data file should have this structure:
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

## Troubleshooting

### Common Issues:

1. **Missing API Key**: Make sure your `.env` file contains `MISTRAL_API_KEY`
2. **File Not Found**: Ensure `singapore_hdb_data.json` is in the same directory
3. **Import Errors**: Install all dependencies with `pip install -r requirements.txt`
4. **Memory Issues**: The chatbot keeps conversation history in memory. For long conversations, consider implementing conversation trimming.

### Performance Tips:

1. **Reuse Bot Instance**: Initialize once and reuse for multiple conversations
2. **Batch Processing**: For multiple users, consider using async patterns
3. **Caching**: The vector store is built once during initialization
4. **Memory Management**: Clear old conversations periodically in production

## Advanced Usage

### Custom System Messages
You can modify the system message by editing the `generate` function in the `rag_chatbot.py` file.

### Different Models
Change the model by modifying the initialization:
```python
# In the _initialize_models method
self.llm = init_chat_model("mistral-small-latest", model_provider="mistralai")
```

### Custom Retrieval
Modify the retrieval parameters in the `retrieve` tool:
```python
retrieved_docs = self.vector_store.similarity_search(query, k=5)  # Get more docs
```