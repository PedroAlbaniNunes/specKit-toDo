from __future__ import annotations

from datetime import datetime

from flask import Flask, jsonify, redirect, render_template, request, url_for

from app.controllers.task_controller import TaskController
from app.views.task_view import TaskView

app = Flask(__name__)
controller = TaskController()
view = TaskView()


def _evaluate_and_prepare() -> tuple[list[dict], list[dict], list[dict]]:
    notified = controller.evaluate_reminders()
    tasks = controller.list_tasks()
    return notified, tasks, view.render_tasks(tasks)


@app.route("/", methods=["GET"])
def index() -> str:
    notified, tasks, tasks_html = _evaluate_and_prepare()
    return render_template(
        "index.html",
        tasks_html=tasks_html,
        error=None,
        success=None,
        notifications=notified,
    )


@app.route("/tasks", methods=["POST"])
def create_task() -> str:
    title = request.form.get("title", "")
    reminder_raw = request.form.get("reminder_at")
    reminder_at = datetime.fromisoformat(reminder_raw) if reminder_raw else None
    created, message, _ = controller.create_task(title, reminder_at)
    notified, tasks, tasks_html = _evaluate_and_prepare()
    if created:
        return render_template(
            "index.html",
            tasks_html=tasks_html,
            error=None,
            success="Tarefa criada com sucesso.",
            notifications=notified,
        )
    return render_template(
        "index.html",
        tasks_html=tasks_html,
        error=message,
        success=None,
        notifications=notified,
    )


@app.route("/tasks/<task_id>", methods=["POST", "DELETE"])
def remove_task(task_id: str):
    removed, message = controller.remove_task(task_id)
    if request.method == "DELETE":
        if removed:
            return jsonify({"status": "removed"}), 200
        return jsonify({"error": message}), 404

    notified, tasks, tasks_html = _evaluate_and_prepare()
    if removed:
        return render_template(
            "index.html",
            tasks_html=tasks_html,
            error=None,
            success="Tarefa removida com sucesso.",
            notifications=notified,
        )
    return render_template(
        "index.html",
        tasks_html=tasks_html,
        error=message,
        success=None,
        notifications=notified,
    )


if __name__ == "__main__":
    app.run(debug=True)
