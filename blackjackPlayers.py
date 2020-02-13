'''Defines Blackjack players and how they take their turns including the dealer.'''

from cards import Collection


class Hand(Collection):
    '''A player's Blackjack hand.

    Inherits from the Collection class in the cards module.'''

    def __init__(self, cards=None, replacement=False):
        super.__init__(cards=cards, replacement=replacement)

    @property
    def value(self) -> int:
        ''' Returns the value of a hand as determined by the rules of blackjack.'''

        value_list = [10 if card.value > 10  # 10, Jack, Queen, and King are all worth 10 points
                      else card.value for card in self.cards]  # Creates a list of the integer values of each card in the hand.

        # Adds all the values together - treats all Aces as if they're worth 1 point each
        hand_value = sum(value_list)

        # Checks to see if any Aces can be worth 11 points instead of 1 point
        while value_list.count(1) > 0 and (21 - hand_value) >= 10:
            value_list[value_list.index(1)] = 11
            hand_value = sum(value_list)

        return hand_value

    @property
    def num_aces(self) -> int:
        '''Returns the number of aces in a hand'''

        # Simply counts how many cards have a value of 1
        return [card.value for card in self.cards].count(1)


class Player():
    '''
    A blackjack player.

    This is the parent class for a human player and the dealer. It includes
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
            True if the player has had their turn. False otherwise

        lost : bool
            True if the player has faild to beat the dealer at the end of a game. False otherwise

        won : bool
            True if the palyer has beaten the dealer at the end of a game. False otherwise

        Busted : bool
            True if the player's hand value exceeded 21. False otherwise
    '''

    def __init__(self, name: str):

        self.hand = Hand()
        self.name = name
        self.completedTurn = False
        self.lost = False
        self.won = False
        self.busted = False

    @property
    def hasBlackjack(self) -> bool:
        '''Returns True if the player's hand value is 21.'''
        if self.hand.value == 21:
            return True
        else:
            return False

    def clean_up(self) -> None:
        '''
        Resets the player for a new game.

        The method empties the player's hand and sets completedTurn, lost, won, and busted to False.
        '''
        self.hand.discard()
        self.completedTurn = False
        self.lost = False
        self.won = False
        self.busted = False


class HumanPlayer(Player):
    '''
    A class for a human player.

    The user intereacts with the game through an interactive python shell.

    Inherits from the Player class.
    '''

    def __init__(self, name):
        super().__init__(name)

    def turn(self) -> bool:
        '''Defines a human player's turn.
        Returns a bool to be handled by the game program.'''

        while True:
            # Get's user input, makes all charactures lowercase, and removes any whitespace
            decision = input('Enter "hit" or "stay". \n').lower().strip()

            if decision == 'hit':
                return True  # A return value breaks the while loop
            elif decision == 'stay':
                return False
            else:
                # Humans can be dumb. Doesn't break the while loop
                print('\nYou must type "hit" or "stay".')


class Dealer(Player):
    '''The dealer in a game of Blackjack. Inherits from the Player class.'''

    def __init__(self):
        super().__init__('The Dealer')

    def turn(self):

        return self.hand.value < 17  # Returns True for 'hit' or False for 'stay'
