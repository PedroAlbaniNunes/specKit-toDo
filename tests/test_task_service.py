from datetime import datetime, timedelta

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


def test_reminder_is_marked_when_due():
    controller = TaskController()
    reminder_time = datetime.now() - timedelta(minutes=1)

    created, error, task = controller.create_task("Revisar documentação", reminder_time)

    assert created is True
    assert error is None

    notified_tasks = controller.evaluate_reminders()

    assert len(notified_tasks) == 1
    assert notified_tasks[0].id == task.id
    assert notified_tasks[0].status == "notified"
