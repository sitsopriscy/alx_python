"""
    _This is a class Square that defines a square_

Returns:
    _'_Square__size'_: _3_
"""
class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
"""
Example: 
"""

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

""" To get 'Square' object has no attribute 'size'
"""
try:
    print(my_square.size)  
except AttributeError as e:
    print(e)

"""
To get 'Square' object has no attribute '__size'
"""
try:
    print(my_square.__size)  
except AttributeError as e:
    print(e)
