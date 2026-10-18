# docs/arquitetura/

Componentes e decisões arquiteturais. Veja [`decisoes.md`](decisoes.md).

## Camadas

| Camada | Conteúdo | Onde está no código |
|---|---|---|
| Apresentação | App do tutor, sistema web, painel administrativo | Fora do escopo desta base (futuro front-end) |
| Aplicação | Controle dos casos de uso e coordenação das operações | Serviços dos pacotes de `src/` |
| Domínio | Regras de agendamento, cadastro, permissões e histórico | Pacotes de `src/` |
| Infraestrutura | Banco de dados, backup, notificações, logs e integrações | `infraestrutura`, `notificacoes` |
