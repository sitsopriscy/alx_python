#!/usr/bin/python3
def add(a, b):
    return a + b

if __name__ == "__main__":
    a, b = 1, 2
    print("{} + {} = {}".format(a, b, add(a, b)))

    # print(f"{a} + {b} = {(add(a,b))}")