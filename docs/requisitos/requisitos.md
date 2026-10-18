# Requisitos

Numeração oficial adotada: a da Aula 03 (RF05 = Notificações). Nos documentos anteriores, notificações aparece também como RF08 (Aulas 10 e 11) e RF03 (Aula 12); essas referências devem ser lidas como RF05.

## Requisitos funcionais

| ID | Nome | Descrição | Prioridade | Critério de aceitação |
|---|---|---|---|---|
| RF01 | Cadastro de Tutores | Cadastrar tutores com dados pessoais e de contato | Alta | Tutor cadastrado fica disponível para consulta e edição por usuários autorizados |
| RF02 | Cadastro de Pets | Cadastrar animais vinculados aos tutores | Alta | Pet associado ao tutor responsável, com dados armazenados |
| RF03 | Agendamento Online | Agendar consultas e serviços pela internet | Alta | Usuário escolhe unidade, serviço, veterinário, data e horário e recebe confirmação |
| RF04 | Histórico Clínico do Pet | Armazenar e disponibilizar consultas, diagnósticos, vacinas, exames e tratamentos | Alta | Histórico consultado apenas por usuários autorizados, completo e atualizado |
| RF05 | Notificações de Agendamento | Enviar confirmação, cancelamento e lembretes por e-mail, SMS ou push, respeitando as preferências do tutor | Alta | Tutor recebe confirmação após o agendamento e lembrete antes da consulta |

## Requisitos não funcionais

| ID | Nome | Descrição | Critério de aceitação |
|---|---|---|---|
| RNF01 | Autenticação de Usuários | Exigir autenticação e controle de acesso por perfil | Apenas usuários autenticados acessam as funcionalidades permitidas ao seu perfil |

RNFs ainda a definir (apontados na Aula 12): proteção e mascaramento de dados pessoais (LGPD), registro de auditoria com prazo de retenção, e disponibilidade/backup.

## Regras de negócio

| ID | Regra |
|---|---|
| RN01 | Não é permitido cadastrar a mesma pessoa duas vezes (verificação por CPF) |
| RN02 | Todo pet deve estar vinculado a exatamente um tutor |
| RN03 | Um agendamento só é concluído após validar a disponibilidade do veterinário e do horário |
| RN04 | O registro de um atendimento atualiza obrigatoriamente o histórico clínico do pet |
| RN05 | Dados pessoais e clínicos são protegidos conforme a LGPD |
