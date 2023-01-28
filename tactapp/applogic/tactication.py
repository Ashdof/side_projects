"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION MODULE
    DATE CREATED:           25-JAN-2023
    LAST UPDATED:           28-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE PROVIDES USER AUTHENTICATION METHODS
"""

#!/usr/bin/python3

import uuid
import datetime

from applogic.tactroot import TactRoot
from applogic.dbmanager import TactdbManager

newpath = "applogic/dbase/tactdbase.db"
db = TactdbManager()
db.dbpath = newpath


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
        if len(newname) < 3:
            raise ValueError("\tUsername should be at least three charaters long.")

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
            raise ValueError("\tPassword must be at least 6 characters long")

        else:
            self.__password = newpass
    
    def signup(self):
        """User signup
        
        Description:
            This method is for registration of a new user. To be able to use
            the application, the user will have to register with a username and
            password. This method invokes the user authentication method from the
            database manager module to authenticate the user
        """
        tday = datetime.date.today()
        uid = uuid.uuid4().hex
        userid = "tactuser" + str(uid)
        uname = self.username
        pword = self.password

        try:
            userreg = db.save_tact_user(regdate=tday, username=uname, password=pword, ubase=userid)
            if userreg:
                print("Data saved!")

        except (TypeError, ValueError, AttributeError) as e:
            print("\tError!", e)

    def connect(self):
        try:
            userreg = db.dbconnection()
            if userreg:
                print("\tConnected!")

        except (TypeError, ValueError, AttributeError) as e:
            print("\tError!", e)