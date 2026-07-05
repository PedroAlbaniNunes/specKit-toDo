# Todo List Constitution

<!--
Sync Impact Report
- Version change: 1.0.0 → 1.1.0
- Modified principles: III. Essential Focus with Clear User Errors → IV. Essential Focus with Clear User Errors; added III. MVC Architecture by Default
- Added sections: none
- Removed sections: none
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: none
-->

## Core Principles

### I. Clean and Organized Code
Production code MUST be readable, modular, and organized by responsibility. Functions, classes, and modules MUST have a single clear purpose, and duplication MUST be reduced through shared abstractions. Complexity MUST be justified by user value and kept as low as possible.

### II. Separation of Business Rules from Interface Handling
Business rules MUST be implemented in dedicated domain or service layers that are independent from UI, controllers, or presentation logic. Interface components MUST only collect input, render output, and delegate decisions to the business layer. This separation MUST be preserved in new features and refactors.

### III. MVC Architecture by Default
The project MUST follow the MVC architectural pattern, with clear boundaries between Model, View, and Controller responsibilities. Models MUST encapsulate data and domain rules, Views MUST focus on presentation, and Controllers MUST coordinate interactions and application flow. This structure MUST be used unless a future change explicitly justifies a different architecture.

### IV. Essential Focus with Clear User Errors
The system MUST focus on the essential user flow and avoid unnecessary features or complexity. User-facing errors MUST be explicit, actionable, and understandable, with no silent failures. When a failure occurs, the interface MUST provide a clear message and the underlying cause MUST be handled at the appropriate layer.

## Implementation Constraints
All changes MUST preserve readability, maintainability, and separation of concerns. New dependencies or architectural patterns MUST be introduced only when they solve a real need and do not increase complexity without justification. Business-rule changes MUST remain testable without depending on interface details. The project MUST be organized as a mono-repo, keeping application code and documentation such as MkDocs in the same repository to simplify version control and deployment.

## Development Workflow
Every change MUST be reviewed against these principles before merge. Features that add complexity beyond the essential scope MUST include a clear justification. Error handling MUST be reviewed for clarity and alignment with the user's task, not only for technical correctness. New modules or components MUST be placed in a structure that preserves MVC boundaries and mono-repo organization.

## Governance
This constitution supersedes local preferences when requirements conflict. Amendments MUST be documented, reviewed, and versioned with a clear rationale. Compliance with these principles MUST be checked during implementation planning and review, and any deviation MUST be explicitly justified.

**Version**: 1.1.0 | **Ratified**: 2026-07-05 | **Last Amended**: 2026-07-05
