#!/usr/bin/python3
"""
Unittest for place
"""
from models.place import Place
import datetime
import unittest


class PlaceCase(unittest.TestCase):
    """Test for metthods and instances for place"""
    placex = Place()

    def test_hasattr(self):
        """Test for attributes"""
        self.assertTrue(hasattr(self.placex, "city_id"))
        self.assertTrue(hasattr(self.placex, "user_id"))
        self.assertTrue(hasattr(self.placex, "description"))
        self.assertTrue(hasattr(self.placex, "name"))
        self.assertTrue(hasattr(self.placex, "number_rooms"))
        self.assertTrue(hasattr(self.placex, "number_bathrooms"))
        self.assertTrue(hasattr(self.placex, "max_guest"))
        self.assertTrue(hasattr(self.placex, "price_by_night"))
        self.assertTrue(hasattr(self.placex, "latitude"))
        self.assertTrue(hasattr(self.placex, "longitude"))
        self.assertTrue(hasattr(self.placex, "amenity_ids"))
        self.assertTrue(hasattr(self.placex, "id"))
        self.assertTrue(hasattr(self.placex, "created_at"))
        self.assertTrue(hasattr(self.placex, "updated_at"))

    def test_types(self):
        """Test for Instances"""
        self.assertIsInstance(self.placex.city_id, str)
        self.assertIsInstance(self.placex.user_id, str)
        self.assertIsInstance(self.placex.description, str)
        self.assertIsInstance(self.placex.number_rooms, int)
        self.assertIsInstance(self.placex.max_guest, int)
        self.assertIsInstance(self.placex.price_by_night, int)
        self.assertIsInstance(self.placex.latitude, float)
        self.assertIsInstance(self.placex.longitude, float)
        self.assertIsInstance(self.placex.amenity_ids, str)
        self.assertIsInstance(self.placex.name, str)
        self.assertIsInstance(self.placex.id, str)
        self.assertIsInstance(self.placex.created_at, datetime.datetime)
        self.assertIsInstance(self.placex.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
