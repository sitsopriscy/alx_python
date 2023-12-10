"""_summary_

Returns:
    _type_: _description_
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


# my_square = Square(3)
# print(type(my_square))
# print(my_square.__dict__)


# """ To get 'Square' object has no attribute 'size'
# """
# try:
#     print(my_square.size)  
# except AttributeError as e:
#     print(e)

# '''
# To get 'Square' object has no attribute '__size'
# '''
# try:
#     print(my_square.__size)  
# except AttributeError as e:
#     print(e)

# square1 = Square(5)
# print("Size of square1:", square1.get_size())
# print("Area of square1:", square1.area())