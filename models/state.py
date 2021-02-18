#!/usr/bin/python3
"""This is the State class"""
import models


class State(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs != {}:
            super().__init__(**kwargs)
        else:
            self.name = ""
            super().__init__()
