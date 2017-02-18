"""
# File: run.py
# Organizes user interface, runs the game
# Created by Ivan Kosarevych
# 18.02.2017 19:06:57
"""

from base import Game
import time, os


game = Game()
while True:
    os.system('cls')

    if game.check_winner((game._current_player + 1) % 2):
        winner = game._players[(game._current_player + 1) % 2]._name
        break

    print('\n')
    game.field_with_ships(game._current_player)
    print('\n')
    game.field_without_ships((game._current_player - 1) % 2)

    if not game.shoot_at(game._current_player, (game._current_player + 1) % 2):
        input("Press any key and give a computer to your opponent")
        game._current_player = (game._current_player + 1) % 2

    input('Press any key to start')

print(winner, 'WON!')
