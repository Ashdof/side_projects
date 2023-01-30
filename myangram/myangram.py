"""
    =======================     MY ANAGRAM GAME APPLICATION     ===================================
    FILE:                   GAME INTERFACE MODULE
    DATE:                   04-NOV-2022
    LAST UPDATED:           30-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS IS A SIMPLE GAME APPLICATION. IT DISPLAYS SHUFFLED WORDS FOR THE USER TO GUESS THE
                            CORRECT SPELLING. IT SAVES GAME RECORDS TO AN SQLite3 DATABASE FILE

    MODULE DESCRIPTION:     THIS MODULE ACTS AS THE FRONTEND OF THE APPLICATION. IT INTERACTS WITH THE USER THROUGH
                            SIMPLE COMMANDS.
"""

#!/usr/bin/env python3

from applogic.dbclass import GamedbManager
from applogic.gamelogic import Anagram

gamewords = 'applogic/game_words'
dbfile = 'applogic/gamedb/gamedb.db'
anagram = Anagram(gamewords)

# Create database file and table if not exist
db = GamedbManager(dbfile)
# db.create_table()

class MyAngram:

    def __init__(self):
        pass

    def head(self):
        appname = "MyAnagram Game Application"
        pro_info = "Challenge yourself to best the world of word game"
        pro_info_1 = "This application is powered by commands. Use the following to \n\tperform most common tasks. Use 'mangram' for more."

        line = "__________________________________________________________________"

        print("\t\t", appname)
        print("\t", pro_info)
        print(line)
        print(pro_info_1)
        print("\n")
        print("Game Mode: 'play'\tDisplay Mode: 'ds'\tApp Manual: 'mangram' ")
        print(line)

    def main(self):
        self.head()
        done = False
        cmds = ["play", "mangram", "ds", "done"]

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
                    case "play":
                        print("\n\t\t\tGame Mode")
                        print("\t\tNavigate the Game Mode: ")
                        print("\tShuffle: 's'\tQuit: 'q'\tPass: 'Enter' ")
                        print("\t____________________________________________")
                        val = anagram.gameloop()
                    case "ds":
                        val = anagram._getrecords_()
                    case "mangram":
                        val = anagram.mangram()


#   ====================================================================================

if __name__ == '__main__':
    myangra = MyAngram()
    myangra.main()