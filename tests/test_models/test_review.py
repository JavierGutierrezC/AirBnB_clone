#!/usr/bin/python3
"""
Unittests for review
"""
from models.review import Review
import datetime
import unittest


class ReviewCase(unittest.TestCase):
    """Tests for methods and instances of Review"""
    reviewx = Review()

    def test_hasattr(self):
        """Test for attributes"""
        self.assertTrue(hasattr(self.reviewx, "place_id"))
        self.assertTrue(hasattr(self.reviewx, "user_id"))
        self.assertTrue(hasattr(self.reviewx, "text"))
        self.assertTrue(hasattr(self.reviewx, "id"))
        self.assertTrue(hasattr(self.reviewx, "created_at"))
        self.assertTrue(hasattr(self.reviewx, "updated_at"))

    def test_types(self):
        """Tests for instances"""
        self.assertIsInstance(self.reviewx.place_id, str)
        self.assertIsInstance(self.reviewx.user_id, str)
        self.assertIsInstance(self.reviewx.text, str)
        self.assertIsInstance(self.reviewx.id, str)
        self.assertIsInstance(self.reviewx.created_at, datetime.datetime)
        self.assertIsInstance(self.reviewx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
