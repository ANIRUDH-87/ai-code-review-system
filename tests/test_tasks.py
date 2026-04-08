from tasks.task_manager import get_task


def test_easy_task():
    code, issues = get_task("easy")

    assert isinstance(code, str)
    assert isinstance(issues, list)
    assert len(issues) > 0


def test_medium_task():
    code, issues = get_task("medium")

    assert isinstance(code, str)
    assert isinstance(issues, list)
    assert len(issues) > 0


def test_hard_task():
    code, issues = get_task("hard")

    assert isinstance(code, str)
    assert isinstance(issues, list)
    assert len(issues) > 0