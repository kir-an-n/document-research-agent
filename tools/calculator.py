def calculate(expression):
    """
    Safely evaluates a basic math expression like '25 * 4' or '100 / 5'.
    """
    try:
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expression):
            return "Error: expression contains invalid characters."
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"