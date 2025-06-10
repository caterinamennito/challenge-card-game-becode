from typing import List

from player import Player
from card import Deck, Card

class Board:
    def __init__(self, players: List['Player']):
        self.players = players
        self.turn_count = 0
        self.active_cards:List['Card'] = []
        self.history_cards: List['Card'] = []
        self.game_over = False
    
    def __str__(self) -> str:
        active_cards_str = [str(card) for card in self.active_cards]
        history_cards_str = [str(card) for card in self.history_cards]

        return f"Board with {len(self.players)} players, turn count: {self.turn_count}, active cards: {active_cards_str}, history cards: {history_cards_str}"
    
    def start_game(self):
        d = Deck()
        d.fill_deck()
        d.shuffle()
        d.distribute(self.players)

    
    def play_turn(self):

        for player in self.players:
            card_played = player.play()
            if card_played:
                self.active_cards.append(card_played)
                self.history_cards.append(card_played)
            else:
                self.game_over = True
                print("The game is over!")
                break
        if not self.game_over:
            self.turn_count += 1
            self.active_cards = []
            print(f"{self}")
        

names = ['Cat',"E", "Ri", "Na", "X"]
players = []
for name in names:
    players.append(Player(name))
b = Board(players)
print(b)
b.start_game()
while not b.game_over:
    b.play_turn()