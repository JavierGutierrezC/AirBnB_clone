#!/usr/bin/python3
from models.city import City
import datetime
import unittest
"""Unittests for city"""


class CityCase(unittest.TestCase):

    cityx = City()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.cityx, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.cityx, "id"))
        self.assertTrue(hasattr(self.cityx, "created_at"))
        self.assertTrue(hasattr(self.cityx, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.cityx.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.cityx.id, str)
        self.assertIsInstance(self.cityx.created_at, datetime.datetime)
        self.assertIsInstance(self.cityx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
