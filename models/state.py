#!/usr/bin/python3
"""This is the State class"""
import models


class State(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__()
