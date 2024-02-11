#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        cyi = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cyi))
        self.assertNotIn("state_id", cyi.__dict__)

    def test_name_is_public_class_attribute(self):
        cyi = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cyi))
        self.assertNotIn("name", cyi.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cyi = City()
        cyi.id = "123456"
        cyi.created_at = cyi.updated_at = dt
        cystr = cyi.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        cyi = City(None)
        self.assertNotIn(None, cyi.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cyi = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cyi.id, "345")
        self.assertEqual(cyi.created_at, dt)
        self.assertEqual(cyi.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def newName(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def remove(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        cyi = City()
        sleep(0.05)
        first_updated_at = cyi.updated_at
        cyi.save()
        self.assertLess(first_updated_at, cyi.updated_at)

    def test_two_saves(self):
        cyi = City()
        sleep(0.05)
        first_updated_at = cyi.updated_at
        cyi.save()
        second_updated_at = cyi.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cyi.save()
        self.assertLess(second_updated_at, cyi.updated_at)

    def test_save_with_arg(self):
        cyi = City()
        with self.assertRaises(TypeError):
            cyi.save(None)

    def test_save_updates_file(self):
        cyi = City()
        cyi.save()
        cyid = "City." + cyi.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cyi = City()
        self.assertIn("id", cyi.to_dict())
        self.assertIn("created_at", cyi.to_dict())
        self.assertIn("updated_at", cyi.to_dict())
        self.assertIn("__class__", cyi.to_dict())

    def test_to_dict_contains_added_attributes(self):
        cyi = City()
        cyi.middle_name = "Holberton"
        cyi.my_number = 98
        self.assertEqual("Holberton", cyi.middle_name)
        self.assertIn("my_number", cyi.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cyi = City()
        cy_dict = cyi.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        cyi = City()
        cyi.id = "123456"
        cyi.created_at = cyi.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cyi.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cyi = City()
        self.assertNotEqual(cyi.to_dict(), cyi.__dict__)

    def test_to_dict_with_arg(self):
        cyi = City()
        with self.assertRaises(TypeError):
            cyi.to_dict(None)


if __name__ == "__main__":
    unittest.main()
