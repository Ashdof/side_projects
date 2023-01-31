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