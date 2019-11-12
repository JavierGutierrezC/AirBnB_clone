#!/usr/bin/python3
from models.amenity import Amenity
import datetime
import unittest
"""Unittests for amenity"""


class AmenityCase(unittest.TestCase):

    amenitix = Amenity()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.amenitix, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.amenitix, "id"))
        self.assertTrue(hasattr(self.amenitix, "created_at"))
        self.assertTrue(hasattr(self.amenitix, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.amenitix.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.amenitix.id, str)
        self.assertIsInstance(self.amenitix.created_at, datetime.datetime)
        self.assertIsInstance(self.amenitix.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
