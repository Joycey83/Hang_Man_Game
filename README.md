# HANGMAN GAME

For my portfolio 3 project I have chosen a fun school favourite, a well known game called Hangman. This game Hangman will be displayed in a Python terminal, which runs through the Code Institute terminal on Heroku.

[View the live project here.](https://hangman-83.herokuapp.com/)

---

![page mock up.](assets/images/hangman-mock-up.JPG)

---
# How to play Hangman
Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, within a certain number of guesses.
However, in this game, one player is only needed as the words are automatically randomized and the lives will automatically be deducted for any incorrect guess. The User will enters their desired Username and the game will select a random word from a word list.
The word to be guessed will be displayed as _ _ _ _ _ and with an image of a hangman in different stages depending on the number of incorrect guesses. In this game the player will have 8 attempts to guess the correct letters for the word. When the User guesses a letter that is in the random word, the terminal will display the correct letter guessed, this will replace the blank dashes _ _ _ with the correct letter and in the correct position, in this example the letter “t” will replace the third blank space of the random word _ _t. This process will continue until the player has run out of guesses and then will be 'You are HANGED in the gallows!!' on a platform.  This will be shown on the terminal and a message letting the User know they have 'died' and have lost the game. The other option will be that the User continued guessing the correct letters and got the correct word before running out of lives. When the User has either wins or loses, they will have the option to play again.

# User Experience (UX)

+ ## User Stories
    - ### First Time User
    1. As a first time user, I want to easily navigate through the game with simple inputs.
    2. As a first time user, I want to be able to have fun, enjoy the game and feel nostalgic when playing.
    - ### Returning User
    1. As a Returning user, I want the navigation to be the same as it was the first time to keep it familiar.
     2. As a Returning user, I want to be able to guess different words that I haven't guessed before.
    - ### Frequent User
    1. As a Frequent User, I want to be able to notice different words still being guessed.
    2. As a Frequent User, I want the navigation to be the same throughout.

---
# Flow Chart of Hang Man Game
![Hang Man Flow Chart.](assets/images/flowchart-final-hangman.jpg)

----
# Features
## Existing Features

* **Game Heading & Hangman Display**
  * A appealing ASCII code text and display image of the Hangman Game will be shown to introduce the player to the game.
![Hang Man Heading.](assets/images/hang-man-heading.JPG)
![Hang Man Display.](assets/images/hang-man-display.JPG)

* **Player Name**
  * The player will be asked to enter a name before the Hangman Game can start, The game will not start without a player name. If the player just leaves it blank and press enter a prompt message letting the player know that they will need to enter a name in order to start the game.

![Player Name.](assets/images/playername.JPG)
![Player Name Validation.](assets/images/playername-validation.JPG)

* **Welcome Message**
  * After the player has entered a player name a short welcome message will be shown. A message letting the player know how many lives that they have to play this game will also be shown.

![Welcome Message.](assets/images/welcome-message.JPG)

* **Guessing the letter or Word**
  * The Guessing screen displays the hangman title, the first stage of the hangman game. Underneath the hangman display it will also show the player the number of letters of the word that they need to guess. The player is asked to input a guess of a letter or word.

![Guessing Screen.](assets/images/guessing-screen.JPG)

* **Incorrect Letter**
  * when the player guess is valid but is not in the word, they are greeted with text stating that their guess was not in the word, therefore being incorrect the player will lose a life and this will display the next stage of hangman.

![Incorrect Letter.](assets/images/incorrect-letter-screen.JPG)

* **Correct Letter**
  * When the player guess is valid and also correct, they are greeted with text praising them and stating that their guess is in the word, therefore being correct a life will not be lost so the hangman display will stay at the same stage until the next correct or incorrect guess.

![Correct Letter.](assets/images/correct-letter-screen.JPG)

* **Guess Word**
  * The player can type in the whole word if they feel that after a few guesses, they already know the secret word. Once the whole word is typed a message will allow the player to tell them if their guess was correct or not.

![Guess Word Screen.](assets/images/guess-word-screen.JPG)

* **Letters Guessed**
  * Each time the player enters a valid letter it will be shown on the display to let the player know which letters that they have tried. In theory it should stop the player from inputting repeated letters.

![Letters Guessed.](assets/images/guessed-letter-screen.JPG)

* **Already Guessed**
  * As the game plays on, often the player may accidentally guess a letter that they have already guessed, even though we have added the letters on to the Letter Guessed display. As a fall back we will also display a text to let the player know that they have already guessed that letter.

![Already Guessed.](assets/images/already-guess.JPG)

* **Invalid Guess**
  * When the player guess is invalid(1,&,?) etc, they are are greeted with text stating that their guess is not a valid character(not a letter).

![Validation of Letter.](assets/images/validation-of-letter-screen.JPG)

* **Hangman Display**
  * The Player will be able to see their progress of not only the hangman stages but also the letters that they have used previously in the current game. With each incorrect letter or word guessed, the hangman display will go to the next 'stage' of the display until the User gets the word correct or runs out of lives, which will the show either a congratulations screen or an unfortunate lose screen.

![Hangman Stages.](assets/images/hang-man-stages.JPG)

---
# Technology Used

---
# Testing

---
# Deployment

---
# Credit & Acknowledgement



