#!/usr/bin/python3
"""This is the User class"""
import models


class Review(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__()
