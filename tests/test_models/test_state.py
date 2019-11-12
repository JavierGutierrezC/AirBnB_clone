#!/usr/bin/python3
from models.state import State
import datetime
import unittest
""" Unittests for state"""


class StateCase(unittest.TestCase):

    statex = State()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.statex, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.statex, "id"))
        self.assertTrue(hasattr(self.statex, "created_at"))
        self.assertTrue(hasattr(self.statex, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.statex.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.statex.id, str)
        self.assertIsInstance(self.statex.created_at, datetime.datetime)
        self.assertIsInstance(self.statex.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
