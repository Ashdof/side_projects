#!/usr/bin/python3

from models.base import Base

if __name__ == "__main__":

    b = Base()
    print(f"Path to file: {b.db_connection}")
