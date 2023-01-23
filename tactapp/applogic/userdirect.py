"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER DIRECT CLASS
    DATE:                   23-JAN-2023
    LAST UPDATED:           23-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS CLASS INTERACTS DIRECTLY WITH THE USER INTERFACE CLASS; IT CONNECTS TO THE DATABASE MANAGER
    CLASS DESCRIPTION:      THIS CLASS PROVIDES THE USER INTERFACE
"""

from applogic import tactdbmanager as ptk

"""Pass the path to the database file to the class being called"""
dbpath = "procons.db"
record = ptk.prodbmanager(db_path=dbpath)

line_1 = "___________________________"

class UserDirect:
    
    def __init__(self, last_name="", first_name="", name_code="", prof="", e_mail="", f_number=""):
        """ Initialise class variables
        
        last_name           Last name of the contact person
        first_name          First name of the contact person
        name_code           Unique code of the contact person
        prof                The profession of the contact person
        e_mail              The email address of the contact person
        f_number            The phone number of the contact person
        """
        self._last_name = last_name
        self._first_name = first_name
        self._name_code = name_code
        self._prof = prof
        self._e_mail = e_mail
        self._f_number = f_number

    def get_last_name(self):
        """Return last name of contact"""
        return self._last_name
    
    def get_first_name(self):
        """Return first name of contact"""
        return self._first_name
    
    def get_name_code(self):
        """Return the code of this contact"""
        return self._name_code.upper()
    
    def get_profession(self):
        """Return the profession of contact"""
        return self._prof
    
    def get_email(self):
        """Return the email address"""
        return self._e_mail
    
    def get_phone_number(self):
        """Return the phone number of contact"""
        return self._f_number

    def _commit_to_database_(self):
        """Pass Records to the save method to be committed
        to the database
        """

        faults = ["", " ", "@", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")"]
        done = False

        while not done:
            name_code = input("\nUnique code: ")

            if name_code in faults:
                print("{} is allowed".format(name_code))
            else:
                last_name = input("Last name: ")
                first_name = input("First name: ")
                prof_sion = input("Profession: ")
                e_mail = input("Email: ")
                phone_num = input("Phone: ")

                record.save_record(_lastname=last_name, _firstname=first_name, _uniquecode=name_code, _profession=prof_sion, _email=e_mail, _phone_number=phone_num)
                
                done = True

                print("Record saved successfully")
                print(line_1)


    def _commit_multi_records(self):
        """Commit Multiple Records
        
        Save multiple records from the standard input until a condition becomes false
        """
        done = False
        faults = [" ", "@", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")", "'"]

        while not done:
            name_code = input("\nUnique code: ")

            if name_code in faults:
                print("{} is allowed".format(name_code))

            elif name_code == "":
                print("New record entry process cancelled")
                done = True

            else:
                last_name = input("Last name: ")
                first_name = input("First name: ")
                prof_sion = input("Profession: ")
                e_mail = input("Email: ")
                phone_num = input("Phone: ")

                record.save_record(_lastname=last_name, _firstname=first_name, _namecode=name_code, _profession=prof_sion, _email=e_mail, _phone_number=phone_num)

        print("Records saved successfully")
        print(line_1)


    def _editrecord_(self):
            """Edit a record

            Invoke the edit record function to update one record at a time 
            """

            done = False
            faults = [" ", "@", "/", "?",";", ":", "#", "%", "&", "!", "$", "^", "*", "(", ")", "'"]
            vals = ['Y', 'y']

            while not done:
                name_code = input("\nUnique code: ")

                if name_code == "":
                    print("Data edit process cancelled")
                    done = True

                elif name_code in faults:
                    print("{} is not allowed".format(name_code))

                else:
                    last_name = input("Last name: ")
                    first_name = input("First name: ")
                    prof_sion = input("Profession: ")
                    e_mail = input("Email: ")
                    phone_num = input("Phone: ")

                    edit_info = record.edit_record(_lastname=last_name, _firstname=first_name, _namecode=name_code, _profession=prof_sion, _email=e_mail, _phone_number=phone_num)
                    if edit_info == 1:
                        print("{}'s record not found".format(name_code))
                        done = True

                    elif edit_info == 0:
                        print("{}'s record updated successfully.".format(name_code)) 
                        done = True


    def _getrecords_(self):
        """Display Records
        
        User is presented with options to choose from
        """
        
        done = False

        print("\nSelect the number for a corresponding record to display\n")
        print("1: Detail Record\n2: Name and Codes\n3: Name, Profession and Phone Numbers\n4: Names and Phone Numbers\n5. Name and Email Addresses ")
        
        while not done:
            val = input("\nNumber ?>: ")

            if val == "":
                print("Display process cancelled")
                done = True
                
            else:
                match val:
                    case "1":
                        record.display_detail_records()
                        done = True

                    case "2":
                        record.display_names_and_codes()
                        done = True

                    case "3":
                        record.display_names_prof_contacts()
                        done = True

                    case "4":
                        record.display_names_and_numbers()
                        done = True

                    case "5":
                        record.display_names_email_addresses()
                        done = True
        

    def _get_multi_records_(self):
        """Display Records
        
        User is presented with options to choose from
        """
        
        done = False

        print("\nSelect the number for a corresponding record to display\n")
        print("1: Detail Record\n2: Name and Codes\n3: Name, Profession and Phone Numbers\n4: Names and Phone Numbers\n5. Name and Email Addresses ")
        
        while not done:
            val = input("\nNumber ?>: ")

            if val == "":
                print("Display process cancelled")
                done = True
                
            else:
                match val:
                    case "1":
                        record.display_detail_records()
                    case "2":
                        record.display_names_and_codes()
                    case "3":
                        record.display_names_prof_contacts()
                    case "4":
                        record.display_names_and_numbers()
                    case "5":
                        record.display_names_email_addresses()


    def _deleterecord_(self):
        """Delet a record at a time
        
        Delete a record by providing the unique code of the record
        """
        done = False

        while not done:
            quest = input("\nUnique code ?> ")

            if quest == "":
                print("Delete process cancelled")
                done = True
            
            else:
                del_info = record.delete_record(quest)

                if del_info == 1:
                    print("{}'s record not found'".format(quest))

                elif del_info == 0:
                    print("{}'s record deleted successfully.".format(quest)) 
                    done = True

    
    def _delete_multiple_records(self):
        """Delete multiple records
        
        Delete records by providing unique codes. Hitting enter key without any data will exit
        """

        done = False

        while not done:
            quest = input("\nUnique code ?> ")

            if quest == "":
                print("Delete process cancelled")
                done = True
            
            else:
                del_info = record.delete_record(quest)

                if del_info == 1:
                    print("{}'s record not found'".format(quest))

                elif del_info == 0:
                    print("{}'s record deleted successfully.".format(quest)) 

    
    def _manpro_(self):
        """Displays the manual when invoked
        
        Read the information from file and display it on the scree
        """
        manpro = open("manpro", "r")

        for line in manpro:
            print(line, end='')
        manpro.close()