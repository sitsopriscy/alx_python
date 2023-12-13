# """
# This module defines a Square class.

# The Square class represents a square geometric shape and has a private
# instance attribute for the size.

# Example:
#     square = Square(5)
#     print(square.get_area())  # Output: 25
# """


# class Square:
#     """This class defines a Square.

#     Attributes:
#         __size (int): Private instance attribute representing the size of the square.
#     """

#     def __init__(self, size=0):
#         """Initializes a new instance of the Square class.

#         Args:
#             size (int): The size of the square.
#         """
#         self.__size = size

#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with the given size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        size = int
        if size != int(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


