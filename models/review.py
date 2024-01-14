#!/usr/bin/python3
"""
Shebang Line:
    - Identifies the Python interpreter to use for executing this script.
    - Ensures compatibility with Python 3 syntax and features.

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review written by a user about a specific place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review,
        containing the user's feedback and opinions.
    """

    place_id = ""
    user_id = ""
    text = ""
