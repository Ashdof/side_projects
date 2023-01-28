"""
    =======================     TACT DATABASE MANAGER     ===================================
    FILE:                   DATABASE ACCESS CLASS
    DATE CREATED:           24-JAN-2023
    LAST UPDATED:           28-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                            AS THE GLUE BETWEEN THE DATABASE FILE AND FRONTEND CLASS THAT INTERACTS WITH THE USER. IT ALSO
                            INHERITS FROM THE ROOT MODULE AND ITS PROPERTIES
"""

#!/usr/bin/python3

import sqlite3
from applogic.tactroot import TactRoot

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
    
    def save_tact_user(self, regdate, username, password, ubase):
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

            query = "INSERT INTO tactusera73fb274976741158f3854f0c1554c0b (date_registered, username, password, userbase)\
                VALUES (?, ?, ?, ?)"
            queryple = (regdate, username, password, ubase)
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