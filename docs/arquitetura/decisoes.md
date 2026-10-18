# Registro de decisões

| # | Decisão | Justificativa resumida | Origem |
|---|---|---|---|
| 1 | Arquitetura em camadas (Apresentação, Aplicação, Domínio, Infraestrutura) | Separa telas, regras de negócio e banco; reduz acoplamento e facilita testes | Aula 03 |
| 2 | Repository Pattern para persistência | O domínio não depende da tecnologia de armazenamento | Aula 03 |
| 3 | PostgreSQL como banco de dados | Dados estruturados e interdependentes (tutor, pet, consulta, histórico); integridade referencial e transações. Comparado com MySQL e MongoDB (A²ER²) | Aula 06 |
| 4 | Notificações orientadas a eventos, com Orientação a Objetos para as preferências do tutor | Desacopla o agendamento do envio de mensagens; falha do provedor não trava a interface | Aula 10 |
| 5 | Technology Radar: Docker (Adotar); Lambda e EventBridge (Experimentar); IA Generativa (Avaliar); Edge (Evitar) | Análise de maturidade, risco, custo e segurança | Aula 07 |
| 6 | Linguagem Python 3.12 com FastAPI e SQLAlchemy (a integrar) | API REST moderna com validação e documentação automática (Swagger em /docs); bom suporte a PostgreSQL; SQLAlchemy facilita o Repository Pattern | Aula 18 |
| 7 | Testes com pytest em `tests/` | Estrutura exigida (`docs/`, `src/`, `tests/`) e verificação automatizada do esqueleto | Aula 18 |

## Observação

A Aula 12 apontou que Lambda/EventBridge não têm um RNF que os justifique (a clínica não tem volume que exija esse porte). Enquanto isso não for resolvido, o esqueleto não depende de nenhum serviço de nuvem: o desacoplamento de notificações pode começar com eventos internos da aplicação.
