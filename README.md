# maxine-shi-project0
## Hangman Text Game
### Programmer: Maxine Shi

Design and implement a hangman game that allows the user to guess a word. 

## Required Features:
 - CLI-based game
 - Read a list of words from a file
 - Write user win streak to a json format

## Game Principles:
 - The user has 8 chances to guess the word. 
 - A word is randomly selected from a list of words. The user can guess a letter or the entire word. 
 - If the user guesses a letter that is in the word, the letter is revealed. 
 - If the user guesses a letter that is not in the word, the user loses a chance. 
 - If the user guesses the word, the user wins. 
 - If the user runs out of chances, the user loses. The user can play again if they win or lose.
  
## To Play:
  - Download the folder
  - Open a terminal within the project0 folder
  - Ensure the correct version of python is installed
  - Pip install required package with following command
    - ```pip install -r requirements.txt```
- Run the program with the following command
  - ```python userInterface.py```

## Utilizations:
- Python Version: 3.13.1
 - Miniconda
   - conda activate <env>
   - change VScode Interpreter to conda version
 - Pandas
 - Tabulate
