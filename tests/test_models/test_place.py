#!/usr/bin/python3
"""place testing"""
import unittest
import json
from models.place import Place


class Test_Place(unittest.TestCase):
    """Place testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = Place()
        self.assertEqual(b1.name, "")
        self.assertEqual(b1.city_id, "")
        self.assertEqual(b1.user_id, "")
        self.assertEqual(b1.description, "")
        self.assertEqual(b1.number_rooms, 0)
        self.assertEqual(b1.number_bathrooms, 0)
        self.assertEqual(b1.max_guest, 0)
        self.assertEqual(b1.price_by_night, 0)
        self.assertEqual(b1.latitude, 0.0)
        self.assertEqual(b1.longitude, 0.0)
        self.assertEqual(b1.amenity_ids, [])
