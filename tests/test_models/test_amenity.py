#!/usr/bin/python3
"""Amenity testing"""
import unittest
import json
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Amenity testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = Amenity()
        self.assertEqual(b1.name, "")