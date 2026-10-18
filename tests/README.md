# tests/

Testes automatizados (pytest). A configuração está em `pytest.ini` na raiz (`testpaths = tests`).

Os testes devem verificar comportamentos e regras de negócio, não apenas a existência de arquivos. Ao implementar um módulo, criar o teste correspondente em `tests/` seguindo o nome do pacote (ex.: `tests/test_tutores.py`).

- Teste atual: `test_saude.py` (confirma que `GET /saude` responde 200 com `{"status": "ok"}`).
- Executar: `pytest`
