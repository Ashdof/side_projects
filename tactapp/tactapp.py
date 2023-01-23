"""
    =======================     TACT APPLICATION     ===================================
    FILE:                   USER AUTHENTICATION CLASS
    DATE:                   23-JAN-2023
    LAST UPDATED:           23-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL

    DESCRIPTION:            THIS IS THE IMPORVED VERSION OF THE MYPRONETWORK APPLICATION

    CLASS DESCRIPTION:      THIS CLASS PROVIDES THE USER INTERFACE
"""

from applogic import userdirect as ud

appname = "\tTactApp Application"
tag_1 = "\tKeep track of your professional network"
tag_2 = "\tThis application is powered by commands. Use the following to \n\tperform most common tasks. Use tactman for more."

line = "\t__________________________________________"

#================================   display on screen  ============================



def main():
    print()
    print("\t\t", appname)
    print("\t", tag_1)
    print(line)
    print("\tNew: add\tEdit: dit\tDelete: del\tDisplay: dis")
    print(line)

    done = False
    cmds = ["add", "adds", "dit", "dits", "del", "dels", "dis", "diss", "manpro", "done"]

    while not done:
        print()
        print("\tWhat do you want to do? ")
        activity = input("\t?> ")
        
        if activity not in cmds:
            print("Command not found")

        elif activity == "done":
            print("\nAPPLICATION EXIT")
            done = True
            exit(0)

        else:
            match activity:
                case "add":
                    ud.UserDirect()._commit_to_database_()
                case "adds":
                    ud.UserDirect()._commit_multi_records()
                case "dis":
                    ud.UserDirect()._getrecords_()
                case "diss":
                    ud.UserDirect()._get_multi_records_()
                case "del":
                    ud.UserDirect()._deleterecord_()
                case "dels":
                    ud.UserDirect()._delete_multiple_records()
                case "dit":
                    ud.UserDirect()._editrecord_()
                case "tactman":
                    ud.UserDirect()._manpro_() 