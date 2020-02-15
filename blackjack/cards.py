"""
A learning exercise to learn OOP in python.

"""

import random


class Card():
    """A playing card object

        Parameters
        ----------
            value : int
                The value of a card. 1 is Ace. 11 is Jack. 12 is Queen. 13 is King.

            suit : str
                The suit of the card. Generally 'Spades', 'Hearts', 'Diamonds', or 'Clubs'.

        Attributes
        -----------
            hidden : bool
                If true, the card is "face down" and can't be viewed with the show() method.
    """

    def __init__(self, value: int, suit: str, hidden=False):

        self._value = value
        self._suit = suit
        self._is_hidden = hidden

    @property  # use properties so these can't be changed from the outside.
    def value(self):
        """Returns the numerical value of the card. Returns None if self.hidden=True"""
        if not self._is_hidden:
            return self._value
        else:
            return None

    @property
    def suit(self):
        """Returns the suit of the card. Returns None if self.hidden=True"""
        if not self._is_hidden:
            return self._suit
        else:
            return None

    @property  # The only way to change the state of this card is to 'flip' it over
    def is_hidden(self):
        """Returns True if the card is hidden, False if the card is not hidden."""
        return self._is_hidden

    def flip(self):
        """ 'flips' the card over and changes the value of _is_hidden."""
        self._is_hidden = not self._is_hidden

    def info(self):
        """Prints the value and suit of the Card object."""

        if self._is_hidden:
            print("This card is hidden.")
            return None

        if self.value == 1:
            print(f'Ace of {self.suit}')
        elif self.value < 11:
            print(f'{self.value} of {self.suit}')
        elif self.value == 11:
            print(f'Jack of {self.suit}')
        elif self.value == 12:
            print(f'Queen of {self.suit}')
        else:
            print(f'King of {self.suit}')

    # Ordering functions:
    #     The following functions define an order on the cards. Note, the order depends entirely
    #     on the value of the card and nothing else. Bacause of this, two cards are equal
    #     if they have the same value but not necessarly the same suit.

    #     Card(4, 'Spades') == Cards(4, 'Hearts') # This will return true

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class Collection():
    """An object for a collection of cards. This is the base class for a deck of cards or a player's hand.

        Attributes:
        ----------
        cards : list
            A list to hold the playing card objects in the collection.

        replacement : bool
            If True, self.draw() does NOT remove a card object from the collection.
            If False, self.draw() removes a card object from the collection.
    """

    def __init__(self, cards=None, replacement=False):

        if cards is None:
            self._cards = []
        else:
            self._card_check(cards)
            self._cards = list(cards)
        self._replacement = replacement

    def __iter__(self):  # Allows for interation over the collection of cards
        # Returns the interator object for the _cards list
        return iter(self._cards)

    def __len__(self):
        """Returns the number of cards in the collection."""
        return len(self._cards)

    def __add__(self, other):
        """Defines addition on a collection of cards.
        Returns a new collection with all the same cards as self and other.
        """

        # type(self) makes sure the collection object can be subclassed.
        if type(other) is type(self):
            return type(self)(cards=list(self) + list(other))
        else:
            raise TypeError(
                f'can only concatenate {type(self).__name__} (not {type(other).__name__}) to {type(self).__name__}')

    def __getitem__(self, index):
        """Allows the collection object to be indexed."""
        return self._cards[index]

    def _card_check(self, to_check):
        """Checks the type of each object to be held by the collection"""
        try:
            for item in to_check:
                if type(item) is not Card:
                    raise TypeError(
                        f'{type(self).__name__} object can only hold Card objects')
            return None
        except TypeError:
            if type(to_check) is not Card:
                raise TypeError(
                    f'{type(self).__name__} object can only hold Card objects')
            return None

    def add(self, cards):
        """Adds a card object or a list of card objects to the collection"""
        self._card_check(cards)

        try:
            for card in cards:
                self.add(card)
        except TypeError:
            self._cards.append(cards)

    def draw(self):
        """Retuns a card object from the collection.
        if _replacement is False, removes the first card in the collection and returns that card
        if _replacement is True, returns a random card from the collection without removing the card
        """

        if self._replacement:
            return random.choice(self._cards)
        else:
            return self._cards.pop(0)

    def discard(self):
        """Clears _cards back to an empty list"""

        self._cards.clear()

    def hide(self):
        """flips all cards to a hidden state"""
        for card in self:
            if not card.is_hidden:
                card.flip()

    def info(self):
        """Prints the value and suit of each card in the collection."""

        for card in self:
            card.info()

    def reveal(self):
        """flips all cards to a not hidden state"""
        for card in self:
            if card.is_hidden:
                card.flip()

    def shuffle(self):
        """Randomizes the order of the collection of cards."""

        random.shuffle(self._cards)


class Deck(Collection):
    """ A deck of standard playing cards.

    A freshly initialized Deck object consists of 52 Card objects with the
    standard suits and values. This can be used as a deck of cards to
    play various games.

    Inharets from the Collection Class.
    """

    def __init__(self, cards=None, replacement=False):

        super().__init__(cards=cards, replacement=replacement)
        if self._cards == []:
            self._build()

    def _build(self):
        """Creats the 52 cards in a standard deck of playing cards.

        Note
        ----
            This method only adds cards. It does not remove cards from the deck. To remove cards,
            the discard() method in the parent class should be called
        """

        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.add(Card(value, suit))

    def reset(self):
        """Resets the deck to the original state: 52 standard playing cards."""

        self.discard()
        self._build()
