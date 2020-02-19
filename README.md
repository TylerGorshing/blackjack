# Blackjack
An exercise in object oriented programming.

## About this Project

The goal of this project was to write a functional program in python using OOP.

After I completed the cards.py project, I wanted to take everything a step further and create a functional program with classes. I decided that building on top of my previous project would be the simplest way to acomplish this goal, so I built a blackjack game that uses a modified and updated version of my cards.py project as a module.

Documentaion for this program can be found in the DOCUMENTAION.md file.

## Running the Program
Running the program requires Python 3.7 or later. The program can be launched from the from terminal by navigated to the directory contaning the blackjack package and entering the following command:

`python -m blackjack`

The `-m` flag tell python to run the package as a script using `__main__` module in the package. Upon launch, the program will first ask how many humans are playing.

```
How many human players are playing? 
2
What is the name of player 1? 
Alice
What is the name of player 2? 
Bob
```

After collecting information from the user, the program starts a game of blackjack by creating a game object with the human players. Because the game object is callable the program simply calls `game()` to start a new game.

The program will print all the cards of each player, but only one card from the dealer's hand revealing just as much information to each player as a real game of blackjack. Then player 1 (Alice), can take their turn.

```
----- New Game! -----


----- The Dealer -----
This card is hidden.
8 of Spades



----- Alice with 9 -----
3 of Diamonds
6 of Diamonds



----- Bob with 21 -----
Ace of Spades
King of Diamonds

```

Alice takes her turn by entering "hit" or "stay". The program can identify if something other than "hit" or "stay" is entered and handles the situation appropriately. Alice continues to take her turn until she busts or chooses to stay.



```
----- Alice with 9 -----
3 of Diamonds
6 of Diamonds

Enter "hit" or "stay". 
hello

You must type "hit" or "stay".
Enter "hit" or "stay". 
 
hit
Alice hits.

3 of Diamonds
6 of Diamonds
2 of Clubs


Alice has 11.

Enter "hit" or "stay". 
hit
Alice hits.

3 of Diamonds
6 of Diamonds
2 of Clubs
7 of Diamonds


Alice has 18.

Enter "hit" or "stay". 
hit
Alice hits.

3 of Diamonds
6 of Diamonds
2 of Clubs
7 of Diamonds
8 of Hearts


Alice has 26.

Alice busts!
```

When Alice's turn is over, player 2 (Bob) begins their turn.

 ```
----- Bob with 21 -----
Ace of Spades
King of Diamonds

Enter "hit" or "stay". 
stay
Bob stays with 21.

```

When all the humans have completed their turns, the dealer takes a turn following the standard rules of blackjack. A summery of the game is then printed to the screen, and the players are given the option of playting another round.

```
----- The Dealer with 18 -----
Queen of Spades
8 of Spades

The Dealer stays with 18.



----- Final Results -----


----- Alice Busts! -----


----- Bob Wins! -----
Another round? Y/N

```


