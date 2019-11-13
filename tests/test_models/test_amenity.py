#!/usr/bin/python3
"""
Unittest for amenity
"""
from models.amenity import Amenity
import datetime
import unittest


class AmenityCase(unittest.TestCase):
    """Test for methods and instances"""
    amenitix = Amenity()

    def test_hasattr(self):
        """Tets for attributes"""
        self.assertTrue(hasattr(self.amenitix, "name"))

        # BaseModel Attributes
        self.assertTrue(hasattr(self.amenitix, "id"))
        self.assertTrue(hasattr(self.amenitix, "created_at"))
        self.assertTrue(hasattr(self.amenitix, "updated_at"))

    def test_types(self):
        """Tests for Instances"""
        self.assertIsInstance(self.amenitix.name, str)
        
        # BaseModel Attributes
        self.assertIsInstance(self.amenitix.id, str)
        self.assertIsInstance(self.amenitix.created_at, datetime.datetime)
        self.assertIsInstance(self.amenitix.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
