import os
import time
from hangman import Hangman

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

Tips:
  - Try to guess common letters (like vowels) first to narrow down the word.
  - Letters you have already guessed will not be registered
  - Remember: You have a limited number of incorrect guesses!

Have fun and good luck!

Press enter to resume the game now

----------------------------------------
"""


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
        self.game = Hangman("tester")
        self.gameState: int = 1 # 0 is exit, 1 is welcome, 2 is in-game, 3 is endscreen
        self.previousStatement = ""
        
    
    

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
            print("Get out") 
            self.gameState = 0
            return

        if self.gameState == 3:
            return

        if usrInput.startswith("/"):
            if usrInput == "/help":
                self.gameState = 5 # set the gamestate to help
            elif usrInput == "/start" and self.gameState == 1:
                self.gameState = 2 # sets the game state to be ingame if in welcome page
            else:
                statement = "Invalid command detected :( "
                print(statement)
                self.previousStatement = statement
        
        else:
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
                    self.handleInput()
                case 2: # ingame
                    while self.game.getLife() > 0 and "_" in self.game.displayString() and self.gameState == 2:
                        self.renderGame()  # Display the current hangman state and word
                        print("What's your next move?")
                        self.handleInput()  # Handle user input for guesses or commands
                    if self.game.getLife() == 0: # Loss
                        self.renderGame() 
                        print("\nGame over! The word was:", self.game.word)
                        self.gameState = 3
                    elif self.gameState ==2: # Win
                        print("Congratulations! You've guessed the word!")
                        self.gameState = 3  # Transition to End Screen
                case 3: # endscreen
                    print("Type in /exit to leave and press enter to try a again...")
                    self.handleInput()
                    self.gameState = 4 
                case 4: # reset
                    self.game = Hangman("newtest")
                    self.previousStatement = ""
                    self.gameState = 2
                case 5: # help
                    print(ghost)
                    print(helpPrint) 
                    input("> ")
                    self.gameState = 2
                case _:
                    print("Default case: You are not supposed to see this")
    
        
        print("Thank you for playing. Goodbye ^w^")

    

    
    


if __name__ == '__main__':
    ui = UserInterface()
    ui.run()
