B#!/usr/bin/python3
"""File storage module: UPDATE THIS LINE LATER"""
import json
import os.path


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
            json.dump(savedict, f)

    def reload(self):
        """reloads a json file to a dictionary"""
        redict = {}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                redict = json.load(f)
            for key in redict:
                tmp = key[__class__](key)
                self.new(tmp)
