#!/usr/bin/python3

def add(a, b):
    return a+b 

a = 1
b = 2

# Import the add function from add_0.py
# from add_0 import add

print("{} + {} = {}".format(a, b, add(a, b)))

# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     a, b = 1, 2
#     result_string = "{} + {} = {}".format(a, b, add(a, b))
#     print(result_string)

    # print(f"{a} + {b} = {(add(a,b))}")