def function_with_uncommon_error(data):
    try:
        # ... some code that might raise an exception ...
        result = 1 / 0  # Example: ZeroDivisionError
        return result
    except Exception as e:
        # In this example, we don't handle the specific exception
        # This is an uncommon error because it's a very broad
        # exception handler that could mask the actual cause.
        print(f"An error occurred: {e}")
        return None

# Incorrect usage because the error is not handled specifically
result = function_with_uncommon_error(some_data)