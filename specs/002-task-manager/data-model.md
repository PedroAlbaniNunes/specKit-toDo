# Data Model: Task Manager

## Entity: Task

| Field | Type | Description | Rules |
|---|---|---|---|
| id | string | Unique identifier | Generated automatically |
| title | string | User-provided task title | Required and non-empty after trimming |
| reminderAt | string or null | Optional reminder date/time | Must be a valid timestamp when provided |
| createdAt | string | Creation timestamp | Generated automatically |
| status | string | Current task status | Example values: pending, notified |

## Validation Rules

- Title MUST be present and trimmed before persistence.
- Reminder time MUST be optional; if provided, it MUST be a valid date/time.
- Reminder notifications MUST be triggered when the current time reaches or passes the scheduled reminder time.

## State Transitions

- Pending -> Notified: The reminder time is reached and the alert is shown.
- Pending -> Removed: The task is deleted.
