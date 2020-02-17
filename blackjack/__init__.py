"""A blackjack game written in Python.

To play a game of blackjack

This package has 3 modules:
    cards
    players
    game"""

# import all custom classes into package namespace
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

__all__ = ['Card',
           'Collection',
           'Deck',
           'Hand',
           'Player',
           'HumanPlayer',
           'Dealer',
           'Game']
