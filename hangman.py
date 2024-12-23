class Hangman:
    def __init__(self, word: str):
        """
        Construct a new Hangman object with the given word to guess.
        
        Args:
            word (str): The word to guess
        
        """
        self.word: str = word
        self.lifecount: int = 8
        self.history: set = set()  # Store the guessed letters, set is used to avoid duplicate letters
        self.revealed: set = set() # Store the indexes of the revealed letters

    def displayString(self) -> str:
        """
        Return the current state of the word to guess.
        
        Returns:
            str: The current state of the word to guess
        
        """
        display = ''

        for i in range(len(self.word)):
            if i in self.revealed:
                display += self.word[i]
            else:
                # print a underline space
                display += "_"

        return display
        
    def checkInput(self, input: str):
        if len(input) > 1:
            if input==self.word:
                print()


if __name__ == '__main__':
    import userInterface
    print("This is hangman")