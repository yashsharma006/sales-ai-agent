from fastapi import FastAPI, Header, HTTPException
from agent import ask_agent

app = FastAPI()

API_KEY = "company123"


@app.get("/")
def home():
    return {"message": "Sales AI API is running"}


@app.post("/ask")
def ask(question: str, api_key: str = Header(None)):

    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    answer = ask_agent(question)

    return {
        "answer": answer
    }