# Feature Specification: Task Manager

**Feature Branch**: `002-task-manager`

**Created**: 2026-07-05

**Status**: Draft

**Input**: User description: "O sistema é um gerenciador de tarefas (To-Do List). Os requisitos funcionais primários são: 1. Cadastrar novas tarefas com título e data opcional; 2. Remover tarefas existentes; 3. Exibir a data associada à tarefa na lista."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cadastrar tarefas com data (Priority: P1)

O usuário deve conseguir registrar uma nova tarefa informando um título e, quando desejado, uma data.

**Why this priority**: Este é o fluxo principal do sistema e permite que o usuário organize tarefas por data sem usar horário ou lembrete com hora.

**Independent Test**: Pode ser testado ao criar uma tarefa com e sem data e confirmar que ela aparece na lista de tarefas.

**Acceptance Scenarios**:

1. **Given** que o usuário abriu o gerenciador, **When** ele informa um título e confirma a criação da tarefa, **Then** a tarefa é adicionada à lista.
2. **Given** que o usuário deseja associar uma data à tarefa, **When** ele seleciona uma data, **Then** o sistema armazena essa data junto à tarefa.
3. **Given** que o usuário cria uma tarefa sem selecionar uma data, **When** a tarefa é salva, **Then** a tarefa é criada e exibida sem data associada.

---

### User Story 2 - Remover tarefas (Priority: P2)

O usuário deve conseguir remover tarefas que já não são mais necessárias.

**Why this priority**: A remoção é essencial para manter a lista organizada e evitar acúmulo de itens desnecessários.

**Independent Test**: Pode ser testado ao excluir uma tarefa e confirmar que ela deixa de aparecer na lista.

**Acceptance Scenarios**:

1. **Given** que existe uma tarefa cadastrada, **When** o usuário solicita a remoção, **Then** a tarefa é removida da lista.
2. **Given** que a tarefa foi removida, **When** o usuário recarrega a página, **Then** a tarefa não deve mais aparecer.

---

### User Story 3 - Visualizar a data associada à tarefa (Priority: P2)

O usuário deve conseguir identificar rapidamente a data relacionada a cada tarefa.

**Why this priority**: A data ajuda a organizar e priorizar as tarefas sem depender de horário ou notificações.

**Independent Test**: Pode ser testado ao visualizar a lista de tarefas e confirmar que a data aparece corretamente para os itens que a possuem.

**Acceptance Scenarios**:

1. **Given** que uma tarefa possui uma data associada, **When** o usuário visualiza a lista, **Then** a data é exibida junto à tarefa.
2. **Given** que uma tarefa não possui data associada, **When** o usuário visualiza a lista, **Then** o sistema indica claramente que não há data definida.

---

### Edge Cases

- O que acontece se o usuário tentar cadastrar uma tarefa sem título?
- O que acontece se uma tarefa for criada sem data?
- O que acontece se a data selecionada for anterior à data atual?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema MUST permitir que o usuário cadastre uma nova tarefa com título.
- **FR-002**: O sistema MUST permitir que o usuário associe opcionalmente uma data à tarefa, considerando apenas a data (sem horário).
- **FR-003**: O sistema MUST permitir que o usuário remova uma tarefa existente.
- **FR-004**: O sistema MUST exibir a data associada à tarefa na lista, quando houver.
- **FR-005**: O sistema MUST impedir o cadastro de tarefas sem título ou com título composto apenas por espaços.
- **FR-006**: O sistema MUST indicar claramente quando uma tarefa não possui data associada.
- **FR-007**: O sistema MUST manter as tarefas atualizadas após remoção e após recarregar a página.

### Key Entities

- **Tarefa**: Representa uma atividade do usuário, com título, opcionalmente uma data associada e estado de ativo ou concluído.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Usuários conseguem cadastrar uma tarefa em até 10 segundos em uma interação simples.
- **SC-002**: Usuários conseguem remover uma tarefa sem necessidade de instruções adicionais.
- **SC-003**: Usuários conseguem identificar a data associada a uma tarefa sem dificuldade.
- **SC-004**: O sistema mantém a lista de tarefas atualizada após remoção e recarregamento da página.

## Assumptions

- O sistema será usado em uma interface web simples e direta.
- A persistência local das tarefas é desejada para preservar o estado entre recarregamentos.
- O cadastro de tarefas será baseado apenas em data; horário e lembrete com hora não fazem parte do escopo.
