"""A game of blackjack."""

from cards import Deck
from players import (
    HumanPlayer,
    Dealer,)


class Game():
    """
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
    """

    def __init__(self, *players, summary=True):
        self._summary = summary
        self._dealer = Dealer()
        self._players = players
        self._deck = Deck()

    def __call__(self):
        if self._summary:
            self._anounce('New Game!')

        self._deal()
        for player in self._players:
            self._turn_sequance(player)
        self._turn_sequance(self._dealer)

        if self._summary:
            self._results()

        self._clean_up()

    def _anounce(self, string_):
        """This bit of code is used a lot, so I'm making a function."""
        print(f'\n\n----- {string_} -----')

    def _deal(self):
        """Deals a game of blackjack. Defines a function to deal to the players and function to deal to the dealer.
        Resets shuffles the deck. Prints a summary of the deal if summary=True"""

        self._deck.shuffle()

        for player in self._players:
            player.hand.add([self._deck.draw(), self._deck.draw()])

        # Flips one of the dealer's cards facedown.
        self._dealer.hand.add([self._deck.draw(), self._deck.draw()])
        self._dealer.hand[0].flip()

        # Prints a summary of the deal if _summary is True.
        if self._summary:
            self._anounce('The Dealer')
            self._dealer.hand.info()

            for player in self._players:
                self._anounce(f'{player.name} with {player.hand.value}')
                player.hand.info()

    def _get_decision(self, player):
        decision = player.decision()

        if decision is True or decision is False:
            return decision
        else:
            raise TypeError(
                "The turn method of a Player object should return a bool: True or 'hit' or False for 'stay'")

    def _turn_sequance(self, player):
        """Defines a turn sequence for an individual player

        This method should work for ANY Player object, therefore
        ALL Player objects need a begin_turn() method and a decision() method.
        """

        player.begin_turn()
        hand_value = player.hand.value
        if self._summary:
            self._anounce(f'{player.name} with {hand_value}')
            player.hand.info()

        while hand_value <= 21:
            decision = self._get_decision(player)
            if decision:
                player.hand.add(self._deck.draw())
                hand_value = player.hand.value
                if self._summary:
                    print(f'{player.name} hits.\n')
                    player.hand.info()
                    print(f'\n{player.name} has {hand_value}.\n')
            else:
                if self._summary:
                    print(f'{player.name} stays with {hand_value}.\n')
                break

        player.had_trun = True  # Do I really need this?

        if hand_value > 21 and self._summary:
            print(f'{player.name} busts!\n\n')

    def _results(self):
        """Prints the outcome of the game player by player"""
        self._anounce('Final Results')
        dealer_score = self._dealer.hand.value

        for player in self._players:
            player_score = player.hand.value
            if player_score <= 21:
                if player_score < dealer_score < 21:
                    self._anounce(f'{player.name} Loses!')
                else:
                    self._anounce(f'{player.name} Wins!')
            else:
                self._anounce(f'{player.name} Busts!')

    def _clean_up(self):
        """Players discard to prepare for new game."""
        for player in self._players:
            player.clean_up()
        self._dealer.clean_up()
        self._deck.reset()


def main():
    """The main function - only called if __name__ == __main__."""

    while True:
        try:
            number = int(input('How many human players are playing? \n'))
        except ValueError:
            print('Please enter a valid number.')
            continue

        if number > 0:
            break
        else:
            print('Please enter a valid (positive) number.')

    players = []

    for i in range(number):
        name = input(f'What is the name of player {i+1}? \n')
        players.append(HumanPlayer(name))

    game = Game(*players)
    game()  # The game object is callable. Neat!

    while True:
        print('Another round? Y/N')
        answer = input().strip().lower()
        if answer == 'y':
            game()
        else:
            break


if __name__ == '__main__':
    main()
