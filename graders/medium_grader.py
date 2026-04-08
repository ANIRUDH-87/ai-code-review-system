from graders.scoring import calculate_score


def grade_medium(review, true_issues):
    """
    Grades medium task
    """
    return calculate_score(review, true_issues)