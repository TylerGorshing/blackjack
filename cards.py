'''
This is a program for a game of blackjack.

This program allows human players to play blackjack using a
command line interface. To play a game, simply run the cards.py file
using Python 3. The terminal will promt the user for all necessary input.

'''

import random


class Card():
    '''A class for playing cards

        Parameters
        ----------
            value : int
                The value of a card. 1 is Ace. 11 is Jack. 12 is Queen. 13 is King.

            suit : str
                The suit of the card. Generally 'Spades', 'Hearts', 'Diamonds', or 'Clubs'.

        Attributes
        -----------
            value : int
                The value of a card. 1 is Ace. 11 is Jack. 12 is Queen. 13 is King.

            suit : str
                The suit of the card. Generally 'Spades', 'Hearts', 'Diamonds', or 'Clubs'.
    '''

    def __init__(self, value: int, suit: str):

        self._value = lambda self: value
        self._suit = lambda self: suit

    @property
    def value(self):
        return self._value(self)

    @property
    def suit(self):
        return self._suit(self)

    def show(self):
        '''Prints the value and suit of the Card object.'''

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


class Collection():
    '''The parent class for a deck of cards or a player's hand.

    Atributes
    ----------
        cards : list
            A list of the Card objects in the collection.
    '''

    def __init__(self):

        self.cards = []

    def show(self):
        '''Prints the value and suit of each card in the collection.'''

        for card in self.cards:
            card.show()

    def shuffle(self):
        '''Randomizes the order of the collection of cards.'''

        random.shuffle(self.cards)

    def add_card(self, card):
        '''Adds a given card to the collection.

        The Method can be used along with the remove_card()
        method to draw a card from one collection and add that card to a
        different collection.

        Parameters
        -----------

            card : Card object
                The card object to be added to the collection.
        '''

        self.cards.append(card)

    def remove_card(self) -> Card:
        '''Removes a Card object from a collection and returs that card.

        Returns
        -------
            Card
                The first card in the cards attribute
        '''

        return self.cards.pop(0)

    def discard(self):
        '''Empties the entire collection

        This method sets the cards attribute to an empty list.
        '''

        self.cards = []

    def random_card(self) -> Card:
        '''Returns a random card from the Collection object WITH replacement.

        Returns
        -------
            Card

        Note
        ----
            The collection is unchanged after calling this function. It's similar to
            drawing a card and replacing the same card back into the Collection.

        '''
        return random.choice(self.cards)

    @property
    def size(self) -> int:
        ''' int : The number of cards in `cards`.'''

        return len(self.cards)

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        self.cards += other.cards
        return self


class Deck(Collection):
    ''' A deck of standard playing cards.

    A freshly initialized Deck object consists of 52 Card objects with the
    standard suits and values. This can be used as a deck of cards to
    play various games.

    Inharets from the Collection Class.'''

    def __init__(self):

        super().__init__()
        self.build()

    def build(self):
        '''Creats the 52 cards in the Deck

        Note
        ----
            This method only adds cards. It does not remove cards from the deck. To remove cards,
            the discard() method should be called from the parent class
        '''

        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))


class Hand(Collection):
    '''A player's Blackjack hand.

    Inharets from the Collection class.'''

    @property
    def value(self) -> int:
        '''int : The value of a hand as determined by the rules of blackjack.'''

        value_list = [10 if card.value > 10
                      else card.value for card in self.cards]
        hand_value = sum(value_list)

        while value_list.count(1) > 0 and (21 - hand_value) >= 10:
            value_list[value_list.index(1)] = 11
            hand_value = sum(value_list)

        return hand_value

    @property
    def num_aces(self):
        '''int : The number of aces in a hand'''

        return [card.value for card in self.cards].count(1)


class Player():
    '''
    A blackjack player.

    The is the parent class for a human player and the dealer. It includes
    methods and attributes relevent to both kinds of players.

    Parameters
    -----------
        name : str
            The player's name.

    Attributes:
    -----------

        hand : Hand
            A Hand object to hold the player's cards.

        name : str
            The name of the player.

        had_turn : bool
            If False, the player has NOT had their turn yet.
    '''

    def __init__(self, name: str, summary=True):

        self.hand = Hand()
        self.name = name
        self.had_turn = False
        self.summary = summary

    def draw(self, collection, number_of_cards: int = 1):
        '''
        Draws a card from a specified collection object and adds it to the players hand.

        Parameters
        -----------

            collection : Collection
                The collection to draw from. Generally, the Deck object being used in the game.

            number_of_cards : int (Defaults to 1)
                Specifies the number of cards to be drawn from the given collection.
                Defaults to 1 card.
        '''

        for _ in range(number_of_cards):
            self.hand.add_card(collection.remove_card())

    def replacement_draw(self, collection, number_of_cards=1):
        '''
        Draws a card from a given collection WITH replacement.

        This method doesn't remove a card from the collection.
        It returns a copy of a random card in the collection.
        '''

        for _ in range(number_of_cards):
            self.hand.add_card(collection.random_card())

    def show_hand(self):
        '''Prints all the cards in the players hand.
    `   '''

        for card in self.hand.cards:
            card.show()

    def hit(self, deck):
        '''The "hit" action in a game of blackjack.

        Draws a card from the specified deck and adds it to the specified hand. Prints a summary
        and results of the action including all the cards in the player's
        hand and the total value of the hand.

        Parameters:
        -----------

        deck:
            The Deck object the player will draw from. Generally,
            the deck object being used in the game of blackjack the player is playing.
        '''

        if self.had_turn:  # checks to see if the player has had their turn.
            if self.summary:
                print(f'{self.name} has already had thier turn.', '\n')
        else:
            self.draw(deck)
            if self.summary:
                self.show_hand()
                print(f"{self.name}'s hand value is {self.hand.value}", '\n')

        if self.hand.value > 21:  # Checks to see if the player has busted.
            # If they player busts, their turn is ended.
            self.had_turn = True

    def stay(self):
        '''
        The "stay" action in a game of blackjack ending the player's turn.
        '''

        if self.summary:
            print(f'{self.name} stays with a hand value of {self.hand.value}', '\n')
        self.had_turn = True

    def reset(self):
        '''
        Resets the player for a new game.

        The method empties the player's hand and sets self.had_turn to False.
        '''
        self.hand.discard()
        self.had_turn = False


class HumanPlayer(Player):
    '''
    A class for a human player.

    The user intereacts with the game through the terminal.

    Inheriates from the Player class.
    '''

    def turn(self, deck):
        '''
        A method allowing the user to take thier turn using the terminal.

        This method prints instructions for the user and askes the user
        what action they would like to take.
        turn() prints information to the terminal for the user to make game decisions.

        Parameters:
        -----------
            deck : Deck object
                The deck being used for the game of blackjack being played.

        User Input:
        -----------
            This method askes the user for input.

            hit:
                Shows the user has decicded to hit.
                Calls the hit() method in the parents class.

            stay:
                Shows the user has decided to stay.
                Calls the stay() method in the parent class.
        '''

        if self.had_turn:  # checks to see if the user has had their turn.
            print(f'{self.name} has already had their turn.')
            return None

        print('\n', f"\n-----{self.name}'s Turn-----")
        print(f"{self.name}'s hand:")
        self.hand.show()
        print(f"{self.name}'s hand value is {self.hand.value}", '\n')

        # Allows the user to continue until choose "stay" or they bust.
        while not self.had_turn and self.hand.value <= 21:
            print(f'What would {self.name} like to do? Hit or Stay?')
            move = input().strip().lower()
            if move == 'hit':
                self.hit(deck)
            elif move == 'stay':
                self.stay()
            else:
                print("Please enter 'Hit' or 'Stay'.")  # Humans are dumb.

        if self.hand.value > 21:
            print(f'{self.name} has busted!')


class Dealer(Player):
    '''
    The dealer for a game of blackjack.

    The dealer's name is 'The Dealer'. A Dealer object also has a hidden
    card that the player cannot see and a special turn sequence
    as defined by the rules of blackjack.

    Inherits fro the Player class.
    '''

    def __init__(self, summary=True):
        '''
        Initilizes the Dealer object.

        Parameters:
        -----------
            summary: bool
                Defaults to True
                If summer is true, a summary of the dealer's turn is printed to the terminal.

        Atrributes:
        -----------
            self.name is always 'The Dealer'

            self.hidden_card: bool
                True if a card is hidden from the player. When the dealer starts their turn,
                the dealer flips the card, and self.hidden_card is changed to false.

            self.summary: bool
                If summer is true, a summary of the dealer's turn is printed to the terminal.
        '''
        Player.__init__(self, 'The Dealer')
        self.hidden_card = True
        self.summary = summary

    def show_hand(self):
        '''A special show_hand() method for the dealer that hides
        the hidden card if self.hidden_card is Ture.'''

        if self.hidden_card:
            secret_card = self.hand.cards.pop(0)

        Player.show_hand(self)

        if self.hidden_card:
            self.hand.cards.insert(0, secret_card)

    @property
    def up_card(self):
        '''Returns the first card that is visable to other players.'''

        return self.hand.cards[1]

    def show_hidden_card(self):
        '''
        Reveals the deal's hidden card.

        This changes self.hidden_card to False and prints all the dealer's cards to the terminal.
        '''

        if self.hidden_card:
            self.hidden_card = False
        if self.summary:
            self.show_hand()

    def turn(self, deck):
        '''
        The sequence of actions for the dealer's turn.

        This follows the standard rules of blackjack:
        The dealer reveals their hidden card. Then the dealer hits below 17,
        and stays at 17 or above.
        The method also prints a summars of actions to the terminal for any users.
        '''

        if self.had_turn:
            if self.summary:
                print('The Dealer has already had thier turn. The game is over.')
            return None

        if self.summary:
            print(f"-----{self.name}'s Turn-----")
            print(f"{self.name}'s hand with a value of {self.hand.value}:")
            self.show_hidden_card()

        while self.hand.value < 17:  # The dealer must hit if their hand value is less than 17
            if self.summary:
                print(f'{self.name} hits.')
            self.hit(deck)

        if self.hand.value > 21:
            if self.summary:
                print('The dealer has busted!', '\n')

        self.stay()


class Game():
    '''
    A game of blackjack.

    This is the Game object. It has everything needed for a game of blackjack:
    a group of players, a dealer, a deck, a game sequence, and a summary at the end of the game.
    '''

    def __init__(self, *players, summary=True):
        '''
        Initializes the Game object.

        Takes the players and creats a Dealer object and a Deck object.

        Parameters:
        -----------
            *players: HumanPlayer objects
                Accepts any number of human players for a game.
                Caution! A Game object only creats a single Deck object with
                52 cards. Only a handful of players can play before the deck runs out of cards.

            summary: bool
                Defaults to true.
                If summary is true, and summary of the events
                of the game if printed to the terminal.

        Attriburtes:
        ------------
            self.dealer: Dealer object
                The dealer for the game of blackjack. The dealer has a hand with a
                hiden card and takes thier own turn.

            self.deck: Deck object
                A standard 52 card deck that is used to deal cards to the players.

            self.summary: bool
                If self.summary is true, and summary of the events
                of the game if printed to the terminal.
        '''

        self.players = players
        self.summary = summary
        self.dealer = Dealer(summary=self.summary)
        self.deck = Deck()

    def round(self):
        '''
        The sequence of the actions for a game of blackjack.

        This method is simply calls other class methods in game order.
        '''
        if self.summary:
            print('\n', '-----New Game-----')
        self.deal()
        self.player_turns()
        self.dealer.turn(self.deck)
        if self.summary:
            self.outcome()
        self.reset_players()

    def players_discard(self):
        '''
        Empties all the human players' hands.

        This is called at the end of each
        round to ensure the players empty their hand.
        '''

        for player in self.players:
            player.hand.discard()

    def deal(self):
        '''
        Shuffles the deck and deals the cards to the players including the dealer.

        Once the game is finished dealing, a summary of all the visible
        cards (ALL the human players's cards and one of the dealer's cards) are
        printed along with the value of each human's hand.

        Note:
        -----
            This DOES NOT follow standard blackjack deal order. In this case,
            the dealer is delt two Card objects. Then, each player is delt two
            card objects in the order they intered the game.
        '''

        self.deck.shuffle()

        self.dealer.draw(self.deck, number_of_cards=2)

        for player in self.players:
            player.hand.discard()  # For extra redundency or something.
            player.draw(self.deck, number_of_cards=2)

        if self.summary:
            print('The Dealer:')
            self.dealer.show_hand()  # Shows only the visible card.
            print('\n')

            for player in self.players:
                print(f'{player.name} with a hand value of {player.hand.value}:')
                player.show_hand()
                print('\n')

    def player_turns(self):
        '''
        Allows each player to take their turn in the game.
        '''

        for player in self.players:
            player.turn(self.deck)

    def outcome(self):
        '''
        Prints the results of the game: who's won, lost, or busted.
        '''
        print('Results:')

        for player in self.players:
            if player.hand.value > 21:
                print(f'{player.name} busted.')
            elif self.dealer.hand.value > 21:
                print(f'{player.name} has beat the dealer')
            elif self.dealer.hand.value > player.hand.value:
                print(f'{player.name} has lost')
            else:
                print(f'{player.name} has won!')

    def reset_players(self):
        '''
        Resets each player and the dealer in preparation for a new game.
        '''

        for player in self.players:
            player.reset()
        self.dealer.reset()


def main():
    '''The main function - only called if __name__ == __main__.'''

    print('How many human players are playing?')
    number = int(input())

    players = []

    for i in range(number):
        print(f'What is the name of player {i+1}?')
        name = input()
        players.append(HumanPlayer(name))

    game = Game(*players)

    game.round()

    while True:
        print('Another round? Y/N')
        answer = input().strip().lower()
        if answer == 'y':
            game.round()
        else:
            break


if __name__ == '__main__':
    main()
