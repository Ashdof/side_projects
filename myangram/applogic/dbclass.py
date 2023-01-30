""" =======================     MY ANAGRAM GAME APPLICATION     ===================================
    FILE:           GAME DATABASE CLASS
    DATE:           04-Nov-2022
    LAST UPDATED:   30-JAN-2023
    DEVELOPER:      EMMANUEL ENCHILL

    DESCRIPTION:    THIS MODULE HAS METHODS TO CONNECT TO THE DATABASE AND PERFORM CRUD ACTIONS ON IT. IT ACTS
                    AS THE GLUE BETWEEN THE DATABASE FILE AND GAME LOGIC MODULE THAT INTERACTS WITH THE USER.
"""

#!/usr/bin/env python3

import sqlite3
from texttable import Texttable

class GamedbManager:

    def __init__(self, db_path):
        """Initialise the class with the path to the database file
        
        Arguments:
            db_path (string):  path to the database file

        """
        self._db_path = db_path
  

    def db_connection(self):
        """Database Connection
        
        Description:
            Create a connection to the database

        Returns:
            A connection to the database 
        """
        try:
            conn = sqlite3.connect(self._db_path)
            return conn
        except sqlite3.Error as e:
            print("Failed to connect: ", e)


    def create_table(self):
        """Create Table in database file
        
        Descriotn:
            Create a table in the database file

        """
        try:
            conn = self.db_connection()
            query = '''CREATE TABLE IF NOT EXISTS gamerecords(
                id INTEGER NOT NULL,
                curdate TEXT NOT NULL,
                rounds INTEGER NOT NULL,
                score NUMBER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            ); '''
            
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print("Table creation sucessful.")

            cursor.close()

        except sqlite3.Error as e:
            print("Failed to create table: ", e)

        finally:
            if conn:
                conn.close()
    

    def save_record(self, _date, _rounds, _score):
        """Save Record

        Description:
            Commit the records to the database

        Arguments:
            _date (date): the date for the game play
            _rounds (int): an integer value that represents the game stage
            _score (int): an integer value that represents the score of the game

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO gamerecords (curdate, rounds, score) VALUES (?, ?, ?)"
            data_tuple = (_date, _rounds, _score)
            cursor.execute(query, data_tuple)

            conn.commit()
            cursor.close()

            print("Record saved!")

        except sqlite3.Error as e:
            print("Failed to save record: ", e)

        finally:
            if conn:
                conn.close()
    

    def display_detail_records(self):
        """Display Records
        
        Description:
            Display all information in the specified table

        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM gamerecords"
            cursor.execute(query)
            records = cursor.fetchall()

            table = Texttable()
            table.header(["Game Number", "Date", "Game Stage", "Total Score"])
            table.set_cols_dtype(['t', 't', 't', 't'])

            for record in records:
                table.add_row([record[0], record[1], record[2], record[3]])

            print("\n", table.draw())
            print("\nNumber of records found: ", self.get_number_of_records())

            cursor.close()
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                conn.close()
    

    def get_number_of_records(self):
        """Number of records
        
        Description:
            Get the number of records in the table
        
        Returns:
            The number of records
            
        """
        try:
            conn = self.db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM gamerecords"
            cursor.execute(query)
            records = cursor.fetchall()

            total = len(records)

            cursor.close()
            return total
            
        except sqlite3.Error as e:
            print("Failed to fetch records: ", e)
        finally:
            if conn:
                conn.close()