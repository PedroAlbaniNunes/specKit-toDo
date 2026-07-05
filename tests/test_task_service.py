from datetime import date, datetime, timedelta

from app.controllers.task_controller import TaskController


def test_create_task_and_remove_task():
    controller = TaskController()

    created, error, task = controller.create_task("Estudar", None)

    assert created is True
    assert error is None
    assert task is not None
    assert task.title == "Estudar"

    removed, remove_error = controller.remove_task(task.id)

    assert removed is True
    assert remove_error is None
    assert controller.list_tasks() == []


def test_create_task_with_date_only():
    controller = TaskController()
    due_date = date(2026, 7, 10)

    created, error, task = controller.create_task("Revisar documentação", due_date)

    assert created is True
    assert error is None
    assert task is not None
    assert task.due_date == due_date
