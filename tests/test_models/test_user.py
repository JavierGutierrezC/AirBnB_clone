#!/usr/bin/python3
"""
Unitest for user
"""
from models.user import User
import datetime
import unittest


class UserCase(unittest.TestCase):
    """Test for cases and methods"""
    userx = User()

    def test_hasattr(self):
        """Tests for attributes"""
        self.assertTrue(hasattr(self.userx, "email"))
        self.assertTrue(hasattr(self.userx, "password"))
        self.assertTrue(hasattr(self.userx, "first_name"))
        self.assertTrue(hasattr(self.userx, "las_name"))
        self.assertTrue(hasattr(self.userx, "name"))
        self.assertTrue(hasattr(self.userx, "id"))
        self.assertTrue(hasattr(self.userx, "created_at"))
        self.assertTrue(hasattr(self.userx, "updated_at"))

    def test_types(self):
        """Tests for Instances"""
        self.assertIsInstance(self.userx.email, str)
        self.assertIsInstance(self.userx.password, str)
        self.assertIsInstance(self.userx.first_name, str)
        self.assertIsInstance(self.userx.las_name, str)
        self.assertIsInstance(self.userx.name, str)
        self.assertIsInstance(self.userx.id, str)
        self.assertIsInstance(self.userx.created_at, datetime.datetime)
        self.assertIsInstance(self.userx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
