# Blackjack


## About this Project

The goal of this project was to write a functional blackjack program in python using OOP.

After I completed the cards.py project, I wanted to take everything a step further and create a functional program with classes. I decided that building on top of my previous project would be the simplest way to acomplish this goal, so I built a blackjack game that uses the cards.py project as a module.

# Blackjack
An exercise in object oriented programming

## About this Project

The goal of this project was to write a functional blackjack program in python using OOP.

After I completed the cards.py project, I wanted to take everything a step further and create a functional program with classes. I decided that building on top of my previous project would be the simplest way to acomplish this goal, so I built a blackjack game that uses the cards.py project as a module.

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


