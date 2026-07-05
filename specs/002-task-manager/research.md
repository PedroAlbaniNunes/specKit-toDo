# Research: Task Manager

## Decisions

- Decision: Structure the solution as an MVC web application.
- Rationale: This clearly separates task data handling, user interaction, and business rules, which supports scalability and maintainability.
- Decision: Use in-memory persistence only.
- Rationale: The requirement explicitly excludes databases, and in-memory storage is suitable for a simple demo or learning-oriented application.
- Decision: Use MkDocs for technical documentation in the same repository.
- Rationale: This keeps application code and documentation together, simplifying version control and deployment.
- Decision: Design the app to be deployable to free hosting platforms.
- Rationale: The application should be easy to host on Render/Railway and the docs on GitHub Pages/Vercel.

## Alternatives Considered

- Using a database-backed backend.
  - Alternatives considered: Rejected because the requirement mandates in-memory persistence only.
- Using a static frontend-only approach.
  - Alternatives considered: Rejected because the reminder logic and MVC structure are better served by a small server-side application.
- Using a documentation tool other than MkDocs.
  - Alternatives considered: Rejected because MkDocs integrates well with GitHub Pages and Vercel.
