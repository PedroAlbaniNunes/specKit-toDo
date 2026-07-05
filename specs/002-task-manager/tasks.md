# Tasks: Task Manager

**Input**: Design documents from `/specs/002-task-manager/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the base project structure for the MVC application and MkDocs documentation.

- [ ] T001 Create the app package structure for controllers, models, views, templates, and services
- [ ] T002 [P] Create the MkDocs configuration and documentation folder structure under docs/
- [ ] T003 [P] Create the initial Flask/FastAPI app entrypoint and basic project configuration

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement the in-memory model, controller boundaries, and reminder orchestration logic.

- [ ] T004 Create the task model and validation rules for title and reminder data
- [ ] T005 [P] Implement the in-memory task repository/store for creation and deletion operations
- [ ] T006 [P] Implement the controller logic for creating, listing, and removing tasks
- [ ] T007 Implement reminder evaluation logic that checks due tasks and triggers notifications

**Checkpoint**: The MVC core can create, list, remove, and evaluate reminders before story-specific UI work.

---

## Phase 3: User Story 1 - Cadastrar tarefas com lembrete (Priority: P1) 🎯 MVP

**Goal**: Allow the user to add tasks with an optional reminder.

**Independent Test**: A user can open the app, add a task, and see it appear with the configured reminder data.

### Implementation for User Story 1

- [ ] T008 [US1] Build the task creation form in the view/template layer
- [ ] T009 [US1] Connect the form submission to the controller and repository
- [ ] T010 [US1] Display validation feedback for missing titles or invalid reminder values
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

## Phase 5: User Story 3 - Notificar lembretes (Priority: P2)

**Goal**: Notify the user when a reminder time is reached.

**Independent Test**: A user can create a task with a reminder and observe a visible notification when the time arrives.

### Implementation for User Story 3

- [ ] T015 [US3] Implement a visible reminder alert in the UI layer
- [ ] T016 [US3] Trigger reminder evaluation periodically or on page refresh according to the selected approach
- [ ] T017 [US3] Mark reminded tasks appropriately so repeated notifications are avoided

**Checkpoint**: User Story 3 is independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improve the deployment readiness, documentation, and overall usability.

- [ ] T018 [P] Add documentation pages for architecture and usage in docs/docs/
- [ ] T019 [P] Add deployment notes for Render/Railway and GitHub Pages/Vercel in docs/docs/
- [ ] T020 Validate the end-to-end flow for create, remove, and reminder notification in the working app
