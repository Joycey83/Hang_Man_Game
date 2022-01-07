"""
  ASCII hangman art code reference taken from MJ Linane which I found on Google
  which directed me to his github
"""


def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                  """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
                """,
                
                """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
                """,
                # head, torso, both arms, and one leg
                """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
                """,
                # head, torso, and both arms
                """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
                """,
                # head, torso, and one arm
                """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
                """,
                
                """
  +---+
  |   |
  O   |
      |
      |
      |
=========
                """,
                
                """
  +---+
  |   |
      |
      |
      |
      |
=========
                """,
                # initial empty state
                """
  +---+
      |
      |
      |
      |
      |
=========
                """
    ]
    return stages[lives]
