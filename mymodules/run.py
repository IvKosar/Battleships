"""

"""

from game import Game
import os, time


game = Game()
while True:
    if game.check_winner(game._current_player):
        winner = game._players[game._current_player % 2]._name
        print(winner, 'WON!')
        break

    print('\n')
    game.field_with_ships(game._current_player)
    print('\n')
    game.field_without_ships((game._current_player - 1) % 2)

    #print(game.shoot_at(game._current_player, (game._current_player + 1) % 2))
    if not game.shoot_at(game._current_player, (game._current_player + 1) % 2):
        print("Please give a computer to your opponent")
        time.sleep(1)
        game._current_player = (game._current_player + 1) % 2
    #else:
    #   game.shoot_at(game._current_player, (game._current_player + 1) % 2)


