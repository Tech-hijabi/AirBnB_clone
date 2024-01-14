#!/usr/bin/python3
"""
Shebang Line:
    - Instructs the operating system to execute the script using Python 3.
    - Ensures compatibility with Python 3 syntax and features.

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city with its name and associated state.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state in which the city is located.
    """

    name = ""
    state_id = ""
