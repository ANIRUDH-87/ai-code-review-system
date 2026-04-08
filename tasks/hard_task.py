def get_hard_task():
    """
    Returns Python code with optimization and edge-case issues
    """

    code = """def find_max(arr):
    max_val = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
"""

    true_issues = [
        "fails for negative numbers",
        "inefficient loop"
    ]

    code = """def divide(a, b):
        return a / b
    """

    true_issues = [
        "division by zero",
        "no error handling"
    ]

    return code, true_issues