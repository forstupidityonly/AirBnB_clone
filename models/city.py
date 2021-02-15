#!/usr/bin/python3
"""This is the User class"""
import models


class User(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__()
        
