import random


class Card(object):
    """A class of playing cards"""

    def __init__(self, value: int, suit: str):
        """
        The constructor for the Card class.

        Parameters
        ----------
        value : int
            The value of a card. 1 is Ace. 11 is Jack. 12 is Queen. 13 is King.

        suit : str
            The suit of the card. Generally 'Spades', 'Hearts', 'Diamonds', or 'Clubs'.
        """
        self.value = value
        self.suit = suit

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


class Collection(object):
    '''The parent class for a deck of cards or a player's hand.'''

    def __init__(self):
        '''Initializes the collection object with an empty container of cards.'''

        self.cards = []

    def show(self):
        '''Prints each card in the collection.'''

        for card in self.cards:
            card.show()

    def shuffle(self):
        '''Randomizes the order of the collection of cards.'''

        random.shuffle(self.cards)

    def addCard(self, card: Card):
        '''Adds a given card to the collection.

        The Method can be used long with the removeCard() method to draw a card and add it to a hand.

        Parameters:
        -----------

            card: Card object
                The card object to be added to the collection.
        '''

        self.cards.append(card)

    def removeCard(self) -> Card:
        '''Removes a card object from a collection and returs that card.'''

        return self.cards.pop(0)

    def discard(self):
        '''Empties the entire collection'''

        self.cards = []

    @property
    def size(self) -> int:
        ''' A property that returns the number of cards in the collection.'''

        return len(self.cards)


class Deck(Collection):
    ''' A deck of standard playing cards.

    The deck consists of 52 card objects with the standard suits and values.
    This can be used as a deck of cards to play various games.

    Inharets from the Collection Class.'''

    def __init__(self):
        '''Initializes the deck.

        No parameters. Builds a deck of card in asscending order. The order of the suits is Spade, Hearts, Diamonds, and Clubs.
        '''
        super().__init__()
        self.build()

    def build(self):
        '''Creats the 52 cards in the Deck

        This method only adds cards. It does not remove cards from the deck. To remove cards, the discard() method should be called from the parent class
        '''

        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))


class Hand(Collection):
    '''A player's Blackjack hand.

    Inharets from the Collection class.'''

    def __init__(self):
        '''Initializes the hand from the Collection class.'''

        super().__init__()

    @property
    def value(self) -> int:
        '''
        A property that returns the value of the hand according the the rules of blackjack.

        The method takes into consideration the different possible
        values of an ace and the values of Jacks, Kings, and Queens.
        '''

        valueList = [10 if card.value > 10
                     else card.value for card in self.cards]
        handValue = sum(valueList)

        while valueList.count(1) > 0 and (21 - handValue) >= 10:
            valueList[valueList.index(1)] = 11
            handValue = sum(valueList)

        return handValue


class Player(object):
    '''
    A blackjack player.

    The is the parent class for a human player and the dealer. It includes
    methods and attributes relevents to both kinds of players.
    '''

    def __init__(self, name: str):
        '''Initializes the player object.

        Parameters:
        -----------

            name: str
                The player's name.

        Attributes:
        -----------

            self.hand:
                A Hand object to hold the player's cards.

            self.name: str
                The name of the player.

            self.hasHadTurn:
                Boolean - show if the player has had thier turn in a round of blackjack
        '''

        self.hand = Hand()
        self.name = name
        self.hasHadTurn = False

    def draw(self, collection: Collection, hand: Hand = None, number_of_cards: int = 1):
        '''
        Draws a card from a specified collection object and adds it to the players hand.

        Parameters:
        -----------

            collection:
                The collection to draw from. Generally, the Deck object being used in the game.

            hand = None:
                Specifies which hand the player should add the drawn cards to.
                Using None, defaults to the players only hand.

            number_of_cards = 1:
                Specifies the number of cards to be drawn from the given collection.
                Defaults to 1 card.
        '''
        if hand is None:
            hand = self.hand

        for i in range(number_of_cards):
            hand.addCard(collection.removeCard())

    def showHand(self, hand: Hand = None):
        '''Prints all the cards in the players hand.

        Parameters:
        -----------

        hand:
            The hand that will be shown.
            Using None, defautls to the payers only hand.
    `   '''

        if hand is None:
            hand = self.hand

        for card in hand.cards:
            card.show()

    def hit(self, deck: Deck, hand: Hand = None):
        '''The "hit" action in a game of blackjack.

        Draws a card from the specified deck and adds it to the specified hand. Prints a summary
        and results of the action including all the cards in the player's hand and the total value of the hand.

        Parameters:
        -----------

        deck:
            The Deck object the player will draw from. Generally, the deck object being used in the game of blackjack the player is playing.

        hand:
            The Hand object the playing is adding the drawn card to
        '''

        if hand is None:
            hand = self.hand

        if self.hasHadTurn:  # checks to see if the player has had their turn.
            print('{} has already had thier turn.'.format(self.name))
        else:
            self.draw(deck, hand)
            self.showHand()
            print("{}'s hand value is {}".format(
                self.name, self.hand.value))

        if self.hand.value > 21:  # Checks to see if the player has busted.
            # If they player busts, their turn is ended.
            self.hasHadTurn = True

    def stay(self):
        '''The "stay" action in a game of blackjack ending the player's turn.'''

        print('{} stays with a hand value of {}'.format(
            self.name, self.hand.value))
        self.hasHadTurn = True

    def reset(self):
        '''
        Resets the player for a new game.

        The method empties the player's hand and sets self.hasHadTurn to False.
        '''
        self.hand.discard()
        self.hasHadTurn = False


class HumanPlayer(Player):
    '''
    A class for a human player.

    The user intereacts with the game through the terminal.

    Inheriates from the Player class.
    '''

    def __init__(self, name: str):
        '''
        Initalizes the HumanPlayer.

        Parameters:
        -----------
            name: str
                The name of the human playing the game.
        '''
        super().__init__(name)

    def turn(self, deck: Deck):
        '''
        A method allowing the user to take thier turn using the terminal.

        This method prints instructions from the user and askes the user what action they would like to take.
        turn() prints information to the terminal for the user to make game decisions.

        Parameters:
        -----------
            deck: Deck object
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

        if self.hasHadTurn:  # checks to see if the user has had their turn.
            print(f'{self.name} has already had their turn.')
            return None

        print(f"{self.name}'s hand:")
        self.hand.show()
        print(f"{self.name}'s hand value is {self.hand.value}")

        # Allows the user to continue until choose "stay" or they bust.
        while not self.hasHadTurn and self.hand.value <= 21:
            print(f'What would {self.name} like to do? Hit or Stay?')
            move = input().strip().lower()
            if move == 'hit':
                self.hit(deck)
            elif move == 'stay':
                self.stay()
            else:
                print("Please enter 'Hit' or 'Stay'")  # Humans are dumb.

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

    def __init__(self):
        '''
        Initilizes the Dealer object.

        Atrributes:
        -----------
            self.name is always 'The Dealer'

            self.hiddenCard: bool
                True if a card is hidden from the player. When the dealer starts their turn,
                the dealer flips the card, and self.hiddenCard is changed to false.
        '''
        Player.__init__(self, 'The Dealer')
        self.hiddenCard = True

    def showHand(self):
        '''A special showHand() method for the dealer that hides the hidden card if self.hiddenCard is Ture.'''

        if self.hiddenCard:
            secretCard = self.hand.cards.pop(0)

        Player.showHand(self)

        if self.hiddenCard:
            self.hand.cards.insert(0, secretCard)

    def showHiddenCard(self):
        '''
        Reveals the deal's hidden card.

        This changes self.hiddenCard to False and prints all the dealer's cards to the terminal.
        '''

        if self.hiddenCard:
            self.hiddenCard = False
        self.showHand()

    def turn(self, deck: Deck):
        '''
        The sequence of actions for the dealer's turn.

        This follows the standard rules of blackjack:
        The dealer reveals their hidden card. Then the dealer hits below 17, and stays at 17 or above.
        The method also prints a summars of actions to the terminal for any users.
        '''

        if self.hasHadTurn:
            print('The Dealer has already had thier turn. The game is over.')
            return None

        print(f"{self.name}'s hand with a value of {self.hand.value}:")
        self.showHiddenCard()

        while self.hand.value < 17:  # The dealer must hit if their hand value is less than 17
            print(f'{self.name} hits.')
            self.hit(deck)

        if self.hand.value > 21:
            print('The dealer has busted!')

        self.stay()


class Game(object):
    '''
    A game of blackjack.

    This is the Game object. It has everything needed for a game of blackjack:
    a group of player, a dealer, a deck, a game sequence, and a summary at the end of the game.
    '''

    def __init__(self, *players: HumanPlayer):
        '''
        Initializes the Game object.

        Takes the players and creats a Dealer object and a Deck object.

        Parameters:
        -----------
            *players: HumanPlayer objects
                Accepts any number of human players for a game.
                Caution! A Game object only creats a single Deck object with 52 cards. Only a handful of plays can play before the deck runs out of cards.

        Attriburtes:
        ------------
            self.dealer: Dealer object
                The dealer for the game of blackjack. The dealer has a hand with a hiden card and takes thier own turn.

            self.deck: Deck object
                A standard 52 card deck that is used to deal cards to the players.
        '''

        self.players = players
        self.dealer = Dealer()
        self.deck = Deck()

    def round(self):
        '''
        The sequence of the actions for a game of blackjack.

        This method is simply calls other class methods in game order.
        '''

        self.playerDiscards()
        self.deal()
        self.playerTurns()
        self.dealer.turn(self.deck)
        self.outcome()
        self.resetPlayers()

    def playerDiscards(self):
        '''
        Empties all the human players' hands.

        This is called at the begining and end of each
        round to ensure the players start with an empty hand.
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

        print('The Dealer:')
        self.dealer.showHand()  # Shows only the visible card.

        for player in self.players:
            print('{} with a hand value of {}:'.format(
                player.name, player.hand.value))
            player.showHand()

    def playerTurns(self):
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

    def resetPlayers(self):
        '''
        Resets each player and the dealer in preparation for a new game.
        '''

        for player in self.players:
            player.reset()
        self.dealer.reset()


def main():
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
