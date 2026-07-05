from __future__ import annotations

import html
from typing import List

from app.models.task import Task


class TaskView:
    def render_tasks(self, tasks: List[Task]) -> str:
        if not tasks:
            return '<div class="empty-state">Nenhuma tarefa cadastrada.</div>'

        cards = []
        for task in tasks:
            due_date = task.due_date.strftime("%d/%m/%Y") if task.due_date else "Sem data"
            title = html.escape(task.title)
            status_label = "Concluída" if task.is_completed() else "Pendente"
            status_class = "completed" if task.is_completed() else "pending"
            action_button = "" if task.is_completed() else (
                f'<form method="post" action="/tasks/{task.id}/complete" class="inline-form">'
                f'<button type="submit" class="btn btn-success">Concluir</button></form>'
            )
            cards.append(
                f'<article class="task-card {status_class}">'
                f'<div class="task-header">'
                f'<h3>{title}</h3>'
                f'<span class="status-badge {status_class}">{status_label}</span>'
                f'</div>'
                f'<p class="task-date">📅 {due_date}</p>'
                f'<div class="task-actions">'
                f'{action_button}'
                f'<form method="post" action="/tasks/{task.id}" class="inline-form">'
                f'<button type="submit" class="btn btn-danger">Excluir</button></form>'
                f'</div>'
                f'</article>'
            )
        return '<div class="task-list">' + ''.join(cards) + '</div>'
