import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest
from chat_engine import get_response
from crisis import contains_crisis_keyword, SAFETY_MESSAGES
from logger import log_chat
from doc_engine import query_documents
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# allow cors for frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return{"messages": "Welcome to the AI-powered Mental Health Chatbot!"}

@app.post("/chat")
def chat_with_memory(request: ChatRequest):
    session_id = request.session_id
    user_query = request.query
    
    #Crisis Keyword check
    if contains_crisis_keyword(user_query):
        log_chat(session_id, user_query, SAFETY_MESSAGES, is_crisis=True)
        return{"response": SAFETY_MESSAGES}
    
    #Normal LLm response
    response = get_response(session_id, user_query)
    log_chat(session_id, user_query, response, is_crisis=False)
    return{"response": response}

@app.post("/doc-chat")
def chat_with_document(request: ChatRequest):
    response = query_documents(request.query)
    return{"response":response}