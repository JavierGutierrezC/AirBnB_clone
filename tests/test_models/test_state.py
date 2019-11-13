#!/usr/bin/python3
"""
Unittest for State
"""
from models.state import State
import datetime
import unittest


class StateCase(unittest.TestCase):
    """Tests for methods and instances"""
    statex = State()

    def test_hasattr(self):
        """Test for attributes"""
        self.assertTrue(hasattr(self.statex, "name"))
        self.assertTrue(hasattr(self.statex, "id"))
        self.assertTrue(hasattr(self.statex, "created_at"))
        self.assertTrue(hasattr(self.statex, "updated_at"))

    def test_types(self):
        """Test for instances"""
        self.assertIsInstance(self.statex.name, str)
        self.assertIsInstance(self.statex.id, str)
        self.assertIsInstance(self.statex.created_at, datetime.datetime)
        self.assertIsInstance(self.statex.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
