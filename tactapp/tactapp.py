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

appname = "TactApp Application"
pro_info = "Keep track of your professional network"
pro_info_1 = "This application is powered by commands. Use the following to \n\tperform most common tasks. Use manpro for more."

line_1 = "__________________________________________________________________"

#================================   display on screen  ============================

print("\t\t", appname)
print("\t", pro_info)
print(line_1)
print(pro_info_1)
print("\n")
print("New: add\tEdit: dit\tDelete: del\tDisplay: dis")
print(line_1)

done = False
cmds = ["add", "adds", "dit", "dits", "del", "dels", "dis", "diss", "manpro", "done"]

while not done:
    print("\nWhat do you want to do? ")
    activity = input("?> ")
    
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
            case "manpro":
                ud.UserDirect()._manpro_() 