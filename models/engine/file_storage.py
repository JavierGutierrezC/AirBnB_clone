#!/usr/bin/python3
''' File Storage module  for save the objects '''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage():
    ''' File Storage Class '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Show all the objects of the class '''
        return FileStorage.__objects

    def new(self, obj):
        """ For a new object """
        from models.base_model import BaseModel
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' For serialize the object and save it to a file '''
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1[key] = value.to_dict()
        with open("{}".format(FileStorage.__file_path), "w") as Newdict:
            json.dump(dict1, Newdict)

    def reload(self):
        ''' Open the file and extract the object previously stored '''
        try:
            with open(FileStorage.__file_path, 'r') as a_file:
                new_obj = json.load(a_file)
                for a in new_obj.values():
                    n_name = a["__class__"]
                    self.new(eval(n_name)(**a))
        except FileNotFoundError:
            return
