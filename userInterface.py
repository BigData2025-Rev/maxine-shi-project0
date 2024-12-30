import os
import random
import pandas as pd
from hangman import Hangman
from scoreboardManager import ScoreboardManager



stages = [
        """
          -----
         |     
         |
         |
         |
         |
       =========
        """,
        
        """
          -----
         |     
         |     O
         |
         |
         |
       =========
        """,
        """
          -----
         |    
         |     O
         |     |
         |
         |
       =========
        """,
        """
          -----
         |     
         |     O
         |    /|
         |
         |
       =========
        """,
        """
          -----
         |     
         |     O
         |    /|\\
         |
         |
       =========
        """,
        """
          -----
         |     
         |     O
         |    /|\\
         |    /
         |
       =========
        """,
        """
          -----
         |     
         |     O
         |    /|\\
         |    / \\
         |
       =========
        """,
        """
          -----
         |     |
         |     O
         |    /|\\
         |    / \\
         |   GAME OVER
       =========
        """
    ]

ghost = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡿⣿⣷⣄⠀⠀⡀⢀⠀⠀⢀⠀⠀⠀⠀⠀⣀⣴⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⣿⣿⣿⣿⣶⣷⣿⣿⣿⣿⣿⣿⣷⣏⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⢀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⡏⠈⠛⢿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠈⢹⣿⢷⣢⡀⠀⢙⣿⣿⣿⣖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠁⠀⣸⣿⣦⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣤⣤⣤⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢹⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣶⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠉⠛⠿⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠅⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⠇⠀⠀
"""

helpPrint = """

----------------------------------------
                Boo!
----------------------------------------
 
In this game, your goal is to guess the hidden word one letter at a time. Be careful—you only have 8 incorrect guesses!

Instructions:
  - Type a single letter to guess it.
  - Type the full word to attempt solving it.
  - Type `/help` to view this help menu.
  - Type `/exit` to exit the game.
  - Type `/score` to check the scoreboard.

Tips:
  - Try to guess common letters (like vowels) first to narrow down the word.
  - Letters you have already guessed will not be registered
  - Remember: You have a limited number of incorrect guesses!
  - How many word you can guess correctly in a row will be your score

Have fun and good luck!

Press enter to resume the game now

----------------------------------------
"""

words = pd.read_csv("wordlist.csv")
words = words["Word"].tolist()
word = random.choice(words)

def clearTerminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')     
    # For MacOS and Linux
    else:
        os.system('clear')

def welcome():
        clearTerminal()
        print(
"""
Welcome to Hangman, mortal!

Type in /start to start the game now
        /start <name> to start the game and save your score
        /score to check the scoreboard
        /exit to get out of the game
        /help for the rules and commands at anytime


"""
)       
        print(ghost)

class UserInterface:

    
    def __init__(self):
        """
        Clear the terminal and print welcome screen for players

        """
        self.game = Hangman(word)
        self.gameState: int = 1 # 0 is exit, 1 is welcome, 2 is in-game, 3 is endscreen
        self.previousStatement = ""
        self.streak = 0
        self.scoreboard = ScoreboardManager()
        self.player = None
        

    def renderGame(self):
        """
        Clear terminal and renders the hangman and the text of the game

        """
        clearTerminal()
        print(self.game.displayString()) # printing display string
        print(stages[7-self.game.getLife()]) # printing Hangman
        print(self.game.renderHealth())
        print(",".join(self.game.history)) # printing History

    def handleInput(self):
        """
        Handles all user input including future commands

        """
        print(self.previousStatement) if self.previousStatement!="" else None
        self.previousStatement = ""
        usrInput: str = input('> ')
        usrInput = usrInput.strip().lower()

        if usrInput == "/exit":
            if self.player != "":
                print(f"Goodbye, {self.player}!")
                self.scoreboard.addScore(self.player, self.streak)
            else:
                print("Goodbye!")
            self.gameState = 0
            return
        elif self.gameState == 3:
            return
        elif usrInput == "/help":
            self.gameState = 5 # set the gamestate to help
        elif usrInput.startswith("/") and self.gameState<3:
            if usrInput.startswith("/start") and self.gameState==1:
                args = usrInput.split()
                if len(args) == 2:  # /start <name>
                    self.player = args[1].upper()
                    statement = f"Welcome, {self.player}! Your score will be tracked."
                    print(statement)
                    self.previousStatement = statement
                    self.gameState = 2  # Start the game
                elif len(args) == 1 and usrInput == "/start":  # Just /start
                    statement = "Welcome! Starting the game without saving your score."
                    print(statement)
                    self.previousStatement = statement
                    self.gameState = 2  # Start the game
                else:
                    print("Invalid command format. Use /start <name> or /start.")
            elif usrInput == "/streak":
                statement = "Your current streak is" + self.streak
                print(statement)
                self.previousStatement = statement 
            elif usrInput == "/score":
                self.gameState = 6 # sets the game state to be ingame if in welcome page 
            else:
                statement = "Invalid command detected :( "
                print(statement)
                self.previousStatement = statement
        elif self.gameState==2:
            if len(usrInput) == 1 and usrInput.isalpha():  # Single letter guess
                self.game.checkInput(usrInput)
            elif len(usrInput) > 1:  # Full word guess
                self.game.checkInput(usrInput)
            else:
                statement = "Invalid input. Please enter a letter, a word, or a valid command."
                print(statement)
                self.previousStatement = statement

    def run(self):

        while(self.gameState):
            match self.gameState:
                case 0: # quit
                    pass
                case 1: # welcome
                    welcome()
                    prevState=1
                    self.handleInput()
                case 2: # ingame
                    while self.game.getLife() > 0 and "_" in self.game.displayString() and self.gameState == 2:
                        self.renderGame()  # Display the current hangman state and word
                        print("What's your next move?")
                        prevState=2
                        self.handleInput()  # Handle user input for guesses or commands
                    if self.game.getLife() == 0: # Loss
                        self.renderGame() 
                        print("\nGame over! The word was:", self.game.word)
                        self.gameState = 7
                    elif self.gameState == 2: # Win
                        self.renderGame()
                        print("Congratulations! You've guessed the word! It was", self.game.word)
                        self.streak += 1
                        self.gameState = 3  # Transition to End Screen
                case 3: # Win endscreen
                    print("Type in /exit to leave and press enter to play another round...")
                    prevState = 3
                    self.handleInput()
                    if self.gameState == 3:
                        if self.player != None:
                            self.scoreboard.addScore(self.player, self.streak)
                        self.gameState = 4 
                case 4: # reset
                    self.scoreboard=ScoreboardManager()
                    self.game = Hangman(random.choice(words))
                    self.previousStatement = ""
                    self.gameState = 2
                case 5: # help
                    print(ghost)
                    print(helpPrint) 
                    input()
                    self.gameState = prevState
                case 6: # scoreboard
                    self.scoreboard.displayScoreboard()
                    input()
                    self.gameState = prevState
                case 7 : # lose endscreen
                    print("Type in /exit to leave and press enter to try a again...")
                    prevState = 7
                    self.handleInput()
                    self.scoreboard.addScore(self.player,self.streak)
                    self.streak = 0
                    if self.gameState == 7:
                        self.gameState = 4 
                case _:
                    print("Default case: You are not supposed to see this")
    
        
        print("Thank you for playing. Goodbye ^w^")

if __name__ == '__main__':
    ui = UserInterface()
    ui.run()
