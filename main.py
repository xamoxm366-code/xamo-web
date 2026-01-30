from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"


@app.post("/chat")
async def chat(data: dict):
    prompt = data.get("message")

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload)

    answer = res.json().get("response", "")

    return {"reply": answer}