#!/usr/bin/python3
"""
Shebang Line:
    - Identifies the Python interpreter to use for executing this script.
    - Ensures compatibility with Python 3 syntax and features.

"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state within a country.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
