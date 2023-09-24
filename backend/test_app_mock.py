import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestApp(unittest.TestCase):

	@path('app.routes.chess.get_best_move')
	def test_get_best_move(self, mock_get_best_move):
		mock_get_best_move.return_value = "e2e4"
		fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
		response = client.get(f"/chess/best_move/?fen={fen}"_
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), {"best_move": "e2e4"})

	@patch('app.routes.chat.get_move_explanation')
	def test_get_move_explanation(self, mock_get_move_explanation):
		mock_get_move_explanation.return_value = "This move opens up the center."
		move = "e2e4"
		fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
		response = client.get(f"/chat/explain_move/?move={move}&fen={fen}")
		self.assertEqual(response.status_code, 200)
		explanation_text = response.jason().get("explanation", "")
		self.assertIn("open", explanation_text.lower())
		self.assertIn("center", explanation_text.lower())

if __name__ == '__main__':
	unittest.main()
