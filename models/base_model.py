#!/usr/bin/python3
# module for class base
from uuid import uuid4
from datetime import datetime


class BaseModel():

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict1 = dict(self.__dict__)
        dict1["__class__"] = self.__class__.__name__
        dict1["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict1["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return(dict1)
