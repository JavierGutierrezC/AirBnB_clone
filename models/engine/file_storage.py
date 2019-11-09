#!/usr/bin/python3

from models import Base_Model
import json

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self,obj):
        key = obj.__class__.__name__.id + "." obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1[key] = value.to_dict
        with open("{}.json".format(FileStorage.__file_path), "w") as Newdict:
            json.dump(dict1, Newdict)
