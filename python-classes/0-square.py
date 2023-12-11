# class Square:
#     """
#     A class that defines a square.

#     Attributes:
#         __size (int): The size of the square.

#     Methods:
#         __init__(self, size): Initializes a new Square instance with the given size.
#     """
    
#     def __init__(self, size):
#         self.__size = size

#     def get_size(self):
#         return self.__size

# # mysquare = Square(3) print(type(mysquare)) print(mysquare.dict_)
    
# mysquare = Square(3)
# print(type(mysquare))
# print(mysquare.__dict__)


#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size

# Example usage:
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

