class Hangman:
    def __init__(self, word: str):
        """
        Construct a new Hangman object with the given word to guess.
        
        Args:
            word (str): The word to guess
        
        """
        self.word: str = word
        self.lifecount: int = 7
        self.history: set = set()  # Store the guessed letters, set is used to avoid duplicate letters
        self.revealed: set = set() # Store the indexes of the revealed letters


    def getLife(self) -> int:
        return self.lifecount
    
    def renderHealth(self) -> str:
        """
        Renders a health bar with full and empty ASCII hearts.
        
        Args:
            current_health (int): Current health points (e.g., 7).
            max_health (int): Maximum health points (e.g., 10).
        """
        fullHearts = "♥ " * self.lifecount
        emptyHearts = ". " * (7 - self.lifecount)

        # Combine full and empty hearts
        healthBar = fullHearts + emptyHearts
        return healthBar

    def displayString(self) -> str:
        """
        Return the current state of the word to guess.
        
        Returns:
            str: The current state of the word to guess
        
        """
        display = ''

        for char in self.word:
            if char in self.revealed:
                display+=" " + char + " "
            else:
                display+=" _ "

        return display
        
    def checkInput(self, input: str):
        """
        Check if the input is within the word to guess
        If it is more than 1 character check if it is the hidden word

        """
        if len(input) > 1:
            if input==self.word:
                self.revealed.update(input)
            else:
                self.history.add(input)
                self.lifecount-=1

        elif input not in self.history:
            if input in self.word:
                self.revealed.add(input)
            else:
                self.lifecount-=1
                self.history.add(input)
        else:
            print(f"You've already guessed '{input}'!")




if __name__ == '__main__':
    import userInterface
    print("This is hangman")