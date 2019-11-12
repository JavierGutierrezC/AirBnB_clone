#!usr/bin/python3
from models.place import Place
import datetime
import unittest
"""Unittests for Place"""


class AmenityCase(unittest.TestCase):

    placex = Place()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.placex, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.placex, "id"))
        self.assertTrue(hasattr(self.placex, "created_at"))
        self.assertTrue(hasattr(self.placex, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.placex.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.placex.id, str)
        self.assertIsInstance(self.placex.created_at, datetime.datetime)
        self.assertIsInstance(self.placex.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
