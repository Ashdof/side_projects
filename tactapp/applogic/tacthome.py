"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   MAIN APPLICATION MODULE
    DATE CREATED:           25-JAN-2023
    LAST UPDATED:           30-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    MODULE DESCRIPTION:     THIS MODULE ENABLES THE USER TO INTERACT WITH ALL THE OTHER PARTS
                            OF THE APPLICATION
"""

#!/usr/bin/env python3

class TactAppHome:

    def __init__(self):
        """Initialise this module"""

        pass

    def title(self, username):
        """Application description

        Description:
            This method provides the applications name and header information
        """

        appname = "\tTactApp Application"
        tag_1 = f"\tManage {username}'s Contacts"
        tag_2 = "\tThis application is powered by commands. Use the following to \n\tperform most common tasks. Use tactman for more."

        line = "\t__________________________________________"
    
    def main(self, username):
        """Main Method
        
        Description:
            This is the main method of the module. All other methods are access
            from here
        """

        print()
        self.title(username=username)
        print("\tNew: add\tEdit: dit\tDelete: del\tDisplay: dis")
        print("\t__________________________________________")

        done = False
        cmds = ["add", "adds", "dit", "dits", "del", "dels", "dis", "diss", "manpro", "done"]

        while not done:
            print()
            print("\tWhat do you want to do? ")
            activity = input("\t?> ")
            
            if activity not in cmds:
                print("Command not found")

            elif activity == "done":
                print("\n\tAPPLICATION EXIT")
                done = True
                exit(0)