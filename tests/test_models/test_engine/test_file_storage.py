#!/usr/bin/python3
"""file storage testing"""
import unittest
import json
from models.engine.file_storage import FileStorage


class Test_File_storage(unittest.TestCase):
    """File storage testing"""
    def test_attributes(self):
        """testing attributes"""
        sass = FileStorage()
        self.assertEqual(sass.all(), {})