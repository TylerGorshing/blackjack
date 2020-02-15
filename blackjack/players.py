"""Defines Blackjack players and how they take their turns including the dealer."""

from .cards import Collection


class Hand(Collection):
    """A player's Blackjack hand.

    Inherits from the Collection class in the cards module.
    """

    def __init__(self):
        """A Hand object will always be constructed with an empty _cards list and replacement set to False"""
        super().__init__()
        self.value = 0

    def _update_value(self) -> int:
        """Updates value. This is called whenever a card is added to Hand object."""

        value_list = [card.value if card.value <= 10 else 10 for card in self]
        hand_value = sum(value_list)

        # Checks to see if any Aces can be worth 11 points instead of 1 point
        while value_list.count(1) > 0 and (21 - hand_value) >= 10:
            value_list[value_list.index(1)] = 11
            hand_value = sum(value_list)

        self.value = hand_value

    def add(self, cards):
        """Adds a card to the Hand and updates the value of the Hand"""

        super().add(cards)
        self._update_value()


class Player():
    """A blackjack player.

    This is the parent class for a human player and the dealer. It includes
    methods and attributes relevent to both kinds of players.
    """

    def __init__(self, name):

        self.hand = Hand()
        self.had_turn = False
        self.name = name

    def clean_up(self) -> None:
        """Resets the player for a new game.

        The method empties the player's hand and sets had_turn to False.
        """
        self.hand.discard()
        self.had_turn = False

    def begin_turn(self):
        """Called by the game object at the begining of the Player's turn.

        Not all players need to do something. """
        pass

    def decision(self):
        pass


class HumanPlayer(Player):
    """A class for a human player.

    The user intereacts with the game through an interactive python shell.

    Inherits from the Player class.
    """

    def __init__(self, name):
        super().__init__(name)

    def decision(self) -> bool:
        """Defines a human player's turn.
        Returns a bool to be handled by the game program.
        """

        while True:
            # Get's user input, makes all charactures lowercase, and removes any whitespace
            decision = input('Enter "hit" or "stay". \n').lower().strip()

            if decision == 'hit' or decision == 'stay':
                return decision == 'hit'
            else:
                # Humans can be dumb. Doesn't break the while loop
                print('\nYou must type "hit" or "stay".')


class Dealer(Player):
    """The dealer in a game of Blackjack. Inherits from the Player class."""

    def __init__(self):
        super().__init__('The Dealer')

    def begin_turn(self):
        self.hand.reveal()

    def decision(self):
        return self.hand.value < 17  # Returns True for 'hit' or False for 'stay'
