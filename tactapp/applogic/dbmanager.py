"""
    =======================     TACT DATABASE MANAGER     ===================================
    FILE:                   DATABASE ACCESS CLASS
    DATE CREATED:           24-JAN-2023
    LAST UPDATED:           04-FEB-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                            AS THE GLUE BETWEEN THE DATABASE FILE AND FRONTEND CLASS THAT INTERACTS WITH THE USER. IT ALSO
                            INHERITS FROM THE ROOT MODULE AND ITS PROPERTIES
"""

#!/usr/bin/env python3

import sqlite3
from applogic.tactroot import TactRoot
from texttable import Texttable

class TactdbManager(TactRoot):
    """Database management module"""

    def __init__(self, dbpath="", id=None):
        """Initialise module
        
        Description:
            This method initialises the module by setting the path to the
            database file and the id if it is provided
        
        Args:
            id (int): an integer value that tracks the number of database
            instances created.

            dbpath (str): absolute path to the database file
        """

        self.__dbpath = dbpath
        super().__init__(id)
    
    @property
    def dbpath(self):
        """Get Path
        
        Description:
            This method obtains the path to the database file. It executed by
            invoking the function through a dot-notation scheme without the
            parenthesis
        
        Returns:
            Path to the database file
        """

        return self.__dbpath
    
    @dbpath.setter
    def dbpath(self, newpath):
        """Locate new database file
        
        Description:
            This method updates the path to the database file by assigning a
            custom path to the module. It can be assigned a new path via a dot
            notation: eg. db_variable.dbpath = </path/to/file>. The path is
            string in either single or double quotes

        Args:
            _new_path (str): path to the new database file
        
        Raises:
            TypeError if invalide type, such as int, float etc is assigned
            ValueError if of the elements in the list of faults is assigned
        """

        faults = ["", " ", "@", "#", "-", "?", ">", "<", "}", "{", "|", "\\", "%"]

        if not isinstance(newpath, str):
            raise TypeError("{} must be a string of characters".format(newpath))
        
        else:
            for fault in newpath:
                if fault in faults:
                    raise ValueError("{} is present in path name and it\'s not allowed".format(fault))
        
        self.__dbpath = newpath
    
    def dbconnection(self):
        """Database connection
        
        Description:
            This method creates a connection to the database file by invoking the
            property method for the path to the database file. If the database file
            does not exists, it first creates the database, creates a connection to
            it and returns the connection string which can be used to connect execution
            transactions on the database
        
        Returns:
            A connection string to the database
        """
        try:
            conn = sqlite3.connect(self.__dbpath)
            return conn

        except sqlite3.Error as e:
            print("\tFailed to connect to database: ", e)
    
    def save_tact_user(self, regdate, firstname, username, password, ubase):
        """Save new user record

        Description:
            This method commits the record of a newly registered user into a precreated
            table purposefully for storing user information. 

        Args:
            regdate (datetime): the date of registration of the user
            username (str): the username of the user
            password (str): a string of at least 6 characters used as password by the user
            ubase (str): a string of uuid which serve the user's purpose
        """

        try:
            conn = self.dbconnection()
            cursor = conn.cursor()

            query = "INSERT INTO tacters (regdate, firstname, username, password, tacterid)\
                VALUES (?, ?, ?, ?, ?)"
            queryple = (regdate, firstname, username, password, ubase)
            cursor.execute(query, queryple)
            conn.commit()

            if conn:
                return 0

        except sqlite3.Error as e:
            print("\tError!", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def user_login(self, username, password):
        """User login

        Description:
            This method enables a user to log into the application by supplying a username and a
            password.

        Args:
            username (str): the username of this user
            password (str): the password of this user

        Returns:
            1 if both username and password exist in the database
            0 if either username or password does not exist in the database
        """

        try:
            conn = self.dbconnection()
            cursor = conn.cursor()

            query = "SELECT username, password FROM tacters WHERE username = ? AND password = ? "
            querytuple = (username, password)
            cursor.execute(query, querytuple)
            rs = cursor.fetchall()

            return rs

        except sqlite3.Error as e:
            print("\tError!", e)
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def verify_user(self, username):
        """Verify user

        Description:
            This method is used to verify the availability of the username supplied
            by the user. When the user provides the username during signup, the system
            quickly checks the database to ascertain the name does not already exist.
            If it does, it notifies user by repeating the request for new username along
            with a message, stating the reason.
        
        Args:
            username (str): the username of this user
        """

        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            find_user = ("SELECT * FROM tacters WHERE username = ?")
            cursor.execute(find_user, [(username)])
            rs = cursor.fetchall()
            return rs

        except sqlite3.Error as e:
            print("Error!", e)
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def save_record(self, tactid, uniquecode, lastname, firstname, prof, email, phone):
        """Save record
        
        Description:
            This method commits the record of a contact to the database
        
        Args:
            uniquecode (str): the unique code of this contact
            lastname (str): the lastname of this contact
            firstname (str): the firstname of this contact
            prof (str): the profession of this contact
            email (str): the email address of this contact
            phone (str): the phone number of this contact
        
        Returns:
            1 if data is saved successfully
            0 if it fails
        """

        try:
            conn = self.dbconnection()
            cursor = conn.cursor()

            query = "INSERT INTO tactlist (tactid, uniquecode, lastname, firstname, profession, email, phone)\
                VALUES (?, ?, ?, ?, ?, ?, ?)"
            querytuple = (tactid, uniquecode, lastname, firstname, prof, email, phone)
            cursor.execute(query,querytuple)

            conn.commit()
            if conn:
                return 1
            else:
                return 0
        
        except sqlite3.Error as e:
            print("Error! {}".format(e))
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def edit_record(self, tactid, uniquecode, lastname, firstname, prof, email, phone):
        """Update record
        
        Description:
            This method updates the record of a contact
        
        Args:
            uniquecode (str): the unique code of this contact
            lastname (str): the lastname of this contact
            firstname (str): the firstname of this contact
            prof (str): the profession of this contact
            email (str): the email address of this contact
            phone (str): the phone number of this contact
        
        Returns:
            1 if data is updated successfully
            0 if it fails
        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()

            query = "UPDATE myprocons SET uniquecode = ?, lastname = ?, firstname = ?, profession = ?, email = ?, phone = ? WHERE tactid = ? "
            data = (tactid, uniquecode, lastname, firstname, prof, email, phone)

            cursor.execute(query, data)
            conn.commit()
            
            qty = conn.total_changes
            if qty == 0:
                return 1
            else:
                return 0
            
        except sqlite3.Error as e:
            print("\tFailed to update record: {}".format(e))

        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def delete_record(self, uid):
        """Delete record

        Description:
            This method deletes a record of the id passed as parameter
        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "DELETE FROM tactlist WHERE tactid = ?"
           
            cursor.execute(query, (uid,))
            conn.commit()
            
            qty = conn.total_changes
            if qty == 0:
                return (1)
            else:
                return (0)

        except sqlite3.Error as e:
            print("\tFailed to delete record: ", e)
            
        finally:
            if conn:
                cursor.close()
                conn.close()

    def display_detail_records(self):
        """Display detail records
        
        Description:
            This method fetches and display all records in the specified table

        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT * FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Unique Code", "Last name", "First name", "Profession", "Email", "Phone number"])
            table.set_cols_dtype(['t', 't', 't', 't', 't', 't'])

            for record in records:
                table.add_row([record[1], record[2], record[3], record[4], record[5], record[6]])

            print()
            print(table.draw())
            print("\n\tNumber of records found: ", self.get_number_of_records())

        except sqlite3.Error as e:
            print("\tError: {}".format(e))

        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def display_names_and_numbers(self):
        """Display names and phone numbers

        Description:
            This method fetches firstname, lastname and phone numbers from the database

        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, phone FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Phone number"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])

            print()
            print(table.draw())
            print("\n\tNumber of records found: ", self.get_number_of_records())
            
        except sqlite3.Error as e:
            print("\n\tFailed to fetch record: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def display_names_and_profession(self):
        """Display names and profession

        Description:
            This method fetches firstname, lastname and profession from the database

        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, profession FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Profession"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])

            print()
            print(table.draw())
            print("\n\tNumber of records found: ", self.get_number_of_records())
            
        except sqlite3.Error as e:
            print("\n\tFailed to fetch record: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def display_names_and_emails(self):
        """Display names and emails

        Description:
            This method fetches firstname, lastname and email addresses from the database

        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT lastname, firstname, email FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Last name", "First name", "Email address"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])

            print()
            print(table.draw())
            print("\n\tNumber of records found: ", self.get_number_of_records())
            
        except sqlite3.Error as e:
            print("\n\tFailed to fetch record: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def display_names_and_codes(self):
        """Display unique codes and names

        Description:
            This method fetches firstname, lastname and uniquecode from the database

        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT uniquecode, lastname, firstname FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Code", "Last name", "First name"])
            table.set_cols_dtype(['t', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2]])

            print()
            print(table.draw())
            print("\n\tNumber of records found: ", self.get_number_of_records())
            
        except sqlite3.Error as e:
            print("\n\tFailed to fetch record: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def get_number_of_records(self, record=[]):
        """Number of records
        
        Description:
            This method computes for the number of records in the database. If the argument is none,
            it computes for the overall total number of records. If not, it computes for the number of
            records related to the supplied argument
        
        Args:
            record (list): This is a list of values that corresponds to the records to fetch from the
                            database. The first element must be the column label and the second element
                            must be the value to search for. Example

                            record = [lastname, Kay]

                            This instructs the programme to search the lastname column and fetch all records
                            that have 'Kay' as the last name. If either the list is empty or the first element
                            is missing or the second element is mission, it will fetch all records.
        
        Returns:
            Number of records found

        """

        query = ""

        try:
            conn = self.dbconnection()
            cursor = conn.cursor()

            if record == [] or record[0] == "" or record[1] == "":
                query = "SELECT * FROM tactlist"
            else:
                query = "SELECT * FROM tactlist WHERE '"+record[0]+"' = '"+record[1]+"' "

            cursor.execute(query)
            records = cursor.fetchall()

            total = len(records)

            return total
            
        except sqlite3.Error as e:
            print("\tFailed to fetch record: ", e)
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def get_codes(self):
        """Select uniquecodes

        Description:
            This method selectes all unique codes from the database
        """
        try:
            uniq_codes = []

            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT uniquecode FROM tactlist"
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                uniq_codes.append(record)

            return uniq_codes
            
        except sqlite3.Error as e:
            print("\tFailed to fetch records: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
    
    def get_ids(self, lastname, firstname):
        """Select uniquecodes

        Description:
            This method selectes all unique codes from the database
        """
        try:
            conn = self.dbconnection()
            cursor = conn.cursor()
            query = "SELECT tactid FROM tactlist WHERE lastname = '"+lastname+"' AND firstname = '"+firstname+"' "
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                for ids in record:
                    return ids
            
        except sqlite3.Error as e:
            print("\tFailed to fetch records: ", e)

        finally:
            if conn:
                cursor.close()
                conn.close()
