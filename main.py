from datetime import date

from src.services import create_task, get_task

if __name__ == "__main__":
    task = create_task(
        title="Подготовить README",
        description="Добавить инструкцию запуска проекта",
        due_date=date(2027, 6, 30),
    )

    retrieved_task = get_task(task.id)
    print(retrieved_task)
