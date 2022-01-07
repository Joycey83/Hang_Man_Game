import random
from words import word_list
from hang_man_logo import HANGMAN_GAME_LOGO
import time
from hangman import display_hangman


def validate_input_no_empty(input):
    # Validate is not empty
    if not input:
        return False
    return True


def main():
    print(HANGMAN_GAME_LOGO)
    input_is_invalid = True
    while input_is_invalid is True:
        name = input("ENTER YOUR PLAYER NAME ->\n ")
        input_is_invalid = not validate_input_no_empty(name)
        if input_is_invalid is False:
            print("Welcome to Hangman " + name + "! Best of Luck...")
            print("You will only have 7 lives to get the word correct")
            time.sleep(2)
            print("Game begins now...\n")
            time.sleep(2)
        else:
            print("NEED TO ENTER PLAYER NAME! \n")
    word = get_word()
    play_game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play_game(word)


def get_word():
    word = random.choice(word_list)
    return word.upper()


def print_secret_word(secret_word):
    new_word = f' {len(secret_word)} letters: '
    for letter in secret_word:
        new_word += f'{letter} '
    print(new_word)


def print_guessed_letters(guessed_letters):
    print(f'Guessed letters: {" ".join(guessed_letters)}')


def replace_guessed_letter(secret_word, guess, word):
    index = 0
    secret_word_list = list(secret_word)
    for letter in word:
        if guess.upper() == letter.upper():
            secret_word_list[index] = guess
        index = index + 1
    return "".join(secret_word_list)
     
     
def play_game(word):
    secret_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 7
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print_secret_word(secret_word)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a Letter or Word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                secret_word = replace_guessed_letter(secret_word, guess, word)
                
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                secret_word = word
        else:
            print("Not a valid Character.")
        print(display_hangman(lives))
        print_guessed_letters(guessed_letters)
        print_secret_word(secret_word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("OH NO!!, you are HANGED!. The word was " + word + ".Try again")

        
if __name__ == "__main__":

    main()