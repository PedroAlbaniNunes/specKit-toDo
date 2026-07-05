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
            due_date = task.due_date.strftime("%d/%m/%Y") if task.due_date else "Sem data"
            title = html.escape(task.title)
            rows.append(
                f"<li><strong>{title}</strong> — {due_date} — {task.status}"
                f"<form method=\"post\" action=\"/tasks/{task.id}\" style=\"display:inline; margin-left:0.5rem;\">"
                f"<button type=\"submit\">Remover</button></form></li>"
            )
        return "<ul>" + "".join(rows) + "</ul>"
