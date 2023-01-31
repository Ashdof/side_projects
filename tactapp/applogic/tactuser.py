"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER DIRECT MODULE
    DATE CREATED:           31-JAN-2023
    LAST UPDATED:           31-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE PROVIDES METHODS FOR HANDLING THE INFORMATION OF 
                            THE USER'S CONTACTS
"""

#!/usr/bin/env python3

from applogic.dbmanager import TactdbManager

newpath="applogic/dbase/tactdbase.db"
record = TactdbManager(dbpath=newpath)

class TactUserDirect:
    """Module to provide capabilities for managing the information of the user's contacts"""

    def __init__(self, uniquecode="", lastname="", firstname="", prof="", email="", phone=""):
        """Initialise module

        Description:
            This method initialises the module with defauly values
        
        Args:
            uniquecode (str): a unique code identifying this contact person
            lastname (str): the last name of this contact person
            firstname (str): the first name of this contact person
            prof (str): the profession of this contact person
            email (str): the email address of this contact person
            phone (str): the phone number of this contact person
        """

        self.__uniquecode = uniquecode
        self.__lastname = lastname
        self.__firstname = firstname
        self.__prof = prof
        self.__email = email
        self.__phone = phone
    
    @property
    def uniquecode(self):
        """Unique code
        
        Description:
            This method obtains the unique code associated with this contact information. It
            can accessed by invoking the function through a dot-notation scheme without the
            parenthesis. Example:

            variable = tactuser_variable.uniquecode
        
        Returns:
            Unique code of this contact
        """

        return self.__uniquecode
    
    @uniquecode.setter
    def uniquecode(self, new_code):
        """Update unique code
        
        Description:
            This method updates the unique code of this contact information. 
        
        Args:
            new_code (str): the new code to update the unique code with. It can be set
            by assigning to a dot notation. Example:

            variable.uniquecode = <new_code>

            The new_code value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if new_code value is not a string

        """

        if not isinstance(new_code, str):
            raise TypeError("\t'{}' must be a string")
        else:
            self.__uniquecode = new_code
    
    