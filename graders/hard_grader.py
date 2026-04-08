from graders.scoring import calculate_score


def grade_hard(review, true_issues):
    """
    Grades hard task
    """
    return calculate_score(review, true_issues)