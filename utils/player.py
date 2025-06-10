from utils.card import Card
from typing import List
import random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards: List[Card] = []
        self.turn_count = 0
        self.history: List[Card] = []
    
    def __str__(self) -> str:
        cards_str = [str(card) for card in self.cards]
        history_str = [str(card) for card in self.history]

        return f"{cards_str}, {self.turn_count}, {history_str}"
    
    def play(self) -> Card | None:
        """Play a card from the player's hand."""
        if len(self.cards) == 0:
            print('No more cards to play')
            return None
        card_to_play = random.choice(self.cards)
        self.cards.remove(card_to_play)
        self.history.append(card_to_play)
        self.turn_count += 1
        print(f"Player {self.name} turn {self.turn_count} played {card_to_play.value} {card_to_play.icon} {card_to_play.color}")
        return card_to_play

    def give_cards(self, cards:List[Card]):
        """Give cards to the player."""
        self.cards = cards
        print(f"Player {self.name} has {len(self.cards)} cards: {self}")