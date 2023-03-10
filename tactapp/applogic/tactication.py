"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION MODULE
    DATE CREATED:           25-JAN-2023
    LAST UPDATED:           04-FEB-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE PROVIDES USER AUTHENTICATION METHODS
"""

#!/usr/bin/env python3

import uuid
import datetime

from applogic.tactroot import TactRoot
from applogic.dbmanager import TactdbManager

newpath = "applogic/dbase/tactdbase.db"
db = TactdbManager()
db.dbpath = newpath


class Tactication(TactRoot):
    """User authentication module"""

    def __init__(self, firstname="", username="", password="", id=None):
        """Initialise module

        Description:
            This method initialises the module with the assigned values. The
            parameters can be omitted upon invocation

        Args:
            firstname (str): the first name of this user 
            username (str): username of this user
            password (str): password of this user
            id (str):       module instance tracker
        """
        self.__firstname = firstname
        self.__username = username
        self.__password = password
        super().__init__(id)

    @property
    def firstname(self):
        """Get first name
        
        Description:
            This method obtains the first name of the user. It is executed by
            invoking the function through a dot-notation scheme without the
            parenthesis. Example:

            variable = authentication_variable.firstname
        
        Returns:
            The firstname of this user
        """

        return self.__firstname
    
    @firstname.setter
    def firstname(self, newname):
        """Update first name

        Description:
            This method sets a new first name for this user. It can be assigned
            a value via the dot-notation. Example

            authentication_variable.firstname = <new_firstname>

            The new_firstname value should rather be in quotes (single or double)
            and not the < and >

        Raises:
            ValueError if a blank value is assigned to the method

        """
        faults = ["_", "-", "\\", "/", "?", "@", "#", "~", "&", "$", "(", ")", "[", "{", "]", "}", "|", "!"]
        if len(newname) < 4:
            raise ValueError("\tUsername must be at least four charaters long.")
        
        else:
            for fault in newname:
                if fault in faults:
                    raise ValueError("'{}' cannot be used in a username.".format(fault))

            self.__firstname = newname

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
        faults = ["_", "-", "\\", "/", "?", "@", "#", "~", "&", "$", "(", ")", "[", "{", "]", "}", "|", "!"]
        if len(newname) < 4:
            raise ValueError("\tUsername must be at least four charaters long.")
        
        else:
            for fault in newname:
                if fault in faults:
                    raise ValueError("'{}' cannot be used in a username.".format(fault))

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
        userid = self.getuuid()
        uname = self.username
        pword = self.password
        fname = self.firstname

        try:
            userreg = db.save_tact_user(regdate=tday, firstname=fname, username=uname, password=pword, ubase=userid)
            if userreg:
                print("\tData saved!")

        except (TypeError, ValueError, AttributeError) as e:
            print("\tError!", e)
    
    def userlogin(self):
        """User login

        Description:
            This method enables a user to log into the application with a username and
            password information.
        """
        try:
            userlog = db.user_login(self.username, self.password)
            if userlog:
                return 1
            else:
                return 0

        except (ValueError, TypeError, AttributeError) as e:
            print("Error!", e)

    def getuuid(self):
        """Generate a UUID

        Description:
            This method generates a UUID4 (universally unique identifier). It computes
            the hexdecimal value, takes slices from the user's supplied username, appends
            the slices to the hexed uuid and returns a string representation of the uuid
        
        Returns:
            A string representation of the computed uuid
        """
        uid = uuid.uuid4().hex
        return str(uid)

        