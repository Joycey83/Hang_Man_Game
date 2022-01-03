"""
Code for Hangman Game was inspired from a Youtuber called MJ Codes
Imports from the bulit-in Python functions
"""
import random
import time

# Add ASCII Art using a ASCII Art genrator to create hang man game
HANGMAN_GAME_LOGO = """

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗    
██║  ██║██╔══██╗████╗  ██║██╔════╝     ████╗ ████║██╔══██╗████╗  ██║    
███████║███████║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██╔██╗ ██║    
██╔══██║██╔══██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║    
██║  ██║██║  ██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    
                                                                        

 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

             .@==========================@                                   
             .@                          @                                   
             .@                          @                                   
             .@                          @                                   
             .@                          @                                   
             .@                          @                                   
             .@                          @                                   
             .@                         =@:                                  
             .@                       :%: -#.                                
             .@                      :*    .#.                               
             .@                      #.     :-                               
             .@                      %      .+                               
             .@                      *      .+                               
             .@                      *:     :-                               
             .@                       *    :#                                
             .@                       .*==-+                                 
             .@                          +                                   
             .@                          +                                   
             .@                     --.  + .+:                               
             .@                      .*#.+-*.                                
             .@                        .+%=                                  
             .@                          +                                   
             .@                          +                                   
             .@                          +                                   
             .@                          +                                   
             .@                          +                                   
             .@                         :@-                                  
             .@                        .+.*-                                 
             .@                       :*   +.                                
             .@                      .*    .#                                
             .@                     :+      -=                               
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
             .@                                                              
    =########%@#########                                                     
    .:::::::::::::::::::  
                                                                                                                                    
 """
print(HANGMAN_GAME_LOGO)

# Users input their names before starting to play the game
name = input("ENTER YOUR PLAYER NAME ->\n ")
print("Welcome to Hangman " + name + "! Best of Luck...")
print("You will only have 8 lives to get the word correct")
time.sleep(2)
print("Game begins now...\n")
time.sleep(2)

words = ['act', 'category', 'trainer', 'bag', 'cap', 
         'map', 'area', 'baby', 'card', 'dish', 
         'exam', 'convulsion', 'boards', 'chair', 
         'count', 'facts', 'green', 'house']

"""
ASCII hangman art code reference taken from MJ Linane which I found on Google
which directed me to his github
"""
hangman_graphics = ['''

  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Basic functions & Constant variables for the game
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
        print(hangman_graphics[NUMBER_MISTAKES - 1])
    print()
    print('-------------------------------------------')
# Word guessed correctly so player wins
    if len(letters_guessed) == len(letters_word):
        print()
        print('Congratulations!YOU WOOOON!!!')
        break
    playagain = input('Play again? (Y/N)\n ').upper()
    if playagain == 'Y':
        word = random.choice(words)
        break
    elif playagain == 'N':
        break
# Word guessed incorrectly so player lose
if NUMBER_MISTAKES == NUMBER_MISTAKES_ALLOWED:
    print()
    print('OOOH NO!!.. YOU ARE HANGED in the gallows!')   

