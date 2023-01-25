"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION MODULE
    DATE CREATED:           25-JAN-2023
    LAST UPDATED:           25-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE PROVIDES USER AUTHENTICATION METHODS
"""

#!/usr/bin/python3

from applogic.tactroot import TactRoot

class Tactication(TactRoot):
    """User authentication module"""

    def __init__(self, username="", password="", id=None):
        """Initialise module

        Description:
            This method initialises the module with the assigned values. The
            parameters can be omitted upon invocation

        Args:
            username (str): username of this user and the first parameter
            password (str): password of this user and the second parameter
            id (str):       module instance tracker
        """
        self.__username = username
        self.__password = password
        super().__init__(id)

    @property
    def username(self):
        """Get username

        Description:
            This method obtains the username of the user. It is executed by
            invoking the function through a dot-notation scheme without the
            parenthesis. Example:

            variable = authentication_variable.username

        Returns:
            The username of this user
        """

        return self.__username

    @username.setter
    def username(self, newname):
        """Update username

        Description:
            This method sets a new username for this user. It can be assigned
            a value via the dot-notation. Example

            authentication_variable.username = <new_username>

            The new_username value should rather be in quotes (single or double)
            and not the < and >

        Raises:
            ValueError if a blank value is assigned to the method

        """

        if newname == " ":
            raise ValueError("'{}' cannot be used as a username".format(newname))

        elif len(newname) < 3:
            raise ValueError("Username should be at least three charaters long.")

        else:
            self.__username = newname

    @property
    def password(self):
        """Get password

        Description:
            This method obtains the password of this user. It is executed by
            invoking the function through a dot-notation scheme without the
            parenthesis. Example:

            variable = authentication_variable.password

        Returns:
            Password of this user
        """

        return self.__password

    @password.setter
    def password(self, newpass):
        """Update password

        Description:
            This method updates the password of this user. It is executed by
            invoking the function through a dot-notation scheme without the
            parenthesis. Example:

            password_variable.password = <new_password>

            The new_password value should rather be in quotes (single or double)
            and not the < and >

        Args:
            newpass (str): the new value to set the password

        Raises:
            ValueError if the length of the new password is less than 6 characters
        """

        if len(newpass) < 6:
            raise ValueError("Password must be at least 6 characters long")

        else:
            self.__password = newpass