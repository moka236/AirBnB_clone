#!/usr/bin/python3
""" the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

        name (string): The name of the amenity.
    """

    name = ""
