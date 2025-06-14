from typing import List
import random
import numpy as np

from utils.card import Card, IconType, ValueType
from utils.player import Player

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
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)
    
    def distribute(self, players: List[Player]):
        """
        Distribute cards to players.
        Ensures that each player gets an equal number of cards.
        If the number of cards is not divisible by the number of players,
        it removes the excess cards to ensure equal distribution.
        """
        num_players = len(players)
        num_cards = len(self.cards)
        remainder = num_cards % num_players
        if remainder != 0:
            print(f"Removing {remainder} card(s) to ensure equal distribution.")
            self.cards = self.cards[:-remainder]
        cards_per_player = np.array_split(self.cards, len(players))
        for player, cards in zip(players, cards_per_player):
            player.give_cards(list(cards))
        