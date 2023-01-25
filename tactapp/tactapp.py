"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION CLASS
    DATE CREATED:                   23-JAN-2023
    LAST UPDATED:           25-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE IMPORVED VERSION OF THE MYPRONETWORK APPLICATION

    CLASS DESCRIPTION:      THIS CLASS PROVIDES USER AUTHENTICATION
"""

#!/usr/bin/python3

# import resource.apphome as tact

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
        pass

    def auth(self):
        """User registration
        
        Description:
            This method registers a new user for the application
        """

        print("\n\tSign up to proceed\n\t_____________________________")
        username = input("\tUsername: ")
        password = input("\tPassword: ")
        password_2 = input("\tConfirm password: ")

#   ==============================================================================

if __name__ == '__main__':
    user = UserSecure()

    print("\tLogin or type 'su' to signup\n\t_____________________________")
    username = input("\tUsername: ")
    
    if username == "su":
        user.auth()
    else:
        password = input("\tPassword: ")
        # tact.main()