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
        self.assertEqual(b1.last_name, "")
        self.assertEqual(b1.email, "")
        self.assertEqual(b1.password, "")
        test_dict = {'created_at': '2021-02-17T02:16:39.282299',
                     'updated_at': '2021-02-17T02:16:39.282323',
                     'id': '8bdb1808-7f1a-4f06-bb0c-324c46f9c632',
                     'email': 'bob_saget@gmail.com', 'password': 'top_secret',
                     'first_name': 'Bob', 'last_name': 'Saget',
                     '__class__': 'User'}
        b2 = User(**test_dict)
        self.assertDictEqual(b2.to_dict(), test_dict)
