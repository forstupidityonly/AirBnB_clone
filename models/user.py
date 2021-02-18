#!/usr/bin/python3
"""This is the User class"""
import models


class User(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
    
