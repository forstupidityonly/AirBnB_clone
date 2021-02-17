#!/usr/bin/python3
"""state model testing"""
import unittest
import json
from models.state import State


class Test_State(unittest.TestCase):
    """State testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = State()
        self.assertEqual(b1.name, "")