# Documentation
This file describes the modules and classes defined in the blackjack package. For more information about running the program or playing the game, see the README.md file.

# Modules
This program contains 3 modules: cards, players, and game. 

The cards module is based on a my previous cards(link here) project with some modifications - mostly I used new techniques and skills that I learned since I first worte the original cards program. The cards module defines the Card, Collection, and Deck classes.

The players module has classes related to players of a game of blackjack. It includes the Hand, Player, HumanPlayer, and Dealer classes.

The game module has everything needed for the game of blackjack itself. The only class defined here is the Game class.

# Classes
The following describes each class defined in the blackjack package.

## The Card Class
This class represents a standard playing card and is defined in the cards module.

### *class* `Card(value, suit, is_hidden=False)`


#### Parameters
- **value** (int) - The value of the card. For a standard deck of playing cards, 1 is Ace, 11 is Jack, 12 is Queen, and 13 is King.
- **suit** (str) - The suit of the card. Generally, the four suits are `'Spades'`, `'Hearts'`, `'Diamonds'`, and `'Clubs'`.
- **is_hidden** (bool) - If `False` (the default), the card is 'faceup' and details about the card can be viewed (printed to the screen). If `True`, the card is 'facedown' and information about the card cannot be viewed.

#### Data Attributes
- **`value`** (int or None) - Returns the int value of the card. If `is_hidden` is True, returns None.
- **`suit`** (str or None) - Returns the suit of the card. If `is_hidden` is True, returns None.
- **`is_hidden`** (bool) - A repesentation of whether information about the card can be accessed. If set to True, the card is hidden or 'facedown' (no one can see the information). If False, the card is not hidden or 'faceup' and everyone can access information about the card. This attribute can only be changed with the `flip()` method.

#### Methods
- **`flip()`** - Changes the value of `is_hidden` to the opposite boolean value. This is like flipping a card over (from facedown to faceup). Returns None.

#### Other Behaviors
- **Comparison Operators** - Cards can be compared with the standard comparison operators (`==`, `<`, `>`, etc). Only the value of the card is used for comparisons.
- **`str()`** - Returns a string with information about the card in the form of `'{value} of {suit}'`. If `is_hidden` is True, returns the string `'This card is hidden.'` This allows a card object to be passed into the `print()` method.

#### Examples of card objects

```
>>>card_a = Card(4, 'Spades')
>>>print(card_a)
4 of Spades

>>>card_b = Card(12, 'Hearts')
>>>print(card_b)
Queen of Hearts

>>>card_b.flip() # changes is_hidden to True
>>>print(card_b)
This card is hidden.

>>>card_c = Card(8, 'Spades')
>>>card_a == card_b # 4 of Spades is not equal to Queen of Hearts
False

>>>card_a < card_b
True

>>>card_c = Card(4, 'Hearts')
>>>card_a == card_c # 4 of Spades is equal to 4 of Hearts
True
```


## The Collection Bass Class

This class is a base class for any object whose purpose is to hold cards, for example, a deck of playing cards or a player's hand in a card game.

### *class* `Collection(cards=None, replacement=False)`

This is the parent to the Deck and Hand classes, and is defined in the cards module.

#### Parameters
- **cards** (list or None) - A list of cards objects (or a single card object) to be placed in the collection at construction. If `None` (the default), then the collection object is initialized with an empty list to be filled with cards at a later time.
- **replacement** (bool) - Determines if cards are drawn from the collection with or without replacement. If `False` (the default), then cards are drawn without replacement. Cards are drawn with replacement if `replacement` is set to `True`. This cannot be changed after the collection object has been constructed.

#### Methods
- **`add(cards)`** - Adds a single card object or a list of card objects to the collection. This is similar to the `append()` method for a list. Returns None.

    Parameters
        - **cards** (Card or list) - The card or list of cards to be added to the collection.

- **`draw()`** - Returns a single card object from the collection.
    If replacement is `False`, the card is removed from the collection.
    If replacement is `True`, the card is NOT removed from the collection.
- **`discard()`** - Removes all cards from the collection. Returns None.
- **`hide()`** - Sets the is_hidden attribute for each card in the collection to True. Returns None.
- **`reveal()`** - Sets the is_hidden attribute for each card in the collection to False. Returns None.
- **`shuffle()`** - Randomizes the order of the cards in the collection - just like shuffling a deck of cards. Returns None.

#### Other Behaviors
- **Iteration** - A collection object is interable and will interate over all cards held by the collection.
- **Concatination** (The `+` operator) - Two collection objects can be concatinated with the '+' operator. This returns a new collection.
- **Indexing** - A collection can be indexed to acces a card at a specific index and also supports slicing. Indexing can only access cards and cannot add or modify cards.
- **`len()`** - Passing a collection into the `len()` method will return the number of cards in the collection.
- **`str()`** - Passing a collection into the str() method will return a string describing every card in the collection. This allows a colletion to be passed as an argument into the `print()` method.


### *class* `Deck(cards=None, replacement=False)`
A standard deck of 52 playing cards.

This class is defined in the cards module. It extends the `Collection` class, and includes all the attributes from its parent.

#### Parameters
- **cards** (list or None) - A list of card objects (or a single card object) to be placed in the deck at construction. If `None` (the default), then the deck object is initialized with the standard set of 52 playing cards.
- **replacement** (bool) - Determines if cards are drawn from the deck with or without replacement. If `False` (the default), then cards are drawn without replacement. Cards are drawn with replacement if `replacement` is set to `True`. This cannot be changed after the deck object has been constructed.

#### Methods
This section only details the methods defined in the Deck class. Other supported methods are defined in the `Collection` class.

- **`reset()`** - Resets the deck back to the original 52 playing cards. Returns None.

### *class* `Hand()`
A player's hand in a game of blackjack. 

This class is defined in the players module. It extends the `Collection` class, and includes all the attributes from its parent. For other supported methods, see the `Collection` class.

#### Parameters
The Hand class takes no parameters and is always empty at construction.

#### Data Attributes
- **`value`** (int) - The value of the hand as determined by the rules of blackjack. Face cards are woth 10 points, Aces are worth 11 or 1 point, etc. 

### Examples of Collection Objects

```
>>> deck_a = Deck() # a new deck is created with 52 card objects
>>> len(deck_a)
52

>>> print(deck_a) # prints all the cards in the deck
Ace of Spades
2 of Spades
3 of Spades
...
10 of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs

>>> deck_a.shuffle() # the deck can be shuffled
>>> print(deck_a)
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
>>> print(deck_c) # The cards from deck_b are still hidden
This card is hidden.
This card is hidden.
7 of Spades
This card is hidden.
...
8 of Spades
4 of Spades
This card is hidden.
This card is hidden.

>>> hand = Hand() # a hand object
>>> hand.add(Card(4, 'Hearts')) # cards can be added to a collection one at a time
>>> hand.add([Card(5, 'Clubs'), Card(1, 'Spades')]) # or a list of cards can be added

>>> for num, card in enumerate(hand): # collections are iterable
...     print(f'Card {num+1} is the {card}')
... 
Card 1 is the 4 of Hearts
Card 2 is the 5 of Clubs
Card 3 is the Ace of Spades

>>> hand.value # the ace is worth 11 points
20

>>> hand.add(Card(6, 'Diamonds')) # adding a 6 of Diamonds
>>> hand.value # now the ace is worth 1 point
16
```

## The Player Base Class
A base class for blackjack players. Contains attributes relevent to both human players and the dealer.

### *class* `Player(name)`
A blackjack player. The base class for the Dealer and HumanPlayer classes.

#### Parameters
- **name** (str) - The name of the player.

#### Data Attributes
- **`had_turn`** (bool) - Returns `False` if the player has not taken their turn and `True` if the player has taken their turn.
- **`hand`** (Hand) - The player's blackjack hand. 
- **`name`** (str) - The player's name.

#### Methods
- **`begin_trun()`** - Called at the beginning of a palyer's turn by the Game object. This method is required for the Game object, but it doesn't have to do anything. Returns None.
- **`clean_up()`** - Empties the player's hand and sets 'had_turn' to False. Called by the Game object at the end of a game. Returns None
- **`decision()`** - Allows the player object to 'hit' or 'stay' in a game of blackjack. Should return `True` if the player chooses to 'hit' and `False` if the player chooses to 'stay'.

### *class* `HumanPlayer(name)`
Defines a class that allows a human to play a game of blackjack. This class extends the Player class. For other supported attribues and methods, see the `Player` class.

#### Parameters
- **name** (str) - The name of the human player.

#### Methods
- **`begin_trun()`** - Called at the beginning of a palyer's turn by the Game object. This method doesn't do anything for a human player. Returns None.
- **`decision()`** - Using the terminal, this methods asks the human if they would like to 'hit' or 'stay', collects input from the human, and communicates the decision with the game object. Returns `True` if the human chooses to 'hit' and `False` if the human chooses to 'stay'.

### *class* `Dealer()`
This class defines the dealer in blackjack and extends the `Player` class. The dealer is fully automated by the game. For other supported attribues and methods, see the `Player` class.

#### Parameters
    The dealer class take no arguments at construction. The name of the a dealer object is `'The Dealer'`.

#### Methods
- **`begin_trun()`** - Reveals any hidden cards in the dealer's hand. Called by the game object at the begining of the dealer's turn. Returns None.
- **`decision()`** - Determines if the dealer should hit or stay using the standard rules of blackjack. Returns True if the dealer hits (hand value of less than 17). Returns False if the dealer stays (hand value of 17 or more).

This class includes all attributes of the Player class with the addition of a tern method. The dealer's name is always `'The Dealer'`.

## The Game Class
Represents a game of blackjack. A game object handles all interactions in blackjack. The game shuffles the deck, deals the cards to all palyers, allows the players (including the dealer) to take their turn, and discards all player hands at the end of the game. Opptionally, the game object prints a summary at each step of blackjack.

For more about starting or playing a game of blackjack, see the README.md file.

### *class* `Game(*players, summary=True)`

#### Parameters
- **\*players** (Player or list) - The player or list of players to play the game of blackjack.
- **summary** (bool) - If True (the default), the game will print a summary of what's happening in the game. If False, the game will run without printing anything to the terminal.

#### Notes
ALL players MUST have the following methods.
- `begin_turn()`

    This is called at the begining of a player's turn. Not all player's need to do something here, but for example, the dealer needs to reveal any hidden cards at the begining of their turn.

- `decision()`

    This is called when the player needs to choose to hit or stay and might be called several times during thier turn.

- `clean_up()`

    Called at the end of the game. Generally, the player dicards their hand and had_turn is set to False in
    in preparation for their turn.

The game also assumes the following
- Player objects have a `'name'` represented as a string
- Players have a `Hand` object with a `value` attribute and a `add()` method