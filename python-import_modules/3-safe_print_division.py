def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

result = safe_print_division(12, 0)
print(result)

result = safe_print_division(12, 2)
print(result)
