import os
from rag_chatbot import RAGChatbot

data_dir = './Datasets'
data_files = [os.path.join(data_dir, f) 
    for f in os.listdir(data_dir) 
    if f.endswith('.json')
]

bot = RAGChatbot(data_file=data_files)