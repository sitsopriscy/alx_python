class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

# my_square = Square(5)
# print(my_square.area())

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)


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