"""
  ASCII hangman art code reference taken from MJ Linane which I found on Google
  which directed me to his github
"""


def display_hangman(lives):
    stages = [  # final state: noose, head, torso, both arms, and both legs
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
                # noose, head, torso, both arms, and one leg
                """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
                """,
                # noose, head, torso, and both arms
                """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
                """,
                # noose, head, torso, and one arm
                """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
                """,
                # noose, head & torso
                """
  +---+
  |   |
  O   |
      |
      |
      |
=========
                """,
                # noose & head
                """
  +---+
  |   |
      |
      |
      |
      |
=========
                """,
                # noose
                """
  +---+
      |
      |
      |
      |
      |
=========
                """
                # initial empty state
    ]
    return stages[lives]
