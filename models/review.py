#!/usr/bin/python3
""" the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

        place_id (string): The Place id.
        user_id (string): The User id.
        text (string): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
