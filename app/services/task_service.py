from __future__ import annotations

from datetime import date
from typing import List, Optional

from app.models.task import Task


class TaskService:
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def create_task(self, title: str, due_date: Optional[date]) -> Task:
        task = Task(
            id=self._next_id(),
            title=title.strip(),
            due_date=due_date,
        )
        self._tasks.append(task)
        return task

    def remove_task(self, task_id: str) -> bool:
        initial_length = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) != initial_length

    def complete_task(self, task_id: str) -> bool:
        for task in self._tasks:
            if task.id == task_id:
                task.status = "completed"
                return True
        return False

    def evaluate_reminders(self) -> List[Task]:
        return []

    def _next_id(self) -> str:
        return str(len(self._tasks) + 1)
