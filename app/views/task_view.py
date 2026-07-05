from __future__ import annotations

import html
from typing import List

from app.models.task import Task


class TaskView:
    def render_tasks(self, tasks: List[Task]) -> str:
        if not tasks:
            return "<p>Nenhuma tarefa cadastrada.</p>"

        rows = []
        for task in tasks:
            reminder = task.reminder_at.strftime("%d/%m/%Y %H:%M") if task.reminder_at else "Sem lembrete"
            title = html.escape(task.title)
            rows.append(
                f"<li><strong>{title}</strong> — {reminder} — {task.status}"
                f"<form method=\"post\" action=\"/tasks/{task.id}\" style=\"display:inline; margin-left:0.5rem;\">"
                f"<button type=\"submit\">Remover</button></form></li>"
            )
        return "<ul>" + "".join(rows) + "</ul>"
