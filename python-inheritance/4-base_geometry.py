#!/usr/bin/python3

"""Public instance method: def area(self):

    Raises:
        Exception(area()): message(is not implemented)
"""

class BaseGeometry:
    """This is class defines class BaseGeometry.
    """
    def area(self):
        
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

bg = BaseGeometry()

# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))