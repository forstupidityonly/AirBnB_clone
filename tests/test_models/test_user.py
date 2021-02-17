#!/usr/bin/python3
"""user testing"""
import unittest
import json
from models.user import User


class Test_User(unittest.TestCase):
    """user testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = User()
        self.assertEqual(b1.first_name, "")