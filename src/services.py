from datetime import date

from src.exceptions import TaskNotFoundError
from src.logger import logger
from src.models import Task

tasks: dict[int, Task] = {}


def create_task(
    title: str,
    description: str,
    due_date: date,
) -> Task:
    task_id = max(tasks.keys(), default=0) + 1

    task = Task(
        id=task_id,
        title=title,
        description=description,
        due_date=due_date,
    )

    tasks[task_id] = task
    logger.info("Created task: %s", task)

    return task


def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)

    if task is None:
        raise TaskNotFoundError(f"Task with id {task_id} not found")

    return task
