#!/usr/bin/python3
"""
Shebang Line:
    - Identifies the Python interpreter to use for executing this script.
    - Ensures compatibility with Python 3 syntax and features.

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place available for accommodation,
    storing its details and location.

    Attributes:
        amenity_ids (str): A comma-separated list of IDs
        of amenities offered at the place.

        city_id (str): The ID of the city where the place is located.
        description (str): A descriptive text about the place's
        features and accommodations.

        name (str): The name of the place.
        user_id (str): The ID of the user who owns or manages the place.
        number_rooms (int): The number of rooms available in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place's location.
        longitude (float): The longitude coordinate of the place's location.
    """

    amenity_ids = ""
    city_id = ""
    description = ""
    name = ""
    user_id = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
