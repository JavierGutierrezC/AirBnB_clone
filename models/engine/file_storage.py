#!/usr/bin/python3
''' '''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage():
    ''' '''


    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' '''
        return FileStorage.__objects

    def new(self, obj):
        from models.base_model import BaseModel
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' '''
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1[key] = value.to_dict()
        with open("{}".format(FileStorage.__file_path), "w") as Newdict:
            json.dump(dict1, Newdict)

    def reload(self):
        ''' '''
        try:
            with open(FileStorage.__file_path, 'r') as a_file:
                new_obj = json.load(a_file)
                for a in new_obj.values():
                    n_name = a["__class__"]
                    self.new(eval(n_name)(**a))
        except FileNotFoundError:
            return
