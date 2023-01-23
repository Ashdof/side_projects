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

    appname = "TactApp Application"
    tag_1 = "Keep track of your professional network"
    tag_2 = "Use the following to perform most common tasks.\n\tType mantact for more"
    line = "\t_______________________________________"

    print("\t\t", appname, "\n\t\t______________________")
    print("\tLogin to proceed or type 'su' to sign up")
    print()
    username = input("\tUsername: ")
    password = input("\tPassword: ")