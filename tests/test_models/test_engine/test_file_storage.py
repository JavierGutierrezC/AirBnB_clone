#!/usr/bin/python3
"""Unittest for file_storage"""

import os
import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def test_base_model(self):
        """testing the BaseModel"""
        dog = FileStorage()
        self.assertIs(type(dog.id), str)
        self.assertIs(type(dog.created_at), datetime)
        self.assertIs(type(dog.updated_at), datetime)
        self.assertNotEqual(dog.created_at, dog.updated_at)
        self.assertFalse(dog.updated_at == datetime.utcnow())
        old_updated = dog.updated_at
        dog.save()

    def test_save_model(self):
        """ tests to see if the return type of save is a string """
        dog = FileStorage()
        dog.save()
        self.assertIsInstance(dog.to_dict()['created_at'], str)
        self.assertIsInstance(dog.to_dict()['updated_at'], str)
        self.assertNotEqual(old_updated, dog.updated_at)
        d = dog.to_dict()
        self.assertEqual(type(d), dict)
        self.assertEqual(d['__class__'], "BaseModel")
        self.assertEqual(d['created_at'], dog.created_at.isoformat())
        self.assertEqual(d['updated_at'], dog.updated_at.isoformat())
        self.assertEqual(d['id'], dog.id)


if __name__ == '__main__':
    unittest.main()
