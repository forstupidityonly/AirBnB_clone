#!/usr/bin/python3
"""the base for all obj in abab"""
import uuid
import datetime


class BaseModel:
    """BaseModel"""

    def __init__(self):
        """the init"""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """how we return srt of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """to save class"""
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        """to make dict repersentation"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": type(self).__name__}
