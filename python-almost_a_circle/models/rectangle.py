""" This module contains the class Base """

from models.base import Base

class Rectangle(Base):
    """ 
    defines class Rectangle as a subclass of class Base
    
    Attributes:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the super class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_positive_int('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_positive_int('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_int('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_int('y', value)
        self.__y = value

    def __validate_positive_int(self, attribute_name, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{attribute_name} must be a positive integer")

    def __validate_int(self, attribute_name, value):
        if not isinstance(value, int):
            raise ValueError(f"{attribute_name} must be an integer")



