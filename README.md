# Blackjack
An exercise in object oriented programming

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



## Running the Program

The code can be run from the terminal by navigating to the appropriate directory. Upon launch, the program will start by asking for the number of human players then ask for the name of each player.

```
How many human players are playing? 
2
What is the name of player 1? 
Alice
What is the name of player 2? 
Bob
```

After collecting information from the user, the program starts a game of blackjack by calling the Game.round() method. This method deals cards to all the players and the dealer, prints the all the relavent information to the screen, then begins the first player's turn.

The program will print all the cards of each player, but only one card from the dealer's hand revealing just as much information to each player as a real game of blackjack.

```
  ----- New Game ----- 
 

The Dealer:
This card is hidden.
4 of Hearts


Alice with a hand value of 12:
Jack of Diamonds
2 of Spades


Bob with a hand value of 15:
10 of Diamonds
5 of Clubs


---------- Alice with a hand value of 12. ---------- 

Jack of Diamonds
2 of Spades
Enter "hit" or "stay". 
```

 At this point, Alice takes her turn by entering "hit" or "stay". The program can identify if something other than "hit" or "stay" is entered and handles the situation appropriately. 

```
---------- Alice with a hand value of 12. ---------- 

Jack of Diamonds
2 of Spades
Enter "hit" or "stay". 
hit
 
Alice hits and has a hand value of 17
Jack of Diamonds
2 of Spades
5 of Diamonds
Enter "hit" or "stay". 
run away

You must type "hit" or "stay".
Enter "hit" or "stay". 
stay
 
Alice stays with a hand value of 17 
```

 Alice's turn is over when she chooses to stay or if her score exceeds 21. When Alice's turn is over, Bob begins his turn.

 ```
 ---------- Bob with a hand value of 15. ---------- 

10 of Diamonds
5 of Clubs
Enter "hit" or "stay". 
hit
 
Bob hits and has a hand value of 18
10 of Diamonds
5 of Clubs
3 of Diamonds
Enter "hit" or "stay". 
hit
 
Bob hits and has a hand value of 27
10 of Diamonds
5 of Clubs
3 of Diamonds
9 of Spades
Bob has busted! 
```

When all the humans have completed their turns, the dealer takes a turn following the standard rules of blackjack. A summery of the game is then printed to the screen, and the players are given the option of playting another round.

```
---------- The Dealer with a hand value of 15. ---------- 

Ace of Spades
4 of Hearts
 
The Dealer hits and has a hand value of 15
Ace of Spades
4 of Hearts
King of Hearts
 
The Dealer hits and has a hand value of 22
Ace of Spades
4 of Hearts
King of Hearts
7 of Hearts
The Dealer has busted! 
 


 
 ----------Outcome---------- 
 

----- The Dealer has busted! -----
Ace of Spades
4 of Hearts
King of Hearts
7 of Hearts


----- Alice has a hand value of 17. -----
Jack of Diamonds
2 of Spades
5 of Diamonds


Alice has won! 

----- Bob has busted! -----
10 of Diamonds
5 of Clubs
3 of Diamonds
9 of Spades


Bob has lost. 

Another round? Y/N
```


