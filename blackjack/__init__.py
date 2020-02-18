"""A blackjack game written in Python.

This package written in Python version 3.7. To use the package,
you probably need python 3.7 or newer.

This package can be run as a script using the -m flag
    python3 -m blackjack

For further information on running the program or playing a game,
see the readme file.

Thi package can be imported in the following ways:

    # keeps namespaces separate:
    import blackjack as bj

    # becasue __all__ in defined, this won't clutter up the namespace too much:
    from blackjack import * 

For further informatino on the Classes defined in this package, see the documentation file.
"""

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

# Allows for `from blackjack import *` 
__all__ = ['Card',
           'Collection',
           'Deck',
           'Hand',
           'Player',
           'HumanPlayer',
           'Dealer',
           'Game']
