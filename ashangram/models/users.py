#!/usr/bin/env python3
"""A module that defines a user/player/gamer"""


class User:
    """A class that models a user of the application"""

    __no_user = 0

    def __init__(self, fullname=None, username=None, password=None):
        """
        Constructor

        Args:
            full_name (str): full name of this object
            username (str): the username of this object
            password (str): the password of this object
        """

        User.__no_user += 1
        self.__fullname = fullname
        self.__username = username
        self.__password = password

    @property
    def fullname(self):
        """Return the full name of this object"""

        return self.__fullname

    @fullname.setter
    def fullname(self, new_name):
        """
        Update the fullname of this object

        Args:
            new_name (str): the new value to set the name

        Raises:
            TypeError if type of new_name is not a string
        """

        if not isinstance(new_name, str):
            raise TypeError(f"{new_name} must be a string")

        self.__fullname = new_name

    @property
    def username(self):
        """Return the username of this object"""

        return self.__username

    @username.setter
    def username(self, new_name):
        """
        Update the username of this object

        Args:
            new_name (str): the new value to set the username

        Raises:
            TypeError if type of new_name is not a string
        """

        if not isinstance(new_name, str):
            raise TypeError(f"{new_name} must be a string")

        self.__username = new_name

    @property
    def password(self):
        """Return the password of this object"""

        return self.__password

    @password.setter
    def password(self, new_password):
        """
        Update the password of this object

        Args:
            new_password (str): the new value to set the password

        Raises:
            ValueError if length of new_password is less than 6 characters
        """

        msg = f"{new_password} must be at least 6 characters long"

        if len(new_password) < 6:
            raise ValueError(msg)

        self.__password = new_password

    def __str__(self):
        """Return the unofficial string representation of this object"""

        return f"Name: {self.__fullname}\nUsername: {self.__username}"

    def number_of_gamers(self):
        """Return the number of gamers"""

        return self.__no_user
