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