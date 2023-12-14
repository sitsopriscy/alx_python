# #!/usr/bin/python3
# """ this module contains subclass Rectange that inherits from class BaseGeometry """

# class BaseGeometry:
#     """ defines the class BaseGeometry """

#     def area(self):
#         """
#         Calculate the area.

#         Raises:
#             Exception: This method is not implemented in the base class.
#         """
#         raise Exception("area() is not implemented")
    
#     def integer_validator(self, name, value):
#         """
#         Validate if the given value is an integer and greater than 0.

#         Args:
#             name (str): The name of the value being validated.
#             value (int): The value to be validated.

#         Raises:
#             TypeError: If the value is not an integer.
#             ValueError: If the value is less than or equal to 0.
#         """  
              
#         if type(value) != int:
#             raise TypeError("{} must be an integer".format(name))
#         if value <= 0:
#             raise ValueError("{} must be greater than 0".format(name))


# class Rectangle(BaseGeometry):
#     """ defines the subclass Rectangle inheritting from class BaseGeometry """

#     def __init__(self, width, height):
#         """ 
#         initializes an instance of the class Rectange with width and height
        
#         Args:
#             width: must be private and a positive integer
#             height: must be private an a positive integer
        
#         check with integer_validator
#         """
        
#         self.integer_validator("width", width)
#         self.integer_validator("height", height)
#         self.__width = width
#         self.__height = height
    


# !/usr/bin/python3

"""_This module is for a class Rectangle that inherits from BaseGeometry_

    Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
"""


class BaseGeometry:
    """This is class defines class BaseGeometry.
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """This is a class Rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"


# r = Rectangle(3, 5)

# print(r)
# print(dir(r))

# try:
#     print("Rectangle: {} - {}".format(r.width, r.height))
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     r2 = Rectangle(4, True)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
    
# rectangle = Rectangle(width=5, height=10)
# attributes = dir(rectangle)
# has_width_attribute = '_Rectangle__width' in attributes

# print(has_width_attribute)
