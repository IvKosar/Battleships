"""

"""

from game import Game
import os


game = Game()
while True:
    if not game.shoot_at(game._current_player, (game._current_player + 1) % 2):
        game._current_player += 1 % 2
    else:
        game.shoot_at(game._current_player, (game._current_player + 1) % 2)