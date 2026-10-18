"""Verifica o comportamento observável do esqueleto: GET /saude responde 200 com {"status": "ok"}."""
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_rota_de_saude_responde_ok():
    resposta = client.get("/saude")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}
