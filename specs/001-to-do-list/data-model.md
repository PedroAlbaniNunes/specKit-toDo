# Data Model: To-Do List

## Entity: Task

| Field | Type | Description | Rules |
|---|---|---|---|
| id | string | Unique identifier for the task | Generated when the task is created |
| text | string | Display text entered by the user | Must be non-empty after trimming whitespace |
| completed | boolean | Indicates whether the task has been marked as done | Defaults to false |
| createdAt | string | Timestamp for creation order | Used to preserve insertion order |

## Validation Rules

- A task text MUST not be empty or composed only of whitespace.
- Duplicate task texts MUST be prevented using a case-insensitive comparison.
- Completed tasks MUST remain in the list and be visually differentiated.

## State Transitions

- Pending -> Completed: The task becomes visually struck through and its state is updated.
- Completed -> Pending: The task returns to the normal style and its state is updated.
- Any state -> Deleted: The task is removed from the list and from storage.
