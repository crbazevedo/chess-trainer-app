from fastapi import APIRouter
from stockfish import Stockfish

stockfish = Stockfish("/usr/local/bin/stockfish-ubuntu-x86-64-avx2")

router = APIRouter()

@router.get("/best_move/")
def get_best_move(fen):
    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()
    return best_move
