from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Tuple

from app.services.task_service import TaskService
from app.models.task import Task


class TaskController:
    def __init__(self, service: Optional[TaskService] = None) -> None:
        self.service = service or TaskService()

    def list_tasks(self) -> List[Task]:
        return self.service.list_tasks()

    def create_task(self, title: str, reminder_at: Optional[datetime]) -> Tuple[bool, Optional[str], Optional[Task]]:
        if not title or not title.strip():
            return False, "O título da tarefa é obrigatório.", None

        task = self.service.create_task(title, reminder_at)
        return True, None, task

    def remove_task(self, task_id: str) -> Tuple[bool, Optional[str]]:
        removed = self.service.remove_task(task_id)
        if not removed:
            return False, "Tarefa não encontrada."
        return True, None

    def evaluate_reminders(self) -> List[Task]:
        return self.service.evaluate_reminders()
