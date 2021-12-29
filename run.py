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

# Tells you how many letters for that word
print()
print('The word has {} letters'.format(len(letters_word)))

# Add while loop letting player know the wrong letter and how many guesses left
while number_mistakes < number_mistakes_allowed:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print('{}, '.format(letter), end='')
    print()
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    letter_user = input('Enter a letter --> ')

# checking if the letter has been guessed before

while letter_user in letters_guessed or letter_user in wrong_letters:
    print()
    print('You have already USED this letter, enter another one please')
    letter_user = input('Enter a letter --> ')

print()
print('Word: ', end='')

# Add for loop that shows letters that the player has already used

for letter in letters_word:
    if letter_user == letter:
        letters_guessed.append(letter_user)

for letter in letters_word:
    if letter in letters_guessed:
        print(letter + ' ', end='')
    else:
        print('_ ', end='')

# Add else statement hangman graphics correlate with amount of mistakes made
print()
if number_mistakes:
    print(hangman_graphics[number_mistakes - 1])
print()
print('-------------------------------------------')

