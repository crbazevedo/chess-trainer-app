from fastapi import FastAPI
from .routes import chess, chat

app = FastAPI()

app.include_router(chess.router, prefix="/chess", tags=["chess"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])


@app.get("/")
def read_root():
    return {"message": "Hello, Chess Trainer!"}
