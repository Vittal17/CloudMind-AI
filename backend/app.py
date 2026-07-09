from fastapi import FastAPI
from rag.llm import ask_llm

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to CloudMind AI 🚀"
    }
    
@app.get("/ask")
def ask():
    answer = ask_llm("Explain AWS Lambda in one sentence.")
    return {
        "answer": answer
    }