# def raise_exception_msg(message=""):
#     raise NameError(message)
#     raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg
    
# try:
#     raise_exception_msg("")
# except NameError as ne:
#     print(ne)

def raise_exception_msg(message=""):
    raise NameError(message)

if __name__ == "__main__":
    raise_exception_msg("C is fun")
