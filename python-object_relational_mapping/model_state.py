# Write a python file that contains the class definition of a State and an instance Base = declarative_base():

# State class:
# inherits from Base Tips
# links to the MySQL table states
# class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
# class attribute name that represents a column of a string with maximum 128 characters and can’t be null
# You must use the module SQLAlchemy
# Your script should connect to a MySQL server running on localhost at port 3306
# WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)


#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" importing attributes from SQLAlchemy """

Base = declarative_base()


class State(Base):
    """creating class States that inherits from Base"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
