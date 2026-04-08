from env.utils import normalize_text


def calculate_score(review, true_issues):
    review = normalize_text(review)

    matches = 0

    for issue in true_issues:
        issue_words = issue.lower().split()

        # match if at least one keyword is present
        if any(word in review for word in issue_words):
            matches += 1

    total = len(true_issues)

    coverage = matches / total

    # more granular scoring
    if coverage == 1.0:
        return 1.0
    elif coverage >= 0.5:
        return 0.7
    elif coverage > 0:
        return 0.3
    else:
        return 0.0