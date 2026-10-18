# Sistema de Gerenciamento de Clínica Veterinária

Projeto PBL da unidade curricular **Arquitetura e Modelagem de Sistemas**.
Professor: Abraão de Oliveira Ferreira.

**Integrantes:** Alexandre Fabricio Guenther, Gabriel Ângelo Foppa, Ithalo Willian Maximino da Silva e Paulo Henrique Araujo da Silva e Silva.

## Propósito

Centralizar a gestão de uma clínica veterinária: cadastro de tutores e pets, agendamento de consultas, registro do histórico clínico (consultas, diagnósticos, exames, vacinas e tratamentos) e envio de notificações aos tutores.

## Escopo inicial

Esta é a **base inicial** do repositório (Aula 18). Ela contém a organização de pastas, a documentação do design e um esqueleto executável com uma única rota de verificação (`GET /saude`). **Nenhuma regra de negócio foi implementada ainda.**

Requisitos que a estrutura já prevê (detalhes em [`docs/requisitos/`](docs/requisitos/)):

| ID | Requisito | Pacote em `src/` |
|---|---|---|
| RF01 | Cadastro de Tutores | `tutores` |
| RF02 | Cadastro de Pets | `pets` |
| RF03 | Agendamento Online | `agendamentos` |
| RF04 | Histórico Clínico do Pet | `historico_clinico` |
| RF05 | Notificações de Agendamento | `notificacoes` |
| RNF01 | Autenticação de Usuários | `autenticacao` |

## Tecnologias

Python 3.12, FastAPI, Uvicorn e pytest. O banco de dados escolhido é o PostgreSQL (ver [`docs/arquitetura/decisoes.md`](docs/arquitetura/decisoes.md)); ele será integrado quando o modelo de dados for implementado.

## Estrutura do repositório

```
.
├── README.md            Este arquivo
├── requirements.txt     Dependências (versões fixadas)
├── pytest.ini           Configuração dos testes
├── .gitignore           Arquivos que não entram no versionamento
├── .env.example         Modelo de variáveis de ambiente (sem segredos)
├── config/              Modelos e instruções de configuração
├── docs/
│   ├── requisitos/      Requisitos, regras de negócio e rastreabilidade
│   ├── modelagem/       Diagramas UML e descrições dos modelos
│   └── arquitetura/     Componentes e decisões arquiteturais
├── src/
│   ├── main.py          Ponto de entrada (FastAPI) e rota /saude
│   ├── autenticacao/    AuthService
│   ├── tutores/         TutorService
│   ├── pets/            PetService
│   ├── agendamentos/    AgendamentoService
│   ├── historico_clinico/  HistoricoClinicoService
│   ├── notificacoes/    NotificacaoService
│   └── infraestrutura/  Repository Layer, logs, integrações
└── tests/               Testes automatizados (pytest)
```

## Preparação do ambiente

### Pré-requisitos

- Python 3.12 ou superior (`python --version`)
- Git

### Passo a passo

```bash
git clone <URL-DO-REPOSITORIO>
cd clinica-veterinaria

python -m venv .venv
source .venv/bin/activate          # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt

cp .env.example .env               # Windows: copy .env.example .env
pytest                             # verificação inicial
uvicorn src.main:app --reload      # sobe a aplicação
```

Com a aplicação em execução, acesse `http://127.0.0.1:8000/saude`. A resposta esperada é:

```json
{"status":"ok"}
```

A documentação interativa da API (Swagger) fica em `http://127.0.0.1:8000/docs`.

Em alguns sistemas o comando é `python3` em vez de `python`. No Windows, se o PowerShell bloquear a ativação do ambiente virtual, execute `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente novamente.

### Configuração

As variáveis estão listadas em [`.env.example`](.env.example). O arquivo `.env` é local, ignorado pelo Git e carregado automaticamente pela aplicação. No esqueleto atual nenhuma variável é obrigatória. Mais detalhes em [`config/README.md`](config/README.md).

## Onde encontrar os artefatos

| Artefato | Local |
|---|---|
| Requisitos funcionais, não funcionais e regras de negócio | [`docs/requisitos/`](docs/requisitos/) |
| Matriz de rastreabilidade | [`docs/requisitos/rastreabilidade.md`](docs/requisitos/rastreabilidade.md) |
| Diagramas (casos de uso, classes, estados, sequência) | [`docs/modelagem/`](docs/modelagem/) |
| Decisões de arquitetura e tecnologia | [`docs/arquitetura/decisoes.md`](docs/arquitetura/decisoes.md) |
| Testes | [`tests/`](tests/) |

Protótipos de tela ficam no Figma e o quadro de tarefas fora do repositório, ambos citados em `docs/`.

## Convenções de trabalho

- **Branches:** `main` é a referência estável. Mudanças em branches `feature/<descricao-curta>` (ex.: `feature/cadastro-tutor`) ou `docs/<descricao-curta>`.
- **Commits:** mensagem curta, no presente e descritiva (ex.: `Cria estrutura inicial do projeto`). Quando aplicável, citar o requisito (ex.: `RF01: valida CPF duplicado`).
- **Código Python:** módulos e pacotes em `snake_case` sem acentos; classes em `PascalCase`.
- **Segredos:** nunca versionar senhas, tokens ou chaves. Use apenas `.env.example` com valores fictícios.
- **Antes de cada commit:** rodar `git status` para conferir o que será incluído.
