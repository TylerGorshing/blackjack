"""This Module defines Blackjack players and how they take their turns.

The following classes are included in this module:
    Hand
    Player
    HumanPlayer
    Dealer"""

from .cards import Collection


class Hand(Collection):
    """A player's hand in a game of blackjack. Extends the Collection Class. A hand instance is
    always empty at construction.

    Parameters
    ----------
        None

    Data Attributes
    ---------------
        value : int
            The value of the hand as determined by the rules of blackjack.

    Methods
    -------
        add(cards) :
            Adds a single card object or a list of card objects to the hand.

            Returns None

            Parameters
                cards : list or Card
                    The card or list of cards to be added to the hand.

        draw() :
            Removes a single card from the hand and returns that card.
            Returns Card

        discard() :
            Removes all cards from the hand.
            Returns None

        hide() :
            Sets the is_hidden attribute for each card in the hand to True.
            Returns None

        reveal() :
            Sets the is_hidden attribute for each card in the hand to False.
            Returns None

        shuffle() :
            Randomizes the order of the cards in the hand.
            Returns None

    Other Behaviors
    ---------------
        Length :
            Passing a hand into the len() method will return the number of cards in the hand.

        Iteration :
            A hand object is interable and will interate over all cards held by the hand.

        Concatination :
            Two hand objects can be concatinated with the '+' operator. This returns a new hand.

            Example: new_collection = collection_a + collection_b

        Indexing :
            A hand can be indexed to acces a card at a specific index.

            Example: card = hand[2]

            Note: Indexing can only access cards and cannot add or modify cards.

        String :
            Passing a hand into the str() method will return a string describing every card
            in the hand.
    """

    def __init__(self):
        """A Hand object will always be constructed with an empty _cards list and replacement set to False"""
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    def _update_value(self) -> int:
        """Updates value. This is called whenever a card is added to Hand object."""

        value_list = [card.value if card.value <= 10 else 10 for card in self]
        hand_value = sum(value_list)

        # Checks to see if any Aces can be worth 11 points instead of 1 point
        while value_list.count(1) > 0 and (21 - hand_value) >= 10:
            value_list[value_list.index(1)] = 11
            hand_value = sum(value_list)

        self._value = hand_value

    def add(self, cards):
        """Adds a card to the Hand and updates the value of the Hand"""

        super().add(cards)
        self._update_value()


class Player():
    """A blackjack player. The base class for the Dealer and HumanPlayer classes.

    Parameters
    ----------
        name : str
            The name of the player.

    Data Attributes
    ---------------
        had_turn : bool
            False if the player has not taken their turn. True if the player has taken their turn.

        hand : Hand
            The player's blackjack hand.

        name : str
            The player's name.

    Methods
    -------
    begin_trun() :
        Called at the beginning of a palyer's turn by the Game object.

        This method is required for the Game object, but it doesn't have to do anything.

    clean_up() :
        Empties the player's hand and set 'had_turn' to False. Called by the Game object at the end of a game.
        Returns None

    decision() :
        Allows the player object to 'hit' or 'stay' in a game of blackjack.
        Returns True if the player chooses to 'hit'.
        Returns False if the player chooses to 'stay'.
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
    """Allows a human user to interact with a game of blackjack. Extends the Player class.

    Parameters
    ----------
        name : str
            The name of the human.

    Data Attributes
    ---------------
        had_turn : bool
            False if the human has not taken their turn. True if the human has taken their turn.

        hand : Hand
            The human's blackjack hand.

        name : str
            The human's name.

    Methods
    -------
    begin_trun() :
        Called at the beginning of a palyer's turn by the Game object. Doesn't do anything for a human human.
        Returns None

    clean_up() :
        Empties the human's hand and set 'had_turn' to False. Called by the Game object at the end of a game.
        Returns None

    decision() :
        Ask the human if they want to hit or stay.
        Returns True if the human chooses to 'hit'.
        Returns False if the human chooses to 'stay'.
    """

    def __init__(self, name):
        super().__init__(name)

    def decision(self) -> bool:
        """Defines a human player's turn.
        Returns a bool to be handled by the game object.
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
    """The dealer in a game of Blackjack. Inherits from the Player class.

    Parameters
    ----------
        None

    Data Attributes
    ---------------
        had_turn : bool
            False if the dealer has not taken their turn. True if the dealer has taken their turn.

        hand : Hand
            The dealer's blackjack hand.

        name : str
            'The Dealer'

    Methods
    -------
    begin_trun() :
        Reveals any hidden cards in the dealer's hand. Called by the game object at the begining of the dealer's turn.
        Returns None

    clean_up() :
        Empties the dealer's hand and sets 'had_turn' to False. Called by the Game object at the end of a game.
        Returns None

    decision() :
        Determines if the dealer should hit or stay using the standard rules of blackjack
        Returns True if the dealer hits (hand value of less than 17).
        Returns False if the dealer stays (hand value of 17 or more).
    """

    def __init__(self):
        super().__init__('The Dealer')

    def begin_turn(self):
        self.hand.reveal()

    def decision(self):
        return self.hand.value < 17  # Returns True for 'hit' or False for 'stay'
