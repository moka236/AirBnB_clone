#!/usr/bin/python3
""" the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

        name (string): The name of the state.
    """

    name = ""
