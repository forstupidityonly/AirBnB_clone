#!/usr/bin/python3
"""File storage module: UPDATE THIS LINE LATER"""
import json
import os.path
import models


class FileStorage:
    """Storage system for AirBnB clone"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all saved objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to storage"""
        filename = type(obj).__name__ + "." + str(obj.id)
        self.__objects[filename] = obj

    def save(self):
        """Saves objects to json file"""
        savedict = {}
        for x in self.__objects:
            savedict[x] = self.__objects[x].to_dict()

        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(savedict))

    def reload(self):
        """reloads a json file to a dictionary"""
        redict = {}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                redict = json.loads(f.read())
                for key in redict:
                    cn = redict[key]["__class__"]
                    func = models.class_dict[cn]
                    self.__objects[key] = func(**redict[key])
