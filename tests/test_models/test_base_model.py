#!/usr/bin/python3
"""Unittest for base_model"""

import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        Model = BaseModel()
        self.assertIs(type(Model.id), str)
        self.assertIs(type(Model.created_at), datetime)
        self.assertIs(type(Model.updated_at), datetime)
        self.assertNotEqual(Model.created_at, Model.updated_at)
        self.assertFalse(Model.updated_at == datetime.utcnow())
        old_updated = Model.updated_at
        Model.save()

    def test_save_model(self):
        """ tests to see if the return type of save is a string """
        Model = BaseModel()
        Model.save()
        self.assertIsInstance(Model.to_dict()['created_at'], str)
        self.assertIsInstance(Model.to_dict()['updated_at'], str)
        self.assertNotEqual(old_updated, Model.updated_at)
        Model2 = Model.to_dict()
        self.assertEqual(type(Model2), dict)
        self.assertEqual(Model2['__class__'], "BaseModel")
        self.assertEqual(Model2['created_at'], Model.created_at.isoformat())
        self.assertEqual(Model2['updated_at'], Model.updated_at.isoformat())
        self.assertEqual(Model2['id'], Model.id)

    def test_attributes(self):
        """BaseModel Attributes"""
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

        self.assertTrue(hasattr(self.base, "save"))
        self.assertTrue(hasattr(self.base, "to_dict"))

    def test_string_method(self):
        """Test string method of BadeModel """
        self.base.id = "1234-5678-9012"
        self.assertEqual(str(self.base), self.dict_obj)

    def test_string_repr_method(self):
        """Test Method"""
        self.assertEqual(repr(self.base), self.dict_obj)

    def test_dict_method(self):
        """Test dictionary method of BaseModel"""
        cre_at_iso = self.base.created_at.isoformat()
        upd_at_iso = self.base.updated_at.isoformat()
        datetimes = " '{}', 'updated_at': '{}'".format(cre_at_iso, upd_at_iso)

        self.assertEqual(str(self.base.to_dict()), "{'id': '1234-5678-9012', "
                                                   "'created_at':" +
                         datetimes + ", '_class_': 'BaseModel'}")

if __name__ == '__main__':
    unittest.main()
