#!/usr/bin/python3
""" Module for the subclass Amenity that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents a specific amenity available in a given context.

    Attributes:
        name (str): The name of the amenity (e.g., "Wi-Fi", "Pool", "Gym").
    """

    name = ""
