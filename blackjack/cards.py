"""
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

            is_hidden : bool
                If true, the card is "face down" and information about the Card can't be viewed.
                If None (the default) is_hidden is set to False

        Data Attributes
        ---------------
            value : int or None
                Returns the value of the card. If is_hidden is True, returns None.

            suit : str or None
                Returns the suit of the card. If is_hidden is True, returns None.

            is_hidden : bool
                A repesentation of wether information about the card can be accessed.
                True if the card is 'facedown' (no on can see the information). False if
                the card is 'faceup' (everyone can see the information).

        Methods
        -------
            flip() :
                Changes the value of is_hidden. This is like flipping a card from facedown to faceup.
                Returns None

        Other Behaviors
        ---------------
            Comparison Operators :
                Cards can be compared with the standard comparison operators (==, <, >, etc.).
                Only the value of the card is used for comparisons.

                Card(4, 'Spades') == Card(8, 'Spades') will return False
                Card(4, 'Spades') == Card(4, 'Hearts') will return True

            str() :
                Returns a string with information about the card in the
                form of '{value} of {suit}'

                str(Card(4, 'Spades')) will return '4 of Spades'
                str(Card(12, 'Hearts')) will return 'Queen of Hearts'
    """

    def __init__(self, value: int, suit: str, is_hidden=False):

        self._value = value
        self._suit = suit
        self._is_hidden = is_hidden

    @property  # use properties so these can't be changed from the outside.
    def value(self):
        """Returns the numerical value of the card. Returns None if is_hidden is True"""
        if not self._is_hidden:
            return self._value
        else:
            return None

    @property
    def suit(self):
        """Returns the suit of the card. Returns None if is_hidden is True"""
        if not self._is_hidden:
            return self._suit
        else:
            return None

    @property  # The only way to change the is_hidden state of this card is to 'flip' it over
    def is_hidden(self):
        """Returns True if the card is hidden, False if the card is not hidden."""
        return self._is_hidden

    def flip(self):
        """Changes the value of is_hidden. Like flipping a card facedown to hid all the information."""
        self._is_hidden = not self._is_hidden

    def __str__(self):

        if self._is_hidden:
            return "This card is hidden."

        if self.value == 1:
            return f'Ace of {self.suit}'
        elif self.value < 11:
            return f'{self.value} of {self.suit}'
        elif self.value == 11:
            return f'Jack of {self.suit}'
        elif self.value == 12:
            return f'Queen of {self.suit}'
        else:
            return f'King of {self.suit}'

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
    """An object for a collection of cards. This is the base class for Deck and Hand.

        Parameters
        ----------
            cards : list or None
                A list of card objects to be placed in the collection at construction.
                If None (the default), the collections is empty once constructed.

            replacement : bool
                Determines if cards are drawn from the collection with replacement or without replacenemt.
                This can only be set when a new instance is initialized. Once an instance is initialized, 
                replacement cannot be changed.

                If False (the default), cards are drawn without replacement.
                When the draw method is called, a card object is removed from the collection and returnd.

                If True, cards are drawn with replacement.
                When the draw method is called, a card is returned without removing the card from the collection.

        Methods
        -------
            add(cards) :
                Adds a single card object or a list of card objects to the collection.

                Returns None

                Parameters
                    cards : list or Card
                        The card or list of cards to be added to the collection.

            draw() :
                Returns single card from the collection.

                If replacement is False, the card is removed from the collection.
                If replacement is True, the card is NOT removed from the collection.

            discard() :
                Removes all cards from the collection.
                Returns None

            hide() :
                Sets the is_hidden attribute for each card in the collection to True.
                Returns None

            reveal() :
                Sets the is_hidden attribute for each card in the collection to False.
                Returns None

            shuffle() :
                Randomizes the order of the cards in the collection.
                Returns None

        Other Behaviors
        ---------------
            Length : 
                Passing a collection into the len() method will return the number of cards in the collection.

            Iteration :
                A collection object is interable and will interate over all cards held by the collection.

            Concatination :
                Two collection objects can be concatinated with the '+' operator. This returns a new collection.

                Example: new_collection = collection_a + collection_b

            Indexing :
                A collection can be indexed to acces a card at a specific index.

                Example: card = collection[2]

                Note: Indexing can only access cards and cannot add or modify cards.

            String :
                Passing a collection into the str() method will return a string describing every card
                in the collection.
    """

    def __init__(self, cards=None, replacement=False):

        if cards is None:
            self._cards = []
        else:
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

    def __str__(self):
        string_ = ''
        for card in self:
            string_ += str(card) + '\n'
        return string_

    def add(self, cards):
        """Adds a card object or a list of card objects to the collection"""
        try:
            for card in cards:
                self._cards.append(card)
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

    def reveal(self):
        """flips all cards to a not hidden state"""
        for card in self:
            if card.is_hidden:
                card.flip()

    def shuffle(self):
        """Randomizes the order of the collection of cards."""

        random.shuffle(self._cards)


class Deck(Collection):
    """ A deck of standard playing cards. Extends the Collection Class.

        Parameters
        ----------
            cards : list or None
                A list of card objects to be placed in the deck at construction.
                If None (the default), the deck will contain the 52 standard playing cards.

            replacement : bool
                Determines if cards are drawn from the deck with replacement or without replacenemt.
                This can only be set when a new instance is initialized. Once an instance is initialized, 
                replacement cannot be changed.

                If False (the default), cards are drawn without replacement.
                When the draw method is called, a card object is removed from the deck and returnd.

                If True, cards are drawn with replacement.
                When the draw method is called, a card is returned without removing the card from the collection.

        Methods
        -------
            add(cards) :
                Adds a single card object or a list of card objects to the deck.

                Returns None

                Parameters
                    cards : list or Card
                        The card or list of cards to be added to the deck.

            draw() :
                Returns single card from the deck.

                If replacement is False, the card is removed from the deck.
                If replacement is True, the card is NOT removed from the deck.

            discard() :
                Removes all cards from the deck.
                Returns None

            hide() :
                Sets the is_hidden attribute for each card in the deck to True.
                Returns None

            reset() :
                Removes all cards from the deck and replaces them with the 52 standard playing cards.
                Returns None

            reveal() :
                Sets the is_hidden attribute for each card in the deck to False.
                Returns None

            shuffle() :
                Randomizes the order of the cards in the deck.
                Returns None

        Other Behaviors
        ---------------
            Length :
                Passing a deck into the len() method will return the number of cards in the deck.

            Iteration :
                A deck object is interable and will interate over all cards held by the deck.

            Concatination :
                Two deck objects can be concatinated with the '+' operator. This returns a new deck.

                Example: new_collection = collection_a + collection_b

            Indexing :
                A deck can be indexed to acces a card at a specific index.

                Example: card = deck[2]

                Note: Indexing can only access cards and cannot add or modify cards.

            String :
                Passing a deck into the str() method will return a string describing every card
                in the deck.
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
