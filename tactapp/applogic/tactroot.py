"""
    =======================     TACT DATABASE MANAGER     ===================================
    FILE:                   ROOT MODULE
    DATE CREATED:           24-JAN-2023
    LAST UPDATED:           25-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS MODULE IS THE ROOT OF THE APPLICATION. IT IS RESPONSIBLE FOR:
                            1. DATABASE ID MANAGEMENT
                            2. EXPORT AND IMPORT OF DATABASE
"""

#!/usr/bin/python3


import sqlite3

class TactRoot:
    """Base module
    
    Description:
    """

    _dbobjs = 0

    def __init__(self, id=None):
        """Initialise the module"""

        if id == None:
            self.id = id
        else:
            type(self)._dbobjs += 1
            self.id = self._dbobjs
