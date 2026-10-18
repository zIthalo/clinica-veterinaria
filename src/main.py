"""Ponto de entrada da aplicação.

O esqueleto inicial não implementa regras de negócio; apenas permite verificar
que o ambiente foi preparado corretamente (rota GET /saude).
"""
from dotenv import load_dotenv
from fastapi import FastAPI

# Carrega variáveis do arquivo .env (local, ignorado pelo Git), se existir.
load_dotenv()

app = FastAPI(title="Sistema de Gerenciamento de Clínica Veterinária", version="0.1.0")


@app.get("/saude")
def saude() -> dict[str, str]:
    """Confirma que a aplicação sobe e responde."""
    return {"status": "ok"}
