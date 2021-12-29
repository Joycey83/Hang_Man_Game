# Imports from the bulit-in Python functions


import random
import time

# Users input their names before starting to play the game
name = input("ENTER YOU NAME -> ")
print("Welcome to Hangman " + name + "! Best of Luck...")
print("You will only have 9 lives to get the word correct")
time.sleep(2)
print("Game begins now...\n")
time.sleep(2)
words = ['act', 'air', 'age', 'bag', 'cap', 'map', 
         'area', 'baby', 'card', 'dish', 'exam', 
         'good', 'boards', 'chair', 'count', 'facts',
         'green', 'house']

# Hangman images that will show 9 stages when player gets a letter wrong
hangman_graphics = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '                
                    ]

# Basic functions of the Hangman game

number_mistakes = 0
letters_guessed = []
number_mistakes_allowed = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []

