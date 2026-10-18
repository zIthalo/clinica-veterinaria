# src/

Código da aplicação (Python), organizado em pacotes por responsabilidade, espelhando os componentes definidos no design (Aula 03):

| Pacote | Componente | Requisito |
|---|---|---|
| `autenticacao` | AuthService | RNF01 |
| `tutores` | TutorService | RF01 |
| `pets` | PetService | RF02 |
| `agendamentos` | AgendamentoService | RF03 |
| `historico_clinico` | HistoricoClinicoService | RF04 |
| `notificacoes` | NotificacaoService | RF05 |
| `infraestrutura` | Repository Layer, logs, integrações | todos |

`main.py` é o ponto de entrada (FastAPI) e contém a rota de verificação `GET /saude`. Cada pacote tem um `__init__.py` com a descrição de sua finalidade. Novos módulos devem ser criados no pacote da responsabilidade correspondente.
