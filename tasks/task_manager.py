from tasks.easy_task import get_easy_task
from tasks.medium_task import get_medium_task
from tasks.hard_task import get_hard_task


def get_task(task_type):
    """
    Returns code and true issues based on task type
    """

    if task_type == "easy":
        return get_easy_task()

    elif task_type == "medium":
        return get_medium_task()

    elif task_type == "hard":
        return get_hard_task()

    else:
        raise ValueError("Invalid task type")