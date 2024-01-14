#!/usr/bin/python3
"""
Shebang Line:
    - Identifies the Python interpreter to use for executing this script.
    - Ensures compatibility with Python 3 syntax and features.

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user within the application, storing their
    personal information and credentials.

    Attributes:
        email (str): The user's email address, used for
        identification and communication.
        password (str): The user's password, securely stored
        for authentication purposes.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
