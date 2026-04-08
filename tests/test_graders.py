from graders.easy_grader import grade_easy
from graders.medium_grader import grade_medium
from graders.hard_grader import grade_hard


def test_easy_grader():
    review = "missing colon indentation error"
    issues = ["missing colon", "indentation error"]

    score = grade_easy(review, issues)

    assert score == 1.0


def test_medium_grader():
    review = "logic error"
    issues = ["wrong condition", "logic error"]

    score = grade_medium(review, issues)

    assert score in [0.5, 1.0]


def test_hard_grader():
    review = "inefficient loop"
    issues = ["fails for negative numbers", "inefficient loop"]

    score = grade_hard(review, issues)

    assert score in [0.5, 1.0]