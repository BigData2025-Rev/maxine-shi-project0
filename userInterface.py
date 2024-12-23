import os

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
Welcome to Hangman!

Type in /start to get start the game now
        /exit to get out of the game
        /help for the rules and commands at anytime


"""
)

class UserInterface:

    
    def __init__(self):
        """
        Clear the terminal and print welcome screen for players

        """
        self.gameState: int = 1 # 0 is exit, 1 is welcome, 2 is in-game, 3 is endscreen
        
        
    
    def run(self):

        while(self.gameState):
            match self.gameState:
                case 0:
                    pass
                case 1: # welcome
                    welcome()
                    self.handleInput()
                case 2: # ingame
                    self.renderGame()
                    print("What's your next move? ")
                    self.handleInput()
                case 3: # endscnreen
                    print("Press any key to restart ")
                    input()
                    self.gameState = 1
                case _:
                    print("Default case: You are not supposed to see this")
        
        
        print("Thank you for playing. Goodbye ^w^")

    

    def handleInput(self):
        """
        Handles all user input including future commands

        """
        loopInput = 1 # simulates a do while loop to enter the first loop
        while loopInput:

            loopInput = 0
            usrInput: str = input('> ')
            usrInput = usrInput.strip().lower()

            if usrInput.startswith("/"):
                if usrInput == "/help":
                    print("This is helping you") 
                    loopInput = 1
                    #TODO

                elif usrInput == "/exit":
                    print("Get out") 
                    self.gameState = 0

                elif usrInput == "/start" and self.gameState == 1:
                    self.gameState = 2 # sets the game state to be ingame if in welcome page


                else:
                    print("Invalid command detected :( ")
                    loopInput = 1

            else:
                print(usrInput)
                pass

    
    def renderGame(self):
        """
        Clear terminal and renders the hangman and the text of the game

        """
        
        print("Rendering")



if __name__ == '__main__':
    ui = UserInterface()
    ui.run()
