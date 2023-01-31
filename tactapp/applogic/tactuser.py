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

    def __init__(self, uniquecode="", lastname="", firstname="", prof="", email="", phone_number=""):
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
        self.__phonenumber = phone_number
    
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
            by assigning by a dot notation. Example:

            variable.uniquecode = <new_code>

            The new_code value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if new_code value is not a string
            Value Error if length of new_code variable is zero

        """

        if not isinstance(new_code, str):
            raise TypeError("\t'{}' must be a string".format(new_code))
        elif len(new_code == 0):
            raise ValueError("Can't assign unique code to empty value")
        else:
            self.__uniquecode = new_code
    
    @property
    def lastname(self):
        """Last name

        Description:
            This method obtains the last name of this contact information. It can be
            accessed by using the dot notation. Example:

            variable = tactuser_variable.lastname
        
        Returns:
            The last name of this contact
        """

        return self.__lastname
    
    @lastname.setter
    def lastname(self, new_name):
        """Update last name
        
        Description:
            This method updates the last name of this contact information. It can be
            assigned by a dot notation. Example:
        
            variable.lastname = <new_name>

            The new_code value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if type of last_name is not a string
            ValueError if the length of new_name variable is zero
        """

        if not isinstance(new_name, str):
            raise TypeError("'{}' must a string of characters".format(new_name))
        elif len(new_name == 0):
            raise ValueError("Can't assign last name to empty value")
        else:
            self.__lastname = new_name
    
    @property
    def firstname(self):
        """First name

        Description:
            This method obtains the first name of this contact information. It can be
            accessed by using the dot notation. Example:

            variable = tactuser_variable.firstname
        
        Returns:
            The first name of this contact
        """

        return self.__firstname
    
    @firstname.setter
    def firstname(self, new_name):
        """Update first name
        
        Description:
            This method updates the first name of this contact information. It can be
            assigned by a dot notation. Example:
        
            variable.firstname = <new_name>

            The new_code value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if type of first_name is not a string
            ValueError if the length of new_name variable is zero
        """

        if not isinstance(new_name, str):
            raise TypeError("'{}' must a string of characters".format(new_name))
        elif len(new_name == 0):
            raise ValueError("Can't assign first name to empty value")
        else:
            self.__firstname = new_name
    
    @property
    def profession(self):
        """Profession

        Description:
            This method obtains the profession of this contact information. It can be
            accessed by using the dot notation. Example:

            variable = tactuser_variable.profession
        
        Returns:
            The profession of this contact
        """

        return self.__prof
    
    @profession.setter
    def profession(self, profession):
        """Update profession
        
        Description:
            This method updates the profession of this contact information. It can be
            assigned by a dot notation. Example:
        
            variable.profession = <profession>

            The profession value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if type of profession is not a string
            ValueError if the length of profession variable is zero
        """

        if not isinstance(profession, str):
            raise TypeError("'{}' must a string of characters".format(profession))
        elif len(profession == 0):
            raise ValueError("Can't assign profession to empty value")
        else:
            self.__prof = profession
    
    @property
    def email(self):
        """Email

        Description:
            This method obtains the email of this contact information. It can be
            accessed by using the dot notation. Example:

            variable = tactuser_variable.email
        
        Returns:
            The email of this contact
        """

        return self.__email
    
    @email.setter
    def email(self, email):
        """Update email
        
        Description:
            This method updates the email of this contact information. It can be
            assigned by a dot notation. Example:
        
            variable.email = <email>

            The email value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            TypeError if type of email is not a string
            ValueError if the length of email variable is zero or the '@' value is missing
            or the last four characters are not '.com'
        """

        if not isinstance(email, str):
            raise TypeError("'{}' must a string of characters".format(email))
        elif len(email == 0):
            raise ValueError("Can't assign email to empty value")
        elif email[-4:] is not ".com":
            raise ValueError("'{}' is invalid. Please supply a complete email address with a '.com'".format(email))
        elif "@" not in email:
            raise ValueError("'{}' is missing the '@' character.".format(email))
        else:
            self.__email = email
    
    @property
    def phonenumber(self):
        """Phone

        Description:
            This method obtains the phone number of this contact information. It can be
            accessed by using the dot notation. Example:

            variable = tactuser_variable.phone
        
        Returns:
            The phone number of this contact
        """

        return self.__phonenumber
    
    @phonenumber.setter
    def phonenumber(self, phone_number):
        """Update phone number
        
        Description:
            This method updates the phone number of this contact information. It can be
            assigned by a dot notation. Example:
        
            variable.phonenumber = <phone_number>

            The phone number value should rather be in quotes (single or double)
            and not the < and >
        
        Raises:
            ValueError if the length of phone number variable is zero
        """

        if len(phone_number == 0):
            raise ValueError("Can't assign phone number to empty value")
        else:
            self.__phonenumber = phone_number