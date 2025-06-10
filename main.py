from utils.game import Board
from utils.player import Player

names = ['Cat',"E", "Ri", "Na", "X"]
players = []
for name in names:
    players.append(Player(name))
b = Board(players)
print(b)
b.start_game()
while not b.game_over:
    b.play_turn()

    