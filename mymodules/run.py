"""
# File: run.py
# Organizes user interface, runs the game
# Created by Ivan Kosarevych
# 18.02.2017 19:06:57
"""

from base import Game
import time, os

# get players' names
player1_name = input('Player 1, enter your name: ')
os.system('clear')
player2_name = input('Player 2, enter your name: ')

# start the game
game = Game(player1_name, player2_name)
while True:
    os.system('clear')
    input('Press any key to start')

    # check whether we have a winner and if so finish
    if game.check_winner((game._current_player - 1) % 2) or game.check_winner(game._current_player):
        winner = game._players[game._current_player]._name
        break

    print('\n')
    game.field_with_ships(game._current_player)
    print('\n')
    game.field_without_ships((game._current_player - 1) % 2)

    # check whether player hit a ship and if so don't change current player, otherwise change
    if not game.shoot_at(game._current_player, (game._current_player + 1) % 2):
        input("Press any key and give a computer to your opponent")
        game._current_player = (game._current_player + 1) % 2

    time.sleep(1)

os.system('clear')
print(winner, 'WON!')
