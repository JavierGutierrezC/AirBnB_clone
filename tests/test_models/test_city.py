#!/usr/bin/python3
"""
Unittest for city
"""
from models.city import City
import datetime
import unittest


class CityCase(unittest.TestCase):
    """Tests for City's attributes and instances """

    cityx = City()

    def test_hasattr(self):
        """Tests for attributes"""
        self.assertTrue(hasattr(self.cityx, "state_id"))
        self.assertTrue(hasattr(self.cityx, "name"))
        self.assertTrue(hasattr(self.cityx, "id"))
        self.assertTrue(hasattr(self.cityx, "created_at"))
        self.assertTrue(hasattr(self.cityx, "updated_at"))

    def test_types(self):
        """Test for instances"""
        self.assertIsInstance(self.cityx..state_id, str)
        self.assertIsInstance(self.cityx.name, str)
        self.assertIsInstance(self.cityx.id, str)
        self.assertIsInstance(self.cityx.created_at, datetime.datetime)
        self.assertIsInstance(self.cityx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
