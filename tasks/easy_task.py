def get_easy_task():
    """
    Returns a simple Python code with a syntax issue
    """

    code = """def greet()
    print("Hello World")"""

    true_issues = [
        "missing colon",
        "indentation error"
    ]

    return code, true_issues