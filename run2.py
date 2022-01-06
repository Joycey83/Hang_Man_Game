"""
Code for Hangman Game was inspired from a Youtuber called MJ Codes
Imports from the bulit-in Python functions
"""

import random
import time
from graphics_and_words import HANGMAN_GAME_LOGO, HANGMAN_GRAPHICS, WORDS

# Basic functions & Constant variables for the game
NUMBER_MISTAKES = 0
letters_guessed = []
NUMBER_MISTAKES_ALLOWED = len(HANGMAN_GRAPHICS)
word = random.choice(WORDS)
letters_word = list(word)
wrong_letters = []



def validate_input_no_empty(input):
    # Validate is not empty
    if not input:
        return False
    return True


def start_game():
    print(HANGMAN_GAME_LOGO)
    input_is_invalid = True
    while input_is_invalid is True:
        name = input("ENTER YOUR PLAYER NAME ->\n ")
        input_is_invalid = not validate_input_no_empty(name)
        if input_is_invalid is False:
            print("Welcome to Hangman " + name + "! Best of Luck...")
            print("You will only have 8 lives to get the word correct")
            time.sleep(2)
            print("Game begins now...\n")
            time.sleep(2)
            play_game(name, word, letters_word)
        else:
            print('Cant be an empty username \n')


def print_word_hidden(word):
    hidden_word = ''
    for letter in word:
        hidden_word += '_ '
    print(hidden_word)


def get_guess(already_guessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Enter a single letter")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER")
        else:
            return guess


def play_game(username, word, letters_word):

    # Amount of letters the word has
    print()
    print('The word has {} letters'.format(len(letters_word)))
    print_word_hidden(word)
    

if __name__ == "__main__":
    start_game()
   