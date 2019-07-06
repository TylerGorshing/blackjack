import random


class Card(object):
    """A class of playing cards"""

    def __init__(self, value, suit):
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
        '''Prints the value and suit of a Card.'''

        if self.value == 1:
            print('Ace of {}'.format(self.suit))
        elif self.value < 11:
            print('{} of {}'.format(self.value, self.suit))
        elif self.value == 11:
            print('Jack of {}'.format(self.suit))
        elif self.value == 12:
            print('Queen of {}'.format(self.suit))
        else:
            print('King of {}'.format(self.suit))


class Collection(object):
    """A collection of cards to be used as a deck or a players hand."""

    def __init__(self):
        self.cards = []

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self):
        return self.cards.pop(0)

    def discard(self):
        self.cards = []

    @property
    def size(self):
        return len(self.cards)


class Deck(Collection):

    def __init__(self):
        Collection.__init__(self)
        self.build()

    def build(self):
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))


class Hand(Collection):

    def __init__(self):
        Collection.__init__(self)

    @property
    def value(self):
        valueList = [10 if card.value > 10
                     else card.value for card in self.cards]
        handValue = sum(valueList)

        while valueList.count(1) > 0 and (21 - handValue) >= 10:
            valueList[valueList.index(1)] = 11
            handValue = sum(valueList)

        return handValue


class Player(object):
    def __init__(self, name):
        self.hand = Hand()
        self.name = name
        self.hasHadTurn = False

    def draw(self, collection, hand=None, number_of_cards=1):
        if hand is None:
            hand = self.hand

        for i in range(number_of_cards):
            hand.addCard(collection.removeCard())

    def showHand(self, hand=None):
        if hand is None:
            hand = self.hand

        for card in hand.cards:
            card.show()

    def hit(self, deck, hand=None):
        if hand is None:
            hand = self.hand

        if self.hasHadTurn:
            print('{} has already had thier turn.'.format(self.name))
        else:
            self.draw(deck, hand)
            self.showHand()
            print("{}'s hand value is {}".format(self.name, self.hand.value))

        if self.hand.value > 21:
            self.hasHadTurn = True

    def stay(self):
        print('{} stays with a hand value of {}'.format(
            self.name, self.hand.value))
        self.hasHadTurn = True

    def turn(self, deck):
        if self.hasHadTurn:
            print('{} has already had their turn.'.format(self.name))
            return None

        print("{}'s hand:".format(self.name))
        self.hand.show()
        print("{}'s hand value is {}".format(self.name, self.hand.value))

        while not self.hasHadTurn and self.hand.value <= 21:
            print('What would {} like to do? Hit or Stay?'.format(self.name))
            move = input().strip().lower()
            if move == 'hit':
                self.hit(deck)
            elif move == 'stay':
                self.stay()
            else:
                print("Please enter 'Hit' or 'Stay'")

        if self.hand.value > 21:
            print('{} has busted!'.format(self.name))

    def reset(self):
        self.hand.discard()
        self.hasHadTurn = False


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, 'The Dealer')
        self.hiddenCard = True

    def showHand(self):
        if self.hiddenCard:
            secretCard = self.hand.cards.pop(0)

        Player.showHand(self)

        if self.hiddenCard:
            self.hand.cards.insert(0, secretCard)

    def showHiddenCard(self):
        if self.hiddenCard:
            self.hiddenCard = False
        self.showHand()

    def turn(self, deck):
        if self.hasHadTurn:
            print('The Dealer has already had thier turn. The game is over.')
            return None

        print("{}'s hand with a value of {}:".format(self.name, self.hand.value))
        self.showHiddenCard()

        while self.hand.value < 17:
            print('{} hits.'.format(self.name))
            self.hit(deck)

        if self.hand.value > 21:
            print('The dealer has busted!')

        self.stay()


class Game(object):

    def __init__(self, *players):
        self.players = players
        self.dealer = Dealer()
        self.deck = Deck()

        self.round()

    def round(self):
        self.playerDiscards()
        self.deal()
        self.playerTurns()
        self.dealer.turn(self.deck)
        self.outcome()
        self.resetPlayers()

    def playerDiscards(self):
        for player in self.players:
            player.hand.discard()

    def deal(self):

        self.deck.shuffle()

        self.dealer.draw(self.deck, number_of_cards=2)
        for player in self.players:
            player.hand.discard()
            player.draw(self.deck, number_of_cards=2)

        print('The Dealer:')
        self.dealer.showHand()

        for player in self.players:
            print('{} with a hand value of {}:'.format(
                player.name, player.hand.value))
            player.showHand()

    def playerTurns(self):
        for player in self.players:
            player.turn(self.deck)

    def outcome(self):
        print('Results:')

        for player in self.players:
            if player.hand.value > 21:
                print('{} busted.'.format(player.name))
            elif self.dealer.hand.value > 21:
                print('{} has beat the dealer'.format(player.name))
            elif self.dealer.hand.value > player.hand.value:
                print('{} has lost'.format(player.name))
            else:
                print('{} has won!'.format(player.name))

    def resetPlayers(self):
        for player in self.players:
            player.reset()
        self.dealer.reset()


def main():
    alice = Player('Alice')
    bob = Player('Bob')
    game = Game(alice, bob)

    while True:
        print('Another round? Y/N')
        answer = input().strip().lower()
        if answer == 'y':
            game.round()
        else:
            break


if __name__ == '__main__':
    main()
