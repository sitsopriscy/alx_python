def safe_print_division(a, b):
    # safe_print_division = __import__('3-safe_print_division').safe_print_division
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

# Example usage:
result = safe_print_division(10, 2)
print("{:d} / {:d} = {}".format(10, 2, result))
