# Documentation
This file describes the modules and classes defined in the blackjack package. For more information about running the program or playing the game, see the README.md file.

# Modules
This program contains 3 modules: cards, players, and game. 

The cards module is based on a my previous cards(link here) project with some modifications -- mostly I used new techniques and skills that I learned since I first worte the original cards program. The cards modules defines the Card, Collection, and Deck classes.

The players module has classes related to players of a game of blackjack. It includes the Hand, Player, HumanPlayer, and Dealer classes.

The game module has everything needed for the game of blackjack itself. The only class defined here is the Game class.

# Classes
The following describes the classes defined in the blackjack package.

## The Card Class
This class represents a standard playing card. The card can be hidden from view if needed.

### *class* `Card(value, suit, is_hidden=False)`

Defined in the cards module

#### Parameters
- **value** (int) - The value of the card. For a standard deck of playing cards, 1 is Ace, 11 is Jack, 12 is Queen, and 13 is King.
- **suit** (str) - The suit of the card. Generally, the four suits are `'Spades'`, `'Hearts'`, `'Diamonds'`, and `'Clubs'`.
- **is_hidden** (bool) - If `False` (the default), the card is 'faceup' and details about the card can be viewed (printed to the screen). If `True`, the card is 'facedown' and information about the card cannot be viewed.

#### Data Attributes
- **`value`** (int or None) - Returns the int value of the card. If `is_hidden` is True, returns None.
- **`suit`** (str or None) - Returns the suit of the card. If `is_hidden` is True, returns None.
- **`is_hidden`** (bool) - A repesentation of whether information about the card can be accessed. If set to True, the card is hidden or 'facedown' (no on can see the information). If False, the card is not hidden or 'faceup' and everyone can access information about the card. This attribute can only be changed with the `flip()` method.

#### Methods
- **`flip()`** - Changes the value of `is_hidden` to the opposite boolean value. This is like flipping a card over (from facedown to faceup). Returns None

#### Other Behaviors
- **Comparison Operators** - Cards can be compared with the standard comparison operators (==, <, >, etc). Only the value of the card is used for comparisons.

```
>>>Card(4, 'Spades') == Card(8, 'Spades')
False
>>>Card(4, 'Spades') == Card(4, 'Hearts')
True
```

- **`str()`** - Returns a string with information about the card in the form of `'{value} of {suit}'`. If `is_hidden` is True, returns the string `'This card is hidden.'` This allows a card object to be passed into the `print()` method.

```
>>>card_a = Card(4, 'Spades')
>>>print(card_a)
4 of Spades

>>>card_b = Card(12, 'Hearts')
>>>print(card_b)
Queen of Hearts
>>>card_b.flip() # changed is_hidden to True
>>>print(card_b)
This card is hidden.
```

## The Collection Class

This class is a parent class for any object whose purpose is to hold cards, for example, a deck of playing cards or a player's hand in a card game.

### *class* `Collection(cards=None, replacement=False)`

An object for a collection of cards. This is the base class for Deck and Hand.

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

Parameters: 
- **cards** (list or None) - A list of playing cards held by the Collection object. If `None` (the default), then the Collection object is initialized with an empty list to be filled with cards at a later time.
- **replacement** (bool) - Determines if cards are drawn from the collection with or without replacement. If `False` (the default), then cards are drawn without replacement. Cards are drawn with replacement if `replacement` is set to `True`.

#### `cards`
A list of playing card objects. 

#### `discard()`
Empties the `cards` list. If there are no more references to any of the card objects, I think they're garbage collected by python.

#### `draw()`
Returns a card object from the `cards` list. If `replacement` is set to `False`, the first card object in the `cards` list is removed and that card is returned. If `replacement` is set to `True`, a random card in the `cards` list is returned *without* removing it from the list.

#### `hide()`
Sets the `hidden` attribute for every card in the `cards` list to `True`.

#### `reveal()`
Sets the `hidden` attribute for every card in the `cards` list to `False`.

#### `show()`
Prints information about each card object in the `cards` list. This calls the `show()` method on each card object.

#### `shuffle()`
Randomizes the order of the `cards` list. This is like shuffling a deck of cards.

### Other Notes
This class also defines the `len()` magic method as well as the `+` operation. See the Deck class for examples. 

## The Deck Class

A standard deck of 52 playing cards. This class extends the `Collection` class, and includes all the attributes from its parent.

### *class* `Deck(cards=None)`

A deck of standard playing cards. Extends the Collection Class.

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

Parameters:
- **cards** (list or None) - A list of playing cards to be placed in the Deck at construction. If `None` (the default), the deck is constructed with the standard set of 52 playing cards.

#### `build()`
Adds the 52 standard playing card objects to the deck *without* removing any cards already in the deck. To remove the cards already in the deck, see the `reset()` method. This method is called at construction of a new deck object if the `cards` parameter is `None`.

#### `reset()`
Resets the deck object to a standard deck of 52 playing cards. This removes all card objects from the deck then fills the empty deck with 52 playing cards.

### Examples
```
>>> from cards import *
>>> deck_a = Deck() # the deck object starts with 52 playing cards
>>> len(deck_a)
52

>>> deck_a.show()
Ace of Spades
2 of Spades
3 of Spades
...
10 of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs

>>> deck_a.shuffle() # the deck can be shuffled
>>> deck_a.show()
6 of Clubs
8 of Diamonds
7 of Hearts
3 of Spades
...
10 of Hearts
4 of Spades
6 of Spades
3 of Clubs

>>> deck_b = Deck()
>>> deck_b.hide() # all the cards in a deck can be hidden
>>> deck_b.show()
This card is hidden.
This card is hidden.
...
This card is hidden.
This card is hidden.

>>> deck_c = deck_a + deck_b # adding two decks together returns a third deck
>>> len(deck_c)
104

>>> deck_c.shuffle()
>>> deck_c.show() # The cards from deck_b are still hidden
This card is hidden.
This card is hidden.
7 of Spades
This card is hidden.
...
8 of Spades
4 of Spades
This card is hidden.
This card is hidden.
```


## The Hand Class
This class defines a player's hand for a game of blackjack. It extends the Collection class.

### *class* `Hand(cards=None, replacemet=False)`

A player's hand in a game of blackjack. Extends the Collection Class. A hand instance is
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


Parameters: 
- **cards** (list or None) - A list of playing cards held by the Collection object. If `None` (the default), then the Collection object is initialized with an empty list to be filled with cards at a later time.
- **replacement** (bool) - Determines if cards are drawn from the collection with or without replacement. If `False` (the default), then cards are drawn without replacement. Cards are drawn with replacement is replacement is set to `True`.

#### `cards`
A list of playing card objects. These are the cards in the player's hand.

#### `value`
Returns the integer value of the hand as determined by the rules of blackjack. Face cards are worth 10 points. Aces are worth 1 point or 11 points — whichever gets the value closest to 21 without going over. For example, if a hand consist of a 3 and two aces, `value` will return 15 (3+1+11).

#### `num_aces`
Returns an integer number of aces in the hand.

## The Player Class
A base class for blackjack players. Contains attributes relevent to both human players and the dealer.








### *class* `Player(name)`
Parameters:
- name (str) - The name of the player.

A blackjack player. The base class for the Dealer and HumanPlayer classes.

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

#### `busted`
Returns a bool. True of the player's hand value exceeds 21. False otherwise.

#### `clean_up()`
Called at the end of a game of blackjack. This method empties the player's hand and sets `completedTurn`, `won`, `lost`, and `busted` to False in preparation for a new game of blackjack.

#### `completedTurn`
Returns a bool. False if the player hasn't had their turn yet. True otherwise.

#### `hand`
Hand object. This is the players hand for a game of blackjack.

#### `hadBlackjack`
Returns a bool. True if they player's hand value is *exactly* 21. False otherwise.

#### `lost`
Retuns a bool. True if the player has not busted *and* was beated by the dealer. False if the player has busted or if the player beat the dealer. Also returns False if they player hasn't had their turn.

#### `name`
Returns a string. The player's name

#### `won`
Returns a bool. True if the player has completed thier turn, beaten the dealer, *and* has not busted. False otherwise.






## The HumanPlayer Calss
Defines a class that allows a human to play a game of blackjack. This class extends the Player class.

### *class* `HumanPlayer(name)`
Parameters:
- **name** (str) - The name of the human player.

Allows a human user to interact with a game of blackjack. Extends the Player class.

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

This class includes all attributes of the Player class with the addition of a tern method.

#### `turn()`
Allows a human to take their turn. This method prints information about the game to the terminal then askes the player how they would like to procede. This method ends the player's turn if the player chooses to stay or if the player busts. Returns a bool to be handled by the game object. True if the player chooses to hit, False if the player chooses to stay.






## The Dealer Class
This class defines the dealer in blackjack. The dealer is fully automated by the game.

### *class* `Dealer()`


The dealer in a game of Blackjack. Inherits from the Player class.

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

This class includes all attributes of the Player class with the addition of a tern method. The dealer's name is always `'The Dealer'`.

#### `turn()`
The dealer takes their turn based on the standard rules of blackjack. Returns a bool to be handled by the game object. True if the dealer hits (has a hand value less than 17). False if the dealer stays (has a hand value of 17 or more).

## The Game Class
Represents a game of blackjack.

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
