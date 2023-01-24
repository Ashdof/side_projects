"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION CLASS
    DATE:                   23-JAN-2023
    LAST UPDATED:           23-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE IMPORVED VERSION OF THE MYPRONETWORK APPLICATION

    CLASS DESCRIPTION:      THIS CLASS PROVIDES USER AUTHENTICATION
"""

#!/usr/bin/python3

import resource.apphome as tact

class UserSecure:
    """User Authentication CLass"""

    def __init__(self):
        """Initialise class"""

        pass
    
    def user_login(self):
        """User Login
        
        Description:
            This method enables the user to sign in to the application with his username
            and passowrd
        """


#   ==============================================================================

if __name__ == '__main__':
    print("\tLogin or type 'su' to signup\n\t_____________________________")
    username = input("\tUsername: ")
    password = input("\tPassword: ")

    if password:
        tact.main()