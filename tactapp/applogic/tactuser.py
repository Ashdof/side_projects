"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER DIRECT MODULE
    DATE CREATED:           31-JAN-2023
    LAST UPDATED:           05-FEB-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE PROVIDES METHODS FOR HANDLING THE INFORMATION OF 
                            THE USER'S CONTACTS
"""

#!/usr/bin/env python3

from applogic.dbmanager import TactdbManager
from applogic.tactication import Tactication

record = TactdbManager(dbpath="applogic/dbase/tactdbase.db")

class TactUserDirect:
    """Module to provide capabilities for managing the information of the user's contacts"""

    def __init__(self, uniquecode="", lastname="", firstname="", prof="", email="", phone_number=""):
        """Initialise module

        Description:
            This method initialises the module with default values
        
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
            can be accessed by invoking the function through a dot-notation scheme without the
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
                            by assignment with the dot notation. Example:

            variable.uniquecode = "new_code"
        
        Raises:
            TypeError if new_code value is not a string
            Value Error if length of new_code variable is zero

        """

        if not isinstance(new_code, str):
            raise TypeError("\t'{}' must be a string".format(new_code))
        elif len(new_code) == 0:
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
        
            variable.lastname = "new_name"
        
        Raises:
            TypeError if type of new_name is not a string
            ValueError if the length of new_name variable is zero
        """

        if not isinstance(new_name, str):
            raise TypeError("'{}' must a string.".format(new_name))
        elif len(new_name) == 0:
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
        
            variable.firstname = "new_name"
        
        Raises:
            TypeError if type of new_name is not a string
            ValueError if the length of new_name variable is zero
        """

        if not isinstance(new_name, str):
            raise TypeError("'{}' must a string".format(new_name))
        elif len(new_name) == 0:
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
        
            variable.profession = "profession"
        
        Raises:
            TypeError if type of profession is not a string
            ValueError if the length of profession variable is zero
        """

        if not isinstance(profession, str):
            raise TypeError("'{}' must a string".format(profession))
        elif len(profession) == 0:
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
        
            variable.email = "email"
        
        Raises:
            TypeError if type of email is not a string
            ValueError if the length of email variable is zero or the '@' value is missing
            or the last four characters are not '.com'
        """

        if not isinstance(email, str):
            raise TypeError("'{}' must a string".format(email))
        elif len(email) == 0:
            raise ValueError("Can't assign email to empty value")
        elif email[-4:] != ".com":
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
        
            variable.phonenumber = "phone_number"
        
        Raises:
            ValueError if the length of phone number variable is zero
        """

        if len(phone_number) == 0:
            raise ValueError("Can't assign phone number to empty value")
        elif len(phone_number) != 10 or len(phone_number) > 10:
            raise ValueError("'{}' is invalid. Please make sure phone number has 10 digits.".format(phone_number))
        else:
            self.__phonenumber = phone_number
      
    def get_record(self):
        """Display Records
        
        Description:
            This method displays various records based on options selected by the user. The
            options are numbered and the user only has to select a number. Example

            1. Detail records
            2. Names and phone numbers
            3. Names and email address

            If user selects 1, a detail record will be displayed in table powered by texttable
        """
        
        done = False

        print("\n\tSelect the number for a corresponding record to display\n")
        print("\t1: Detail record\n\t2: Names and phone numbers\n\t3. Names and profession")
        print("\t4: Names and email addresses\n\t5: Unique codes and names")
        
        while not done:
            qtn = input("\n\tNumber ?>: ")

            if qtn == "":
                print("\tDisplay process cancelled")
                done = True
                
            else:
                match qtn:
                    case "1":
                        record.display_detail_records()
                        done = True
                    case "2":
                        record.display_names_and_numbers()
                        done = True
                    case "3":
                        record.display_names_and_profession()
                        done = True
                    case "4":
                        record.display_names_and_emails()
                        done = True
                    case "5":
                        record.display_names_and_codes()
                        done = True

    def commit_record(self, method=""):
        """Save record
        
        Description:
            This method invokes the save_record method from the dbmanager module and passes data
            to it to be saved in the database.
        """

        #   Inovke method to request for user input
        self.get_userinput()

        try:
            tact_code = self.lastname[:2] + self.firstname[-2:]

            if method == "add":
                tact_id = Tactication().getuuid()
                save = record.save_record(tactid=tact_id, uniquecode=tact_code.upper(), lastname=self.lastname, firstname=self.firstname, prof=self.profession, email=self.email, phone=self.phonenumber)
            
            elif method == "dit":
                tactuid = record.get_ids(self.lastname, self.firstname)
                save = record.edit_record(tactid=tactuid, uniquecode=tact_code.upper(), lastname=self.lastname, firstname=self.firstname, prof=self.profession, email=self.email, phone=self.phonenumber)
                
            else:
                print("\n\tNo method to execute. Exiting!")
                exit(0)
            
            if save == 1:
                print("\t{}\'s data saved.".format(self.lastname))
            else:
                print("\t{}\'s data coult not be saved.".format(self.lastname))

        except (ZeroDivisionError, ValueError, TypeError) as e:
            print("Error! {}".format(e)) 
      
    def get_userinput(self):
        """Get user input

        Description:
            This method, when invoked requests inputs from the user and assign them to the
            initialised class parameters
        """

        done = False
        faults = [" ", "@", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")", "'", "~", "`"]
        emaults = [" ", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")", "'", "~", "`"]

        while not done:
            last_name = input("\n\tLast name: ")
            if last_name in faults:
                print("\t{} is not allowed".format(last_name))
            
            elif last_name == "":
                print("\tNew record entry process cancelled")
                done = True
            
            else:
                first_name = input("\tFirst name: ")
                if first_name in faults:
                    print("\t{} is not allowed".format(first_name))
                
                elif first_name == "":
                    print("\tNew record entry process cancelled")
                    done = True
                
                else:
                    prof = input("\tProfession: ")
                    if self.profession in faults:
                        print("\t{} is not allowed".format(prof))
                    
                    elif prof == "":
                        print("\tNew record entry process cancelled")
                        done = True

                    else:
                        mail = input("\tEmail address: ")
                        if mail in emaults:
                            print("\t{} is not allowed".format(mail))
                    
                        elif mail == "":
                            print("\tNew record entry process cancelled")
                            done = True
                        
                        else:
                            phone = input("\tPhone number: ")
                            if phone in faults:
                                print("\t{} is not allowed".format(phone))
                            
                            elif phone == "":
                                print("\tNew record entry process cancelled")
                                done = True
                            
                            else:
                                self.lastname = last_name
                                self.firstname = first_name
                                self.profession = prof
                                self.email = mail
                                self.phonenumber = phone

                                break
