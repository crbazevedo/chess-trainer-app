from fastapi imortAPIRouter
import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

router = APIRouter()

@router.get("/explain_move/")
def get_move_explanation(move, fen):
    prompt = f"Explain the chess move {move} in the position {fen}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    explanation = response.choices[0].text.strip()
    return explanation

