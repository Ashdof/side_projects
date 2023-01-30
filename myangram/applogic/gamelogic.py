"""
=======================     MY ANAGRAM GAME APPLICATION     ===================================
    FILE:                   GAME LOGIC CLASS
    DATE:                   04-NOV-2022
    LAST UPDATED:           30-JAN-2023
    DEVELOPER:              EMMANUEL ENCHILL
    DESCRIPTION:            THIS IS A SIMPLE GAME APPLICATION. IT DISPLAYS SHUFFLED WORDS FOR THE USER TO GUESS THE
                            CORRECT SPELLING. IT SAVES GAME RECORDS TO AN SQLite3 DATABASE FILE

    MODULE DESCRIPTION:     THIS MODULE IS THE LOGIC OF THE GAME. THE METHODS DISPLAY SHUFFLED WORDS, TAKES INPUTS FROM
                            THE STANDARD INPUT AS GUESSES, COMPARES AND AWARD MAKRS FOR CORRECT GUESS AND PASS INFORMATION
                            TO THE DATABASE MODULE FILE TO BE COMMITTED TO THE DATABASE. METHODS ALSO DISPLAY RECORDS AND
                            TRACK GAME PROGRESS
"""

#!/usr/bin/env python3

import random
import datetime
from applogic.dbclass import GamedbManager

dbfile = 'applogic/gamedb/gamedb.db'
db = GamedbManager(dbfile)
ddate = datetime.datetime.now()
game_date = str(ddate.year) + "-" + str(ddate.month) + "-" + str(ddate.day)

class Anagram:

    def __init__(self, filepath):
        """Initialise class variables
        
        Arguments:
            filepath (string):  path to the file or name of the file
        """
        self.__filepath = filepath
    
    def get_filepath(self):
        """Get Filepath

        Description:
        This method gets the file path
        
        Returns:
        The path of the file
        """
        return self.__filepath


    def gameloop(self):
        """The Game Loop

        Description:
        This method keeps the application in the loop. The user can access all the
        functionalities of the application while in the loop. The application exits
        when any value in the 'quits' list is provided to the 'Question' and then
        presses the Enter or Return key

        """

        rounds = 0
        score = 0
        done = False
        
        quits = ["q", "quit", 'Q', "Quit", "QUIT"]
        best = ["Awesome!", "Wow!", "Bingo!", "Genius!"]
        better = ["Very good!", "Better!", "Do more!", "Congrats!"]
        good = ["Good!", "Correct!", "Keep up!", "Lucky!"]

        while not done:
            
            asem = self.get_word()
            quest = self.shuffle_word(asem)
            print("\nNew word: ", quest)

            rounds += 1

            for i in range(3, 0, -1):

                """Invoke the guessword method"""
                guess = self.guessword(i)

                if guess in quits:
                    """Save record to database, print game summary quit"""
                    db.save_record(game_date, rounds, score)
                    print("\nSummary: ")
                    print(self.__str__(rounds, score))
                    print("\nGame Mode cancelled")
                    done = True
                    break

                elif guess == "s":
                    """Reshuffle the word

                    Description:
                    This block reshuffles the word but should retain the counter (i) at the same
                    number at which the shuffle_word method was invoked. It needs more work

                    """
                    print("Reshuffled: ", self.shuffle_word(asem))

                elif i == 3 and guess == asem:
                    """Score highest mark for correct guess at the first attempt"""
                    print(random.choice(best))
                    print("Score: ", 5)
                    score += 5
                    
                    break

                elif i == 2 and guess == asem:
                    """Score medium mark for correct guess at the second attempt"""
                    print(random.choice(better))
                    print("Score: ", 3)
                    score += 3

                    break

                elif i == 1 and guess == asem:
                    """Score lowest mark for correct guess at the third attempt"""
                    print(random.choice(good))
                    print("Score: ", 1)
                    score += 1

                elif i == 1 and guess != asem:
                    """Score nothing and print correct word"""
                    print("Correct word: ", asem)
                    print("Score: ", 0)
                    score += 0


    def guessword(self, attempt):
        """Guess the correct word
        
        Description:
        This method takes input from the standard input as the user attempts at guessing
        the correct spelling of the word

        Arguments:
            attempt (int): a counter to track number of attempts made
        """

        guess = input("Attempt {}: ".format(attempt)).lower()

        return guess


    def shuffle_word(self, asem):
        """Shuffle word

        Description:
        This method shuffles the word passed to it as its parameter

        Arguments:
            asem (string):   the word passed to this method as parameter
        """
        asemlist = list(asem)
        shuffled = asem
        done = False

        while not done:
            random.shuffle(asemlist)
            shuffled = ''.join(asemlist)

            if shuffled != asem:
                return shuffled


    def get_word(self):
        """Select a word

        Description:
        This method selects a word at random from  a sea of words in a file.
        The file has no extension

        Returns:
            A single word upon each invocation
        
        """
        file = self.get_filepath()

        rec = open(file, 'r')
        wordstore = list(rec)
        while True:
            getword = random.choice(wordstore).strip()

            if getword == "":
                continue

            return getword

    
    def __str__(self, _round, _totalscore):
        """Return a string representation of values

        Description:
        This method overrides the __str__() function and returns a string
        representation of game records

        Arguments:
            _round (int): an integer value that represents the current stage of the game
            _totalscore (int): an integer value that represents the total score earned so far

        Returns:
        A brief summary of game stage and score
        """

        return "Game stage: {}\nTotal score: {}".format(_round, _totalscore)

    
    def mangram(self):
        """The application's manual

        Description:
        This method reads the information from file and display it on the screen. The contents
        detail rules and commands for playing the game and navigating the application

        """
        man = open("mangram", "r")

        for line in man:
            print(line, end='')
        man.close()


#===============    DATABASE ACCESS SECTION     ==================================

    def _getrecords_(self):
        """Display Records
        
        Description:
        This method displays the records of the game. User is presented with options to
        from to choose how to display the record
        the option chosen by the user

        Options:
            1: detail record display in table
        
        """
        
        done = False

        print("\nSelect the number for a corresponding record to display")
        print("To exit the display mode, press the enter or return key\n")
        print("1: Detail Record")
        
        while not done:
            val = input("\nNumber ?>: ")

            if val == "":
                print("Display Mode cancelled")
                done = True
                
            else:
                match val:
                    case "1":
                        db.display_detail_records()
                        done = True

                    # case "2":
                    #     db.display_names_and_codes()
                    #     done = True

                    # case "3":
                    #     db.display_names_prof_contacts()
                    #     done = True

                    # case "4":
                    #     db.display_names_and_numbers()
                    #     done = True

                    # case "5":
                    #     db.display_names_email_addresses()
                    #     done = True