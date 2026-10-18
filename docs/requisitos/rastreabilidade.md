# Matriz de rastreabilidade

Caminho seguido: **Requisito, Caso de Uso, Modelo, Componente, Teste**. Os casos de uso e a relação com requisitos vêm da Aula 08; os componentes, da Aula 03.

| Requisito | Casos de uso | Modelo (docs/modelagem) | Pacote em src/ | Teste (tests/) |
|---|---|---|---|---|
| RF01 | Cadastrar Tutor | Casos de uso; Classes | `tutores` | A criar |
| RF02 | Cadastrar Pet | Casos de uso; Classes | `pets` | A criar |
| RF03 | Agendar Consulta (inclui Validar Disponibilidade) | Casos de uso; Estados; Sequência | `agendamentos` | A criar |
| RF04 | Realizar Triagem; Registrar Atendimento; Atualizar Histórico Clínico; Consultar Histórico Clínico | Casos de uso; Classes | `historico_clinico` | A criar |
| RF05 | Enviar Lembrete de Consulta (extend de Agendar Consulta) | Sequência | `notificacoes` | A criar |
| RNF01 | Autenticação (Serviço de Autenticação) | Casos de uso | `autenticacao` | A criar |
| (todos) | Verificação do esqueleto | - | `main.py` | `test_saude.py` |

## Pendências conhecidas

- Os identificadores UC01, UC02... variam entre as Aulas 02, 08 e 12. Padronizar antes de incluí-los nesta matriz.
- Na Aula 08, o diagrama liga "Registrar Atendimento" à Recepcionista, mas a especificação textual (UC06) define o Veterinário como ator principal.
- Não há protótipo de tela para o histórico clínico / carteirinha de vacinas (RF04), apontado como requisito órfão na Aula 12.
