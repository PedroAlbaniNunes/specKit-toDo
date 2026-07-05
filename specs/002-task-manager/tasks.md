# Tasks: Task Manager

**Input**: Design documents from `/specs/002-task-manager/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the base project structure for the MVC application and documentation updates.

- [ ] T001 Create the app package structure for controllers, models, views, templates, and services
- [ ] T002 [P] Create the MkDocs configuration and documentation folder structure under docs/
- [ ] T003 [P] Create the initial Flask app entrypoint and basic project configuration

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement the in-memory model, controller boundaries, and task status handling.

- [ ] T004 Create the task model and validation rules for title, optional date, and status values
- [ ] T005 [P] Implement the in-memory task repository/store for creation, deletion, and status updates
- [ ] T006 [P] Implement the controller logic for creating, listing, removing, and updating task status
- [ ] T007 Remove reminder-by-time evaluation logic and keep only date-based task data handling

**Checkpoint**: The MVC core can create, list, remove, and update task status before UI work.

---

## Phase 3: User Story 1 - Cadastrar tarefas com data (Priority: P1) 🎯 MVP

**Goal**: Allow the user to add tasks with an optional date.

**Independent Test**: A user can open the app, add a task, and see it appear with the configured date.

### Implementation for User Story 1

- [ ] T008 [US1] Update the task creation form in the view/template layer to collect a date instead of a datetime field
- [ ] T009 [US1] Connect the form submission to the controller and repository using the new date-only input
- [ ] T010 [US1] Display validation feedback for missing titles or invalid date values
- [ ] T011 [US1] Persist task data in memory and reflect it in the rendered list

**Checkpoint**: User Story 1 is fully functional and independently testable.

---

## Phase 4: User Story 2 - Remover tarefas (Priority: P2)

**Goal**: Allow the user to remove tasks from the list.

**Independent Test**: A user can delete a task and confirm it disappears from the list and from the backing store.

### Implementation for User Story 2

- [ ] T012 [US2] Add the delete action to the task list view
- [ ] T013 [US2] Connect removal actions to the controller and repository
- [ ] T014 [US2] Ensure the list refreshes correctly after deletion

**Checkpoint**: User Stories 1 and 2 are both independently functional.

---

## Phase 5: User Story 3 - Gerenciar status e concluir tarefas (Priority: P1)

**Goal**: Allow the user to mark tasks as completed without deleting them.

**Independent Test**: A user can open the app, click the conclude action on a pending task, and see the status change while the task remains stored.

### Implementation for User Story 3

- [ ] T015 [US3] Add a task status field to the model and serialization logic
- [ ] T016 [US3] Add a controller method to update the status of a task
- [ ] T017 [US3] Add a new route in the Flask application to handle status updates from the UI

**Checkpoint**: User Story 3 is independently functional.

---

## Phase 6: User Story 4 - Modernizar a interface visual (Priority: P2)

**Goal**: Refactor the task list UI into a modern card-based experience.

**Independent Test**: A user can view the app and see styled task cards with distinct pending/completed appearance and interactive buttons.

### Implementation for User Story 4

- [ ] T018 [US4] Refactor the HTML template to build a modern layout with a form section and a task card list
- [ ] T019 [US4] Replace the current basic styling with modern CSS including rounded cards, shadows, spacing, and hover effects
- [ ] T020 [US4] Update the task rendering logic to display pending and completed tasks with different visual states
- [ ] T021 [US4] Ensure buttons for conclude and remove use semantic colors and accessible labels

**Checkpoint**: The UI is modernized and visually distinguishes pending and completed tasks.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improve documentation readiness and overall usability.

- [ ] T022 [P] Add documentation pages for architecture and usage in docs/docs/
- [ ] T023 [P] Add deployment notes for Render/Railway and GitHub Pages/Vercel in docs/docs/
- [ ] T024 Validate the end-to-end flow for create, remove, conclude, and visual rendering in the working app
