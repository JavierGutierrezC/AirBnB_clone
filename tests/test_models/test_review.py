#!/usr/bin/python3
from models.review import Review
import datetime
import unittest
"""Unittests for review"""


class ReviewCase(unittest.TestCase):

    reviewx = Review()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.reviewx, "name"))
        # BaseModel Attributes
        self.assertTrue(hasattr(self.reviewx, "id"))
        self.assertTrue(hasattr(self.reviewx, "created_at"))
        self.assertTrue(hasattr(self.reviewx, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.reviewx.name, str)
        # BaseModel Attributes
        self.assertIsInstance(self.reviewx.id, str)
        self.assertIsInstance(self.reviewx.created_at, datetime.datetime)
        self.assertIsInstance(self.reviewx.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
