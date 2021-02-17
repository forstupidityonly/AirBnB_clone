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
                     'id': '8bdb1808-7f1a-4f06-bb0c-324c46f9c632'}
        b2 = BaseModel(**test_dict)
        td2 = b2.to_dict()
        self.assertEqual(td2["__class__"], "BaseModel")
        self.assertEqual(b2.id, '8bdb1808-7f1a-4f06-bb0c-324c46f9c632')
        self.assertEqual(b2.created_at, datetime.datetime(2021, 2, 17, 2, 16,
                                                          39, 282299))
        self.assertEqual(b2.updated_at, datetime.datetime(2021, 2, 17, 2, 16,
                                                          39, 282323))
        test_str = b2.__str__()[:52]
        test_last = b2.__str__()[-1:]
        self.assertEqual(test_str, "[BaseModel] \
(8bdb1808-7f1a-4f06-bb0c-324c46f9c632) {")
        self.assertEqual(test_last, "}")
        b2.save()
        up_time = b2.updated_at
        self.assertEqual(b2.updated_at, up_time)
        self.assertEqual(b2.__class__, BaseModel)

        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(b1.created_at, b1.updated_at)
        self.assertNotEqual(b1.id, "")
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.updated_at, datetime.datetime)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(b2.updated_at, datetime.datetime)
        self.assertIsInstance(b2.created_at, datetime.datetime)
        self.assertNotEqual(b2.__dict__, b2.to_dict())
