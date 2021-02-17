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
        test_dict = {'created_at': '2021-02-17T02:16:39.282299',
                     'updated_at': '2021-02-17T02:16:39.282323',
                     'id': '8bdb1808-7f1a-4f06-bb0c-324c46f9c632',
                     '__class__': 'BaseModel'}
        b2 = BaseModel(**test_dict)
        self.assertDictEqual(b2.to_dict(), test_dict)
        self.assertEqual(b2.id, '8bdb1808-7f1a-4f06-bb0c-324c46f9c632')
        self.assertEqual(b2.created_at, datetime.datetime(2021, 2, 17, 2, 16,
                                                          39, 282299))
        self.assertEqual(b2.updated_at, datetime.datetime(2021, 2, 17, 2, 16,
                                                          39, 282323))
        self.assertEqual(str(b2), str(b2))
        b2.save()
        self.assertEqual(b2.updated_at, b2.updated_at)
        self.assertEqual(b2.__class__, BaseModel)

        b1 = BaseModel()
        self.assertEqual(type(b1), BaseModel)
