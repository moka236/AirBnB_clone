#!/usr/bin/python3
""" the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
        state_id (string): The state id.
        name (string): The name of the city.
    """

    state_id = ""
    name = ""
