#! /usr/local/bin/python3

from .cards import(
    Card,
    Collection,
    Deck)

from .players import(
    Hand,
    Player,
    HumanPlayer,
    Dealer)

from .game import Game


def main():
    """The main function - only called if __name__ == __main__."""

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


main()
