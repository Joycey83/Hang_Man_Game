# Code for Hangman Game referenced from a Youtuber called MJ Codes
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

words = ['act', 'air', 'age', 'bag', 'cap', 
         'map', 'area', 'baby', 'card', 'dish', 
         'exam', 'good', 'boards', 'chair', 
         'count', 'facts', 'green', 'house']

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

NUMBER_MISTAKES = 0
letters_guessed = []
NUMBER_MISTAKES_ALLOWED = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []

# Amount of letters the word has
print()
print('The word has {} letters'.format(len(letters_word)))

# while loop which will run until the number of mistakes =
# Number mistakes allowed
# Each wrong letter will take away each guesses left

while NUMBER_MISTAKES < NUMBER_MISTAKES_ALLOWED:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('Guesses left: {}'.format(NUMBER_MISTAKES_ALLOWED - NUMBER_MISTAKES))
    letter_user = input('Enter a letter --> ')  
# checking if the letter has been guessed before

    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print('You have already USED this letter, enter another one please')
        letter_user = input('Enter a letter --> ')
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
        print(hangman_graphics[NUMBER_MISTAKES - 1])
    print()
    print('-------------------------------------------')
# Word guessed correctly so player wins
    if len(letters_guessed) == len(letters_word):
        print()
        print('Congratulations!YOU WOOOON!!!')
        break
# Word guessed incorrectly so player lose
if NUMBER_MISTAKES == NUMBER_MISTAKES_ALLOWED:
    print()
    print('OOOH NO!!..HANGED in the gallows!')   

