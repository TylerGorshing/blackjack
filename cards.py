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

    def draw(self, deck, number_of_cards):
        for i in range(number_of_cards):
            self.hand.append(deck.draw())

    def showHand(self):
        for card in self.hand:
            print('{} of {}'.format(card.value, card.suit))


class BlackJackPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    @property
    def handValue(self):
        valueList = [10 if card.value >
                     10 else card.value for card in self.hand]
        handValue = sum(valueList)

        while valueList.count(1) > 0 and (21 - handValue) >= 10:
            valueList[valueList.index(1)] = 11
            handValue += 10

        return handValue

    def hit(self):
        if self.hasHadTurn:
            print('{} has already had thier turn.'.format(self.name))
            return None

        if self.handValue <= 21:
            self.draw(self.deck, 1)
            self.showHand()

        print("{}'s hand is {}".format(self.name, self.handValue))

        if self.handValue > 21:
            print('{} has busted!'.format(self.name))
            self.hasHadTurn = True

    def stay(self):
        self.hasHadTurn = True


class BlackJackDealer(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.hiddenCard = True

    @property
    def handValue(self):
        valueList = [10 if card.value >
                     10 else card.value for card in self.hand]
        handValue = sum(valueList)

        while valueList.count(1) > 0 and (21 - handValue) >= 10:
            valueList[valueList.index(1)] = 11
            handValue += 10

        return handValue

    def showHand(self):
        if self.hiddenCard:
            secretCard = self.hand.pop()

        Player.showHand(self)

        if self.hiddenCard:
            self.hand.append(secretCard)

    def showHiddenCard(self):
        if self.hiddenCard:
            self.hiddenCard = False
        self.showHand()

    def turn(self):
        if self.hasHadTurn:
            print('The Deal has already had thier turn.')
            pass

        self.showHiddenCard()

        while self.handValue < 17:
            self.draw(self.deck, 1)
            self.showHand()

        print("{}'s hand is {}".format(self.name, self.handValue))

        if self.handValue > 21:
            print('The dealer has busted!')

        self.hasHadTurn = True


class BlackJackGame(object):

    def __init__(self, player):

        self.player = player
        self.dealer = BlackJackDealer('Dealer')

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
