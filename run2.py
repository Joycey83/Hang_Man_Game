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


while NUMBER_MISTAKES < NUMBER_MISTAKES_ALLOWED:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print("{}, ".format(letter), end='')
    print()
    print("Guesses left: {}".format(NUMBER_MISTAKES_ALLOWED - NUMBER_MISTAKES))
    letter_user = input('Enter a letter -->\n')  
# checking if the letter has been guessed before

    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print('You have already USED this letter, enter another one please')
        letter_user = input('Enter a letter -->\n ')
# if the letter not in the word the wrong letter will be printed for the player
    if letter_user not in letters_word:
        NUMBER_MISTAKES += 1
        wrong_letters.append(letter_user)
    
    print()
    print('Word: ', end='')
# If the letter is correct it will replace the blanks in the correct space
    for letter in letters_word:
        if letter_user == letter:
            letters_guessed.append(letter_user)

    for letter in letters_word:
        if letter in letters_guessed:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')

# Hangman graphics correlate with amount of mistakes made
    print()
    if NUMBER_MISTAKES:
        print(HANGMAN_GRAPHICS[NUMBER_MISTAKES - 1])
    print()
    print('-------------------------------------------')
# Word guessed correctly so player wins
    if len(letters_guessed) == len(letters_word):
        print()
        print("Congratulations! You have WOOON!!") 
        break
    
# Word guessed incorrectly so player lose
if NUMBER_MISTAKES == NUMBER_MISTAKES_ALLOWED:
    print()
    print("OH NOO!!! You are HANGED in the gallows!!")   


def play_game(username, word, letters_word):

    # Amount of letters the word has
    print()
    print('The word has {} letters'.format(len(letters_word)))
    print_word_hidden(word)


if __name__ == "__main__":
    start_game()