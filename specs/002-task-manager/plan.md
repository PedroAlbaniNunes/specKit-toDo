# Implementation Plan: Task Manager UI Modernization

**Branch**: `002-task-manager` | **Date**: 2026-07-05 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/002-task-manager/spec.md`

## Summary

Modernizar a interface do usuário do gerenciador de tarefas para oferecer uma experiência visual mais limpa, atrativa e responsiva. A mudança deve preservar a arquitetura MVC atual, concentrando-se na camada de view/template com estilo moderno, cards para as tarefas, botões semânticos e microinterações de hover.

## Technical Context

**Language/Version**: Python 3.11+ com Flask

**Primary Dependencies**: Flask, pytest

**Storage**: Persistência em memória, sem mudança no modelo atual

**Testing**: pytest para testes de backend e validação manual da interface

**Target Platform**: Aplicação web simples hospedável localmente ou em serviços gratuitos

**Project Type**: Web application with MVC structure

**Performance Goals**: Resposta rápida para renderização da interface e ações de cadastro/remoção

**Constraints**: Manter a implementação simples, sem dependências pesadas; usar CSS puro ou um framework leve via CDN

**Scale/Scope**: Ajuste visual da interface existente, sem impactar o fluxo de negócio principal

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- The implementation MUST preserve clean, organized code.
- Business rules MUST stay separate from interface handling.
- The solution MUST follow MVC boundaries between model, view, and controller.
- The project MUST remain organized as a mono-repo with application code and documentation in the same repository.
- User-facing errors MUST be clear and actionable.
- Complexity MUST remain focused on the essential scope of the feature.

## Project Structure

### Documentation (this feature)

```text
specs/002-task-manager/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
app/
├── controllers/
├── models/
├── views/
├── templates/
└── services/

docs/
├── mkdocs.yml
└── docs/

tests/
└── test_task_service.py
```

**Structure Decision**: The UI refresh will remain within the existing MVC structure. The HTML template will be enhanced with modern CSS, while the controller and service layers continue handling business logic without changes unless required for rendering support.

## Phase 0: Research and Design

- Confirm the current template structure and the data passed from the Flask route.
- Decide between CSS puro ou Bootstrap via CDN for the visual refresh.
- Define the visual structure for the page: header, form, feedback messages, task cards, and action buttons.

## Phase 1: Implementation Plan

1. Update the HTML template in [app/templates/index.html](app/templates/index.html) to use a more modern layout.
2. Add styling for container, form, cards, buttons, spacing, shadows, and hover effects.
3. Ensure task rendering from [app/views/task_view.py](app/views/task_view.py) produces card-like HTML structure.
4. Preserve existing routes and controller behavior while adapting the presentation layer.
5. Validate the experience by running the app and checking the rendered UI.

## Phase 2: Validation

- Run the test suite to ensure no regressions.
- Open the application locally and verify that the layout displays tasks as cards with styling and responsive spacing.

## Complexity Tracking

No major complexity concerns are expected for this UI-focused change.
