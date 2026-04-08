def get_medium_task():
    """
    Returns Python code with logical issues
    """

    code = """def check_even(num):
    if num % 2 == 1:
        return "Even"
    else:
        return "Odd"
"""

    true_issues = [
        "wrong condition",
        "logic error"
    ]

    return code, true_issues