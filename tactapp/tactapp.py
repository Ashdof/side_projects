"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION CLASS
    DATE CREATED:           25-JAN-2023
    LAST UPDATED:           30-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE IMPORVED VERSION OF THE MYPRONETWORK APPLICATION

    CLASS DESCRIPTION:      THIS CLASS PROVIDES USER AUTHENTICATION
"""

#!/usr/bin/env python3
from getpass import getpass

from applogic.tactication import Tactication
from applogic.tacthome import TactAppHome

app = TactAppHome()

class UserSecure:
    """User Authentication CLass"""

    def __init__(self):
        """Initialise class"""

        pass
    
    def usersignin(self):
        """User Login
        
        Description:
            This method enables the user to sign in to the application with his username
            and passowrd
        """
        done = False

        print("\tLogin or type 'su' to signup\n\t_____________________________")

        while not done:

            username = input("\tUsername: ")
            if username == "":
                print("\t[X] User signin cancelled.")
                done = True
                break

            elif username == " ":
                print("\tUsername cannot be blank!\n")
            
            if username == "su":
                self.usersignup()
            
            else:
                password = getpass("\tPassword: ")

                if password == "":
                    print("\t[X] User signin cancelled.")
                    done = True
                    break

                elif password == " ":
                    print("\tPassword cannot be blank!\n")

                else:
                    log = Tactication(username=username, password=password)
                    log.userlogin()
                    if log == 1:
                        print("\tWelcome {}".format(username))
                        app.main(username=username)
                    else:
                        print("\tLogin failed. {}'s information was not found\n".format(username))

    def usersignup(self):
        """User registration

        Description:
            This method registers a new user for the application
        """
        done = False

        print("\n\tSign up to proceed\n\t_____________________________")

        while not done:
            firstname = input("\tFirst name: ")

            if firstname == " ":
                print("\tFirst name cannot be blank!\n")
            
            elif firstname == "":
                print("\t[X] User registration cancelled.")
                done = True
                break
            else:
                username = input("\tUsername: ")

                if username == "":
                    print("\t[X] User registration cancelled.")
                    done = True
                    break

                elif username == " ":
                    print("\tUsername cannot be blank!\n")

                elif len(username) < 4:
                    print("\tUsername must be at least 4 charaters long.")

                else:
                    password = getpass("\tPassword: ")

                    if password == "":
                        print("\t[X] User registration cancelled.")
                        done = True
                        break

                    elif password == " ":
                        print("\tPassword cannot be blank!\n")
                    
                    elif len(password) < 6:
                        print("\tPassword must be at least 6 characters long")

                    else:
                        password_2 = getpass("\tConfirm Password: ")

                        if password_2 == "":
                            print("\t[X] User registration cancelled.")
                            done = True
                            break

                        elif password_2 != password:
                            print("\tPasswords do not match!\n")

                        else:
                            try:
                                reguser = Tactication(firstname=firstname, username=username, password=password_2)
                                reguser.signup()

                                if reguser:
                                    print("\n\tRegistration successful, now sign in\n\t______________________________")
                                    break

                            except (TypeError, ValueError, AttributeError) as e:
                                print("\tError!", e)

#   ==============================================================================

if __name__ == '__main__':

    user = UserSecure()
    user.usersignin()