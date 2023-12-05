def raise_exception():
    raise_exception = __import__('4-raise_exception').raise_exception
try:
    raise_exception(1)
except TypeError as te:
    print("Exception raised")
