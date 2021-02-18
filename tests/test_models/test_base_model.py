#!/usr/bin/python3
"""base model testing"""
import unittest
import json
from models.base_model import BaseModel
import datetime


class Test_Base_model(unittest.TestCase):
    """base model testing"""
    def setUp(self):
        """Runs before each function"""
        self.test_dict = {"id": "72db1a16-1147-4c12-a72b-a91db820f1a6",
        "created_at": "2021-02-18T11:30:32.494714", 
        "updated_at": "2021-02-18T11:30:32.494714"}

    def test_attributes(self):
        """testing attributes"""
        b1 = BaseModel(**self.test_dict)
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(b1.id, self.test_dict["id"])
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.updated_at, datetime.datetime)
        self.assertEqual(b1.created_at, b1.updated_at)
        test_class = b1.to_dict()
        self.assertEqual(test_class["__class__"], "BaseModel")
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)
        b2 = BaseModel()
        self.assertIsInstance(b2, BaseModel)
        self.assertIsInstance(b2.created_at, datetime.datetime)
        self.assertIsInstance(b2.updated_at, datetime.datetime)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2.updated_at, b2.created_at)

        test_str = b1.__str__()[:52]
        test_last = b1.__str__()[-1:]
        self.assertEqual(test_str, "[BaseModel] \
(72db1a16-1147-4c12-a72b-a91db820f1a6) {")
        self.assertEqual(test_last, "}")
