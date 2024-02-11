#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pla))
        self.assertNotIn("city_id", pla.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pla))
        self.assertNotIn("user_id", pla.__dict__)

    def test_name_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pla))
        self.assertNotIn("name", pla.__dict__)

    def test_description_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pla))
        self.assertNotIn("desctiption", pla.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pla))
        self.assertNotIn("number_rooms", pla.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pla))
        self.assertNotIn("number_bathrooms", pla.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pla))
        self.assertNotIn("max_guest", pla.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pla))
        self.assertNotIn("price_by_night", pla.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pla))
        self.assertNotIn("latitude", pla.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pla))
        self.assertNotIn("longitude", pla.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pla = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pla))
        self.assertNotIn("amenity_ids", pla.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pla = Place()
        pla.id = "123456"
        pla.created_at = pla.updated_at = dt
        plstr = pla.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pla = Place(None)
        self.assertNotIn(None, pla.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pla = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pla.id, "345")
        self.assertEqual(pla.created_at, dt)
        self.assertEqual(pla.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        pla = Place()
        sleep(0.05)
        first_updated_at = pla.updated_at
        pla.save()
        self.assertLess(first_updated_at, pla.updated_at)

    def test_two_saves(self):
        pla = Place()
        sleep(0.05)
        first_updated_at = pla.updated_at
        pla.save()
        second_updated_at = pla.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pla.save()
        self.assertLess(second_updated_at, pla.updated_at)

    def test_save_with_arg(self):
        pla = Place()
        with self.assertRaises(TypeError):
            pla.save(None)

    def test_save_updates_file(self):
        pla = Place()
        pla.save()
        plid = "Place." + pla.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        pla = Place()
        self.assertIn("id", pla.to_dict())
        self.assertIn("created_at", pla.to_dict())
        self.assertIn("updated_at", pla.to_dict())
        self.assertIn("__class__", pla.to_dict())

    def test_to_dict_contains_added_attributes(self):
        pla = Place()
        pla.middle_name = "Holberton"
        pla.my_number = 98
        self.assertEqual("Holberton", pla.middle_name)
        self.assertIn("my_number", pla.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        pla = Place()
        pl_dict = pla.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        pla = Place()
        pla.id = "123456"
        pla.created_at = pla.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pla.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        pla = Place()
        self.assertNotEqual(pla.to_dict(), pla.__dict__)

    def test_to_dict_with_arg(self):
        pla = Place()
        with self.assertRaises(TypeError):
            pla.to_dict(None)


if __name__ == "__main__":
    unittest.main()
