def normalize_text(text):
    """
    Converts text to lowercase and removes extra spaces
    """
    return text.lower().strip()


def match_issues(review, true_issues):
    """
    Returns number of matched issues
    """
    review = normalize_text(review)

    matches = 0
    for issue in true_issues:
        if issue in review:
            matches += 1

    return matches