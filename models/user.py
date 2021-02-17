#!/usr/bin/python3
"""This is the User class"""
import models


class User(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            super().__init__()
        else:
            super().__init__(**kwargs)
