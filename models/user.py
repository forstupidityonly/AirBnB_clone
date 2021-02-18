#!/usr/bin/python3
"""This is the User class"""
import models


class User(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
