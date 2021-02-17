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
        self.assertEqual(b1.created_at, b1.created_at)
        self.assertEqual(b1.updated_at, b1.updated_at)
        self.assertDictEqual(b1.to_dict(), b1.to_dict())
