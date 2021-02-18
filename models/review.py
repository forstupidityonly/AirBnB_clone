#!/usr/bin/python3
"""This is the User class"""
import models


class Review(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    place_id = ""
    user_id = ""
    text = ""
