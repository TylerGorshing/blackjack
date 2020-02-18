"""This module is executed when the package is run as a script:
    python3 -m blackjack # requires python 3.7 or later

For more on running the program or playing a game, see the readme file.
"""

from .__init__ import *


def play_blackjack():
    """This function runs when the package is run as a script from the terminal.
    
    python3 -m blackjack
    """

    while True:
        try:
            number = int(input('How many human players are playing? \n'))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if number > 0:
            break
        else:
            print('Please enter a valid (positive) number.')

    players = []

    for i in range(number):
        name = input(f'What is the name of player {i+1}? \n')
        players.append(HumanPlayer(name))

    game = Game(*players)
    game()  # The game object is callable. Neat!

    while True:
        print('Another round? Y/N')
        answer = input().strip().lower()
        if answer == 'y':
            game()
        else:
            break


play_blackjack()
