# Blackjack-2.0
Version 2 of my blackjack game

From Version 1.0 Make a 'documentaion.md' file for all the documentaion. Now that it's been rewritten, it should be a lot easier to document.

## About this Project

The goal of this project was to write a functional blackjack program in python using OOP.

After I completed the cards.py project, I wanted to take everything a step further and create a functional program with classes. I decided that building on top of my previous project would be the simplest way to acomplish this goal, so I built a blackjack game that uses the cards.py project as a module.

# About the Code

This program has 3 modules. The cards module is taken directly from a my previous cards(link here) project with no change. The new classes defined in this program are documented here.

## The Hand Class
This class defines a player's hand for a game of blackjack. It extends the Collection class.

### *class* `Hand(cards=None, replacemet=False)`
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

This class includes all attributes of the Player class with the addition of a tern method.

#### `turn()`
Allows a human to take their turn. This method prints information about the game to the terminal then askes the player how they would like to procede. This method ends the player's turn if the player chooses to stay or if the player busts. Returns a bool to be handled by the game object. True if the player chooses to hit, False if the player chooses to stay.

## The Dealer Class
This class defines the dealer in blackjack. The dealer is fully automated by the game.

### *class* `Dealer()`

This class includes all attributes of the Player class with the addition of a tern method. The dealer's name is always `'The Dealer'`.

#### `turn()`
The dealer takes their turn based on the standard rules of blackjack. Returns a bool to be handled by the game object. True if the dealer hits (has a hand value less than 17). False if the dealer stays (has a hand value of 17 or more).

## The Game Class