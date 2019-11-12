#!/usr/bin/python3
''' module for class base '''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ Class base for the project """
    def __init__(self, *args, **kwargs):
        """ to initialize """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'name':
                    self.name = value
                elif key == 'my_number':
                    self.my_number = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ str method """
        return("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ method to save the new object """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to convert the object to a dictionary """
        dict1 = dict(self.__dict__)
        dict1["__class__"] = self.__class__.__name__
        dict1["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict1["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return(dict1)
