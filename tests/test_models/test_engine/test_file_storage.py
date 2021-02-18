#!/usr/bin/python3
"""file storage testing"""
import unittest
import json
import models
import copy
from models.engine.file_storage import FileStorage


class Test_File_storage(unittest.TestCase):
    """File storage testing"""
    def test_attributes(self):
        """testing attributes"""
        sass = FileStorage()
        self.assertIsInstance(sass.all(), dict)
        test_dict = copy.deepcopy(sass.all())
        tb1 = models.base_model.BaseModel()
        sass.new(tb1)
        self.assertNotEqual(len(test_dict), len(sass.all()))
