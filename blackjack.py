'''A game of blackjack.'''

import cards
import blackjackPlayers


class Game():
    '''
    A game of blackjack.

    This is the Game object. It has everything needed for a game of blackjack:
    a group of players, a dealer, a deck, a game sequence, and a summary at the end of the game.

    Parameters
        ----------
            players : HumanPlayer
                The human players in the game. Can be an arbitrary number of players.

            summary : bool
                Defaults to True
                If true, prints of a summer of each step of the game.

        Attributes
        -----------
            dealer : Dealer
                A dealer object from the players module as the dealer of the game

            deck : Deck
                A deck object from the cards module as the deck of cards in the game
    '''

    def __init__(self, *players, summary=True):
        self.players = players
        self.summary = summary
        self.dealer = blackjackPlayers.Dealer()
        self.deck = cards.Deck()

    def deal(self):
        '''Deals a game of blackjack. Defines a function to deal to the players and function to deal to the dealer.
        Resets shuffles the deck. Prints a summary of the deal if summary=True'''

        def playerDeal(player: blackjackPlayers.Player):
            '''Defines a function that deals two cards to the given player object.'''

            player.completedTurn = False  # The player hasn't taken their turn yet
            player.hand.discard()
            # player.hand.cards is a list.
            player.hand.cards += [self.deck.draw(), self.deck.draw()]

        def dealerDeal():
            ''' Defines a function that deals two cards to the deal, one card is hidden.'''

            self.dealer.completedTurn = False
            self.dealer.hand.discard()
            self.dealer.hand.cards += [self.deck.draw().changeHidden(True),
                                       self.deck.draw()]

        self.deck.reset()
        self.deck.shuffle()

        dealerDeal()

        for player in self.players:
            playerDeal(player)

        if self.summary:
            print('The Dealer:')
            self.dealer.hand.show()  # doesn't print the hidden card
            print('\n')

            for player in self.players:
                # Prints the player's name and their hand value
                print(f'{player.name} with a hand value of {player.hand.value}:')
                player.hand.show()  # prints boths cards in the player's hand
                print('\n')

    def turns(self):
        '''Defines a function turn sequence function then calls the function in a for loop.'''

        def turnSequence(player: blackjackPlayers.HumanPlayer):
            '''The sequence for a single player's turn.'''

            # reveals the dealers hidden card when it's their turn.
            if player.__class__ == blackjackPlayers.Dealer:
                player.hand.reveal()

            if self.summary:
                print(
                    f'---------- {player.name} with a hand value of {player.hand.value}. ----------', '\n')
                player.hand.show()

            while not player.completedTurn:
                choice = player.turn()  # player chooses to 'hit' or 'stay'
                if choice is True:  # If the player chooses to hit
                    # draws a card from the deck and adds it to the players hand
                    player.hand.cards.append(self.deck.draw())
                    if self.summary:
                        print(
                            f'{player.name} hits and has a hand value of {player.hand.value}')
                        player.hand.show()
                    if player.hand.value > 21:  # determins if the player has busted
                        player.completedTurn, player.busted = True, True
                        if self.summary:
                            print(f'{player.name} has busted! \n \n')
                elif choice is False:  # If the player chooses to stay
                    player.completedTurn = True
                    if self.summary:
                        print(
                            f'{player.name} stays with a hand value of {player.hand.value} \n \n')
                else:  # If something other than True or False is returned from the Player object
                    raise ValueError(
                        "The turn() method in the Player object should return a bool: True for hit or False for stay")

        for player in self.players:
            turnSequence(player)

        turnSequence(self.dealer)

    def recordOutcomes(self):
        '''sets player.won and player.lost to the appropriate bool'''

        remainingPlayers = [
            player for player in self.players if player.busted is False]  # Maked a list of all the players who haven't busted

        if self.dealer.busted:  # if the dealer busted, everyone who's left has won!
            for player in remainingPlayers:
                player.won = True
        else:
            dealerValue = self.dealer.hand.value
            for player in remainingPlayers:
                if player.hand.value >= dealerValue:  # for simplicity, the player has won if they tie the dealer
                    player.won = True
                else:  # if the player hasn't deat the dealer
                    player.lost = True

    def outcomes(self):
        '''Prints the outcome of the game player by player'''

        def playerOutcome(player):
            '''A fucntion to be used in a for loop'''

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
            else:  # If the player has lost or busted
                print(f'{player.name} has lost. \n')

    def clean_up(self):
        '''Players discard to prepare for new game.'''
        for player in self.players:
            player.clean_up()
        self.dealer.clean_up()

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

        self.clean_up()


def main():
    '''The main function - only called if __name__ == __main__.'''

    number = int(input('How many human players are playing? \n'))

    players = []

    for i in range(number):
        name = input(f'What is the name of player {i+1}? \n')
        players.append(blackjackPlayers.HumanPlayer(name))

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
