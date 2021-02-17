#!/usr/bin/python3
"""base model testing"""
import unittest
import json
from models.base_model import BaseModel


class Test_Base_model(unittest.TestCase):
    """base model testing"""
    def test_attributes(self):
        """testing attributes"""
        b1 = BaseModel()
        self.assertEqual(b1.id, b1.id)
