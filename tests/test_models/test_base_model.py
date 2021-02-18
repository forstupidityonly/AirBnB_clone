#!/usr/bin/python3
"""base model testing"""
import unittest
import json
from models.base_model import BaseModel
import datetime


class Test_Base_model(unittest.TestCase):
    """base model testing"""
    def test_attributes(self):
        """testing attributes"""
        test_dict = {"id": "72db1a16-1147-4c12-a72b-a91db820f1a6",
        "created_at": "2021-02-18T11:30:32.494714", 
        "updated_at": "2021-02-18T11:30:32.494714"}
        b1 = BaseModel(**test_dict)
        self.assertEqual(b1.id, test_dict["id"])