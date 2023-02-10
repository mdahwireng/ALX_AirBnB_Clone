#!/usr/bin/python3
""" This module defines base model needed for the AirBnB console"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ 
    Class to create ......
    
    Methods:
        ......
        ......
        ......
    """
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now() #.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now() #.strftime("%Y-%m-%dT%H:%M:%S.%f")
        pass

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now() #.strftime("%Y-%m-%dT%H:%M:%S.%f")
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        pass