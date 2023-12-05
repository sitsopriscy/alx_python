def safe_print_division(a, b):
    
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

# Example usage:
result = safe_print_division(10, 2)
# print("{:d} / {:d} = {}".format(10, 2, result))
if result is not None:
    print("{} / {} = {}".format(10, 2, result))
else:
    print("None")
