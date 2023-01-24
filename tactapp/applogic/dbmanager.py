"""
    =======================     TACT DATABASE MANAGER     ===================================
    FILE:                   DATABASE ACCESS CLASS
    DATE:                   24-JAN-2023
    LAST UPDATED:           24-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS CLASS FILE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                            AS THE GLUE BETWEEN THE DATABASE FILE AND FRONTEND CLASS THAT INTERACTS WITH THE USER.
"""

#!/usr/bin/python3

import sqlite3

class TactdbManager:
    """Database management module"""

    def __init__(self, dbpath):
        """Initialise path to the database file"""

        self.__dbpath = dbpath
    
    @property
    def dbpath(self):
        """Get Path
        
        Description:
            This method obtains the path to the database file
        
        Returns:
            Path to the database file
        """

        return self.__dbpath
    
    @dbpath.setter
    def dbpath(self, newpath):
        """Locate new database file
        
        Description:
            This method updates the path to the database file

        Args:
            _new_path (str): path to the new database file
        """

        if not isinstance(newpath, str):
            raise TypeError("{} must be a string of characters".format(newpath))
        
        elif newpath == " ":
            raise ValueError("{} is blank and not allowed")
        
        else:
            self.__dbpath = newpath
    
    def dbconnection(self):
        """Database connection
        
        Description:
            This method creates a connection to the database file
        
        Returns:
            A connection string to the database file
        """

        try:
            con = sqlite3.connect(self.dbpath)
            return con
        except sqlite3.Error as e:
            print("Failed to connect to database, ", e)