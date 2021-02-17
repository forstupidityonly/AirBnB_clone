#!/usr/bin/python3
"""review testing"""
import unittest
import json
from models.review import Review


class Test_Review(unittest.TestCase):
    """review testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = Review()
        self.assertEqual(b1.text, "")