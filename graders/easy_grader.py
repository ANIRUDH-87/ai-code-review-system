from graders.scoring import calculate_score


def grade_easy(review, true_issues):
    """
    Grades easy task
    """
    return calculate_score(review, true_issues)