"""This module defines a game of blackjack and includes the Game class."""

from .cards import Deck
from .players import (
    HumanPlayer,
    Dealer,)


class Game():
    """Represents a game of blackjack.

    To start a game of blackjack

    Parameters
    ----------
        *players : Player or list
            The player or list of players to play the game of blackjack.

        summary : bool
            If True (the default), the game will print a summary of what's happening in the game.
            If False, the game will run without printing anything to the terminal.

    Notes
    -----
        A New Game :
            To play a game of blackjack, create a game instance by passing all player objects into the constructor,
            then simply call the game object.

            Example:
                game = Game(alice, bob) # creats a Game instance with all player objects
                game() # starts a new game of blackjack


        ALL players MUST have the following methods defined.
            begin_turn()
                This is called at the begining of a player's turn. Not all player's need to do something here, but
                for example, the dealer needs to reveal any hidden cards at the begining of their turn.

            decision()
                This is called when the player needs to choose to hit or stay and might be called
                several times during thier turn.

                return True if the player hits
                return False if the player stays

            clean_up()
                Called at the end of the game. Generally, the player dicards and had_turn is set to False in
                in preparation for their turn.
    """

    def __init__(self, *players, summary=True):
        self._summary = summary
        self._dealer = Dealer()
        self._players = players
        self._deck = Deck()

    def __call__(self):
        if self._summary:
            self._anounce('New Game!')

        self._deal()
        for player in self._players:
            self._turn_sequance(player)
        self._turn_sequance(self._dealer)

        if self._summary:
            self._results()

        self._clean_up()

    def _anounce(self, string_):
        """This bit of code is used a lot, so I'm making a function."""
        print(f'\n\n----- {string_} -----')

    def _deal(self):
        """Deals a game of blackjack. Defines a function to deal to the players and function to deal to the dealer.
        Resets shuffles the deck. Prints a summary of the deal if summary=True"""

        self._deck.shuffle()

        for player in self._players:
            player.hand.add([self._deck.draw(), self._deck.draw()])

        # Flips one of the dealer's cards facedown.
        self._dealer.hand.add([self._deck.draw(), self._deck.draw()])
        self._dealer.hand[0].flip()

        # Prints a summary of the deal if _summary is True.
        if self._summary:
            self._anounce('The Dealer')
            print(self._dealer.hand)

            for player in self._players:
                self._anounce(f'{player.name} with {player.hand.value}')
                print(player.hand)

    def _get_decision(self, player):
        decision = player.decision()

        if decision is True or decision is False:
            return decision
        else:
            raise TypeError(
                "The turn method of a Player object should return a bool: True or 'hit' or False for 'stay'")

    def _turn_sequance(self, player):
        """Defines a turn sequence for an individual player

        This method should work for ANY Player object, therefore
        ALL Player objects need a begin_turn() method and a decision() method.
        """

        player.begin_turn()
        hand_value = player.hand.value
        if self._summary:
            self._anounce(f'{player.name} with {hand_value}')
            print(player.hand)

        while hand_value <= 21:
            decision = self._get_decision(player)
            if decision:
                player.hand.add(self._deck.draw())
                hand_value = player.hand.value
                if self._summary:
                    print(f'{player.name} hits.\n')
                    print(player.hand)
                    print(f'\n{player.name} has {hand_value}.\n')
            else:
                if self._summary:
                    print(f'{player.name} stays with {hand_value}.\n')
                break

        player.had_trun = True  # Do I really need this?

        if hand_value > 21 and self._summary:
            print(f'{player.name} busts!\n\n')

    def _results(self):
        """Prints the outcome of the game player by player"""
        self._anounce('Final Results')
        dealer_score = self._dealer.hand.value

        for player in self._players:
            player_score = player.hand.value
            if player_score <= 21:
                if player_score < dealer_score < 21:
                    self._anounce(f'{player.name} Loses!')
                else:
                    self._anounce(f'{player.name} Wins!')
            else:
                self._anounce(f'{player.name} Busts!')

    def _clean_up(self):
        """Players discard to prepare for new game."""
        for player in self._players:
            player.clean_up()
        self._dealer.clean_up()
        self._deck.reset()
