from typing import Literal, List
import random
import numpy as np

# from player import Player

IconType = Literal['♥', '♦', '♣', '♠']
ValueType = Literal['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
class Symbol:

    def __init__(self,  icon:IconType):
        icon_color_dict = {'♥': 'red', '♦': 'red', '♣': 'black', '♠': 'black'}
        self.icon = icon
        self.color = icon_color_dict[icon]
    
    def __str__(self) -> str:
        return f"The card symbol {self.icon} {self.color}"
    
class Card(Symbol):

    def __init__(self, icon: IconType, value: ValueType):
        Symbol.__init__(self, icon)
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} {self.icon} {self.color} "

class Deck:

    def __str__(self) -> str:
        desc = f"A deck of {len(self.cards)} cards:\n "
        for card in self.cards:
            desc += f"{card.value} {card.icon} {card.color}, "
        return desc
    
    def __init__(self):
        self.cards = []
    
    def fill_deck(self):
        """"
        A method to fill a deck of cards
        """
        icons:List[IconType]  = ['♥', '♦', '♣', '♠']
        values: List[ValueType] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for value in values:
            for icon in icons:
                self.cards.append(Card(icon, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    # Todo Player type
    def distribute(self, players):
        num_players = len(players)
        num_cards = len(self.cards)
        remainder = num_cards % num_players
        if remainder != 0:
            print(f"Removing {remainder} card(s) to ensure equal distribution.")
            self.cards = self.cards[:-remainder]
        cards_per_player = np.array_split(self.cards, len(players))
        for player, cards in zip(players, cards_per_player):
            player.give_cards(list(cards))
        





        