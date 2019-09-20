'''
This is a program for a game of blackjack.

This program allows human players to play blackjack using a
command line interface. To play a game, simply run the cards.py file
using Python 3. The terminal will promt the user for all necessary input.

'''

import random


class Card():
    '''A class of playing cards

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

    def __init__(self, value: int, suit: str, hidden=False):

        self._value = value
        self._suit = suit
        self._hidden = hidden

    @property
    def value(self):
        if not self._hiden:
            return self._value
        else:
            return None

    @property
    def suit(self):
        if not self._hidden:
            return self._suit
        else:
            return None

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):

        if hidden.__class__ != bool:
            raise TypeError('Must be bool type.')
        self._hidden = hidden
        return self

    def changeHidden(self, hidden=None):
        if hidden is None:
            self._hidden = not self._hidden
            return self

        if hidden.__class__ == bool:
            self._hidden = hidden
            return self
        else:
            raise TypeError("Must be bool type.")

    def show(self):
        '''Prints the value and suit of the Card object.'''

        if self.hidden:
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

    #######################################
    '''
    Ordering functions:

        These functions define an order on the cards. Note, the order depends entirely
        on the value of the card and nothing else. Bacause of this, two cards are equal
        if they have the same value but not necessarly the same suit.

        Card(4, 'Spades') == Cards(4, 'Hearts') # This will return true

    '''

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

    def __init__(self, cards=[], replacement=False):
        self.cards = cards
        self.replacement = replacement

    def shuffle(self):
        '''Randomizes the order of the collection of cards.'''

        random.shuffle(self.cards)

    def show(self):
        '''Prints the value and suit of each card in the collection.'''

        for card in self.cards:
            card.show()

    def discard(self):
        '''Empties the entire collection

        This method sets the cards attribute to an empty list.'''

        self.cards = []

    def draw(self, replacement=None):
        if replacement is None:
            replacement = self.replacement

        if replacement:
            return random.choice(self.cards)
        else:
            return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):

        return type(self)(cards=self.cards + other.cards)


class Deck(Collection):
    ''' A deck of standard playing cards.

    A freshly initialized Deck object consists of 52 Card objects with the
    standard suits and values. This can be used as a deck of cards to
    play various games.

    Inharets from the Collection Class.'''

    def __init__(self, cards=[]):

        super().__init__(cards)
        if cards == []:
            self.build()

    def build(self):
        '''Creats the 52 cards in a standard deck of playing cards.

        Note
        ----
            This method only adds cards. It does not remove cards from the deck. To remove cards,
            the discard() method should be called from the parent class
        '''

        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def reset(self):
        '''Resets the deck to the original state: 52 standard playing cards.'''

        self.discard()
        self.build()


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
    def num_aces(self) -> int:
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

        completedTurn : bool
            If False, the player has NOT had their turn yet.
    '''

    def __init__(self, name: str):

        self.hand: Hand = Hand()
        self.name: str = name
        self.completedTurn: bool = False
        self.lost: bool = False
        self.won: bool = False
        self.busted: bool = False

    @property
    def hasBlackjack(self) -> bool:
        if self.hand.value == 21:
            return True
        else:
            return False

    def showHand(self) -> None:
        for card in self.hand.cards:
            card.hidden = False

    def hideHand(self) -> None:
        for card in self.hand.cards:
            card.hidden = True

    def newSetup(self) -> None:
        '''
        Resets the player for a new game.

        The method empties the player's hand and sets self.completedTurn to False.
        '''
        self.hand.discard()
        self.completedTurn = False
        self.lost = False
        self.won = False
        self.busted = False


class HumanPlayer(Player):
    '''
    A class for a human player.

    The user intereacts with the game through the terminal.

    Inheriates from the Player class.
    '''

    def __init__(self, name):
        super().__init__(name)

    def turn(self):

        while True:
            decision = input('Enter "hit" or "stay". \n').lower().strip()

            if decision == 'hit':
                return True
            elif decision == 'stay':
                return False
            else:
                print('You must type "hit" or "stay".')


"""Changes to make to player class:

    Have the game object handle all the interactions between the player object and the game object
        Game checks to see if they've had their turn. Player tells the game if it wants to hit or stay and game reacts appropriatly.
        Game take care of printing summary statemtns.

"""


class Dealer(Player):
    '''
    The dealer for a game of blackjack.

    The dealer's name is 'The Dealer'. A Dealer object also has a hidden
    card that the player cannot see and a special turn sequence
    as defined by the rules of blackjack.

    Inherits fro the Player class.
    '''

    def __init__(self):
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
        super().__init__('The Dealer')

    def turn(self):
        '''
        The sequence of actions for the dealer's turn.

        This follows the standard rules of blackjack:
        The dealer reveals their hidden card. Then the dealer hits below 17,
        and stays at 17 or above.
        The method also prints a summars of actions to the terminal for any users.
        '''

        if self.hand.value < 17:
            return True
        else:
            self.completedTurn = True
            return False


class Game():
    '''
    A game of blackjack.

    This is the Game object. It has everything needed for a game of blackjack:
    a group of players, a dealer, a deck, a game sequence, and a summary at the end of the game.
    '''

    def __init__(self, *players, summary=True):
        self.players = players
        self.summary = summary
        self.dealer = Dealer()
        self.deck = Deck()

    def deal(self):
        def playerDeal(player: Player):
            player.completedTurn = False
            player.hand.discard()
            # Maybe make more methods in Player Class to make this prettier
            player.hand.cards.extend([self.deck.draw(), self.deck.draw()])

        def dealerDeal():
            self.dealer.completedTurn = False
            self.dealer.hand.discard()
            self.dealer.hand.cards.extend(
                [self.deck.draw().changeHidden(True), self.deck.draw()])

        self.deck.reset()
        self.deck.shuffle()

        list(map(playerDeal, self.players))

        dealerDeal()

        if self.summary:
            print('The Dealer:')
            self.dealer.hand.show()
            print('\n')

            for player in self.players:
                print(f'{player.name} with a hand value of {player.hand.value}:')
                player.hand.show()
                print('\n')

    def turns(self):
        def turnSequence(player):
            if player.__class__ == Dealer:
                player.showHand()

            if self.summary:
                print(
                    f'---------- {player.name} with a hand value of {player.hand.value}. ----------', '\n')
                player.hand.show()

            while not player.completedTurn:
                choice = player.turn()
                if choice is True:
                    player.hand.cards.append(self.deck.draw())
                    if self.summary:
                        print(
                            f'{player.name} hits and has a hand value of {player.hand.value}')
                        player.hand.show()
                    if player.hand.value > 21:
                        player.completedTurn, player.busted = True, True
                        if self.summary:
                            print(f'{player.name} has busted! \n \n')
                elif choice is False:
                    player.completedTurn = True
                    if self.summary:
                        print(
                            f'{player.name} stays with a hand value of {player.hand.value} \n \n')
                else:
                    raise ValueError(
                        "The turn() method in the Player object should return a bool: True for hit or False for stay")

        for player in self.players:
            turnSequence(player)

        turnSequence(self.dealer)

    def recordOutcomes(self):
        remainingPlayers = [
            player for player in self.players if player.busted is False]

        if self.dealer.busted:
            def won(player):
                player.won = True
            list(map(won, remainingPlayers))
        else:
            dealerValue = self.dealer.hand.value
            for player in remainingPlayers:
                if player.hand.value >= dealerValue:
                    player.won = True
                elif player.hand.value < dealerValue:
                    player.lost = True

    def outcomes(self):
        def playerOutcome(player):

            if player.busted is True:
                print(f'----- {player.name} has busted! -----')
            else:
                print(
                    f'----- {player.name} has a hand value of {player.hand.value}. -----')

            player.hand.show()
            print('\n')

        print('\n', '\n', '----------Outsomes----------', '\n', '\n')

        playerOutcome(self.dealer)

        for player in self.players:
            playerOutcome(player)

            if player.won:
                print(f'{player.name} has won! \n')
            else:
                print(f'{player.name} has lost. \n')

    def newSetup(self):
        for player in self.players:
            player.newSetup()
        self.dealer.newSetup()

    def round(self):
        '''
        The sequence of the actions for a game of blackjack.

        This method is simply calls other class methods in game order.
        '''

        if self.summary:
            print('\n', '\n', '----- New Game -----', '\n', '\n')

        self.deal()
        self.turns()
        self.recordOutcomes()

        if self.summary:
            self.outcomes()

        self.newSetup()


def main():
    #     '''The main function - only called if __name__ == __main__.'''

    #     number = int(input('How many human players are playing? \n'))

    #     players = []

    #     for i in range(number):
    #         name = input(f'What is the name of player {i+1}? \n')
    #         players.append(HumanPlayer(name))

    #     game = Game(*players)

    game = Game(HumanPlayer('Alice'), HumanPlayer('Bob'))

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
