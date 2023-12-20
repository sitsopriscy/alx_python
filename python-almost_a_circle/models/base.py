# models/base.py
class Base:
    # private class attribute
    __nb_objects = 0

    # class constructor
    def __init__(self, id=None):
        # public instance attribute
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            

# from models.base import Base
# if __name__ == "__main__":

#     b1 = Base()
#     print(b1.id)

#     b2 = Base()
#     print(b2.id)

#     b3 = Base()
#     print(b3.id)

#     b4 = Base(12)
#     print(b4.id)

#     b5 = Base()
#     print(b5.id)
