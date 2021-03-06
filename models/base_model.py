#!/usr/bin/python3
"""the base for all obj in abab"""
import uuid
import datetime
import models


class BaseModel:
    """BaseModel for storing AB&B info"""

    def __init__(self, *args, **kwargs):
        """the init"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key is __class__:
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """how we return srt of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """to save class"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """to make dict repersentation"""
        dict_grayson = self.__dict__.copy()
        dict_grayson["created_at"] = self.created_at.isoformat()
        dict_grayson["updated_at"] = self.updated_at.isoformat()
        dict_grayson["__class__"] = type(self).__name__
        return dict_grayson
