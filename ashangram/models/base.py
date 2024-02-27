"""
This file contains the base class from which other models inherit
"""

import sqlite3


class Base:
    """
    Base Model

    Description:
        This model defines methods that perform tasks common to the other
        models defined in the application
    """

    __app_path = "engine/wordpower.db"

    def __init__(self):
        """
        Constructor

        Description:
            This method initializes the base model
        """

        if self.db_connection(self.__app_path):
            print("Connection established")
    
    def db_connection(self, db_path):
        """Create a connection to the database"""
        
        try:
            conn = sqlite3.connect(db_path)

            return conn
        except sqlite3.Error as e:
            print(f"Error: {e}")