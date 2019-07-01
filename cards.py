import random


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
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
                     else card.value for card in self.hand]
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

    def draw(self, collection, hand=self.hand, number_of_cards=1):
        for i in range(number_of_cards):
            hand.addCard(collection.removeCard())

    def showHand(self, hand=self.hand):
        for card in hand.cards:
            card.show()

    def hit(self, deck, hand=self.hand):
        if self.hasHadTurn:
            print('{} has already had thier turn.'.format(self.name))
        else:
            self.draw(deck, hand)
            self.showHand()
            print("{}'s hand value is {}".format(self.name, self.hand.value))

        if self.hand.value > 21:
            print('{} has busted!'.format(self.name))
            self.hasHadTurn = True

    def stay(self):
        print('{} stays with a hand value of {}'.format(
            self.name, self.hand.value))
        self.hasHadTurn = True

    def turn(self):
        print("{}'s hand:".format(self.name))
        self.hand.show()
        print("{}'s hand value is {}".format(self.name, self.hand.value))

        while not self.hasHadTurn and self.hand.value <= 21:
            print('What would {} like to do? Hit or Stay?'.format(self.name))
            if input().strip().lower() == 'hit':
                self.hit()
            elif input().strip().lower() == 'stay':
                self.stay()
            else:
                print("Please enter 'hit' or 'stay'")

        if self.hand.value > 21:
            print('{} has busted!'.format(self.name))


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, 'The Dealer')
        hiddenCard = True

    def showHand(self):
        if self.hiddenCard:
            secretCard = self.hand.pop(0)

        Player.showHand(self)

        if self.hiddenCard:
            self.hand.inster(0, secretCard)

    def showHiddenCard(self):
        if self.hiddenCard:
            self.hiddenCard = False
        self.showHand()

    def turn(self, deck):
        if self.hasHadTurn:
            print('The Deal has already had thier turn. The game is over.')
            pass

        self.showHiddenCard()

        while self.hand.value < 17:
            self.hit(deck)
            self.showHand()

        print("{}'s hand is {}".format(self.name, self.hand.value))

        if self.hand.value > 21:
            print('The dealer has busted!')

        self.hasHadTurn = True


class BlackJackGame(object):

    def __init__(self, *players):

        self.player = player
        self.dealer = Dealer()

        self.player.hand = []

        self.deck = Deck()
        self.deck.shuffle()

        self.player.deck = self.deck
        self.dealer.deck = self.deck

        self.deal()

    def deal(self):

        self.dealer.draw(self.deck, 2)
        self.player.draw(self.deck, 2)

        print('Dealer:')
        self.dealer.showHand()

        print(self.player.name + ':')
        self.player.showHand()

        print("{}'s hand is currently {}".format(
            self.player.name, self.player.handValue))
