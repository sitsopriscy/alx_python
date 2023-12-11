class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the given size.
    """
    
    def __init__(self, _Square__size):
        self.Square__size = _Square__size

    def square(self):
        return self.Square__size
    
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
pass
