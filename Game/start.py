from Game.tic_tac_toe_game import TicTacToeGame
from Game.game_manager import GameManager
from Game.player import Player

p1 = Player("One")
p2 = Player("Two")
1
t = GameManager(p1, p2)

t.start_game_series()