# config/

Modelos e instruções de configuração do projeto. **Nenhum valor secreto deve ser versionado aqui.**

## Como configurar

1. Copie `.env.example` (na raiz) para `.env`.
2. Preencha os valores reais apenas no seu ambiente local.
3. A aplicação carrega o `.env` automaticamente ao iniciar (`python-dotenv`, em `src/main.py`).

## Variáveis

| Variável | Uso | Requisito |
|---|---|---|
| `DATABASE_URL` | Conexão com o PostgreSQL | RF01 a RF04 |
| `SECRET_KEY` | Assinatura dos tokens de autenticação | RNF01 |
| `NOTIFICACAO_EMAIL_API_KEY`, `NOTIFICACAO_SMS_API_KEY` | Provedores de e-mail e SMS | RF05 |

No esqueleto atual nenhuma variável é obrigatória. Se algum segredo for versionado por engano, ele deve ser substituído no serviço de origem: apagar o arquivo em um novo commit não remove o valor do histórico do Git.
