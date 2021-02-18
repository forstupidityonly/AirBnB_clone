#!/usr/bin/python3
"""city testing"""
import unittest
import json
from models.city import City


class Test_City(unittest.TestCase):
    """city testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = City()
        self.assertEqual(b1.name, "")
        self.assertEqual(b1.state_id, "")
