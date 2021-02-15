#!/usr/bin/python3
"""This is the User class"""
import models


class Place(models.base_model.BaseModel):
    """Stores AirBnB user information"""
    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = ""
        self.number_bathrooms = ""
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__()
