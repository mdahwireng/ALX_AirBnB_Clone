#!/usr/bin/python3
""" This module defines base model needed for the AirBnB console"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class to create a base model for the methods and attributes common
    to other objects needed for the AirBnB project\n\n
    Methods:
        __init__: Initializes the BaseModel object
                    Returns None\n
                    Args: Takes no arguments\n\n
        __str__ : Prints visual details in the order shown :
                    [<class name>] (<self.id>) <self.__dict__>
                    Returns a string in the format shown above\n
                    Args: Takes no arguments\n\n
        save : Updates the public instance attribute updated_at with the
                currentd atetime
                Returns None\n
                Args: Takes no arguments\n\n
        to_dict : Returns a dictionary containing all keys/values of
                __dict__ of the instance\n
                Args: Takes no arguments"""
    def __init__(self) -> None:
        """Initializes the BaseModel object\n
        Returns None\n
        Args: Takes no arguments"""
        self.id = str(uuid4())
        self.created_at = datetime.now()  # .strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Prints visual details in the order shown :
            [<class name>] (<self.id>) <self.__dict__>
        Returns a string in the format shown above\n
        Args: Takes no arguments"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute updated_at with the
        current datetime
        Returns None\n
        Args: Takes no arguments"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/values of __dict__
        of the instance\n
        Args: Takes no arguments"""
        hld_dict = dict({"__class__": self.__class__.__name__},
                        **self.__dict__)
        hld_dict["updated_at"] = hld_dict["updated_at"].isoformat()
        hld_dict["created_at"] = hld_dict["created_at"].isoformat()
        return hld_dict
