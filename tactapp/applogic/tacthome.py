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

from applogic.tactuser import TactUserDirect

class TactAppHome:

    def __init__(self):
        """Initialise this module"""

        pass

    def title(self, username):
        """Application description

        Description:
            This method provides the applications name and header information
        """

        print("\t\t\tTactApp Application")
        print(f"\t\tManage {username}'s Professional Contacts")
        print("\tThis application is powered by commands. Use the following to")
        print("\tperform most common tasks. Use tactman for more.")
        print("\t______________________________________________________________")
    
    def main(self, username):
        """Main Method
        
        Description:
            This is the main method of the module. All other methods are access
            from here
        """
        user = TactUserDirect()

        print()
        self.title(username=username)
        print("\tNew: add\tEdit: dit\tDelete: del\tDisplay: dis")
        print("\t\t__________________________________________")

        done = False
        cmds = ["add", "dit", "del", "ds", "tactman", "done"]

        while not done:
            print()
            print("\tWhat do you want to do? ")
            activity = input("\t?> ")
            
            if activity not in cmds:
                print("\tCommand not found")

            elif activity == "done":
                print("\n\tAPPLICATION EXIT")
                done = True
                exit(0)
            
            else:
                match activity:
                    case "add":
                        user.commit_record("add")
                    case "ds":
                        user.get_record()