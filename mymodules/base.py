"""
# File: base.py
# Contains classes for game
# Created by Ivan Kosarevych
# 18.02.17 19:00:17
"""
from field_generator import *

class Ship(object):
    """
    Information about ship, including length, coordinates, orientation, hit decks
    """
    def __init__(self, length, bow, horizontal = True):
        """
        :param length: tuple, example for horizontal 2Xship: (1,2)
        :param bow: tuple(int,int), coordinates of left upper deck
        :param horizontal: bool

        Initializes new ship
        """
        self._length = length
        self.bow = bow
        self.horizontal = horizontal

        position_in_length = 1 if self.horizontal else 0
        self._hit = [False for i in range(self._length[position_in_length])]


    def shoot_at(self, point):
        """
        :param point: tuple
        :return: None

        Shows hitting a deck of a ship

        """
        if self.horizontal:
            deck = point[1] - self.bow[1]
        else:
            deck = point[0] - self.bow[0]

        self._hit[deck] = True


class Field:
    """
    Information about field, its appearance(ships, hit ships, misses),
    random field generation
    """
    def __init__(self):
        """
        Initializes random field
        """
        # create empty field
        self._ships = [[None for i in range(10)] for j in range(10)]
        ships_size = [4, 3, 2, 1]
        field = []
        
        # fill it with ships
        for count in range(len(ships_size)):
            # put as many ships of each type as required
            for i in range(count + 1):
                # generate ship and check whether it doesn't touch others,
                # otherwise regenerate it until it touches no other ship
                shp = generate_ship(ships_size[count])
                horizontal, ship_coordiantes = shp[0], shp[1]
                ship_area = make_shp_area(ship_coordiantes)
                if count != 0:
                    while set(ship_area).intersection(set(field)) != set():
                        shp = generate_ship(ships_size[count])
                        horizontal, ship_coordiantes = shp[0], shp[1]
                        ship_area = make_shp_area(ship_coordiantes)
                
                # add ship object to field
                field.extend(ship_coordiantes)
                length = (1, ships_size[count]) if horizontal else (ships_size[count], 1)
                ship_object = Ship(length, ship_coordiantes[0], horizontal = horizontal)
                for coord in ship_coordiantes:
                    self._ships[coord[0]][coord[1]] = ship_object


    def shoot_at(self, point):
        """
        :param point: tuple(int, int)
        :return: object or None
        
        Demonstrates shoots on field: point on field becomes True if any ship was hit
        or False otherwise
        """
        row,column = point
        if self._ships[row][column] and self._ships[row][column] is not True:
            self._ships[row][column].shoot_at(point)
            ship = self._ships[row][column]
            self._ships[row][column] = True

            return ship

        self._ships[row][column] = False



    def field_with_ships(self):
        """
        :return: str
        
        Makes string with player's ships and opponent's shoots
        """
        field_str = ' '
        for i in range(1, 10):
            field_str += '|' + ' ' + str(i) + ' '
        field_str += '|' + ' ' + 'X' + ' ' + '|' + '\n'

        for i in range(41): field_str += u"\u2594";
        field_str += '\n'

        for row in range(10):
            field_str += chr(65 + row) + '|'
            for column in range(10):
                if self._ships[row][column] is True:
                    field_str += ' X '
                elif self._ships[row][column] is False:
                    field_str += ' '+ u"\u2022" + ' '     # bullet
                elif self._ships[row][column]:
                    field_str += ' * '
                else:
                    field_str += '   '
                field_str += '|'


            field_str += '\n'
            for i in range(41): field_str += u"\u2594";
            field_str += '\n'

        return field_str


    def field_without_ships(self):
        """
        :return: str
        
        Makes string with player's shoots on opponent's field 
        """
        field = Field.field_with_ships(self)
        field = field.replace('*', ' ')

        return field


class Player:
    """
    Info about player, including name and sunk ships. Interaction with
    user, including getting coordinates to shoot
    """
    def __init__(self, name):
        """
        :param name: str

        Initializes new player
        """
        self._name = name
        self.sunk_ships = 0


    def read_position(self):
        """
        :return: tuple(int,int)
        
        Reads game coordinates of shoot and converts them to coordinates in list
        of field
        """
        from string import ascii_uppercase

        battleship_positions = [let + str(i) for let in ascii_uppercase[:10] for i in range(1, 10 + 1)]
        list_positions = [(row, column) for row in range(10) for column in range(10)]
        compliance_table = dict(zip(battleship_positions, list_positions))

        # get coordinates from user until they are correct
        battleship_position  = input(self._name + ', enter position to shoot at: ').strip()
        while battleship_position not in battleship_positions:
            battleship_position = input('There is no position you entered, try again: ').strip()

        return compliance_table[battleship_position]


class Game:
    """
    Combines Fields and Players
    """
    def __init__(self):
        """
        Initializes new game
        """
        import os, time

        player1_name = input('Player 1, enter your name: ')
        os.system('cls')
        player2_name = input('Player 2, enter your name: ')

        self._players = [Player(player1_name), Player(player2_name)]
        self._field = [Field(), Field()]
        self._current_player = 0

    def shoot_at(self, player_index, field_index):
        """

        :param player_index: int
        :param: field_index: int
        :return: ship object if ship was hit, None otherwise

        Makes shoot on given field, raises quantity of sunk ships in given player,
        if ship was sunk
        """
        # Read position to shoot
        point = self._players[player_index].read_position()
        # make shoot on field
        ship = self._field[field_index].shoot_at(point)

        # check whether we hit a ship and if so whether ship is wounded or killed
        # and show it
        try:
            ship_len = ship._length[1] if ship.horizontal else ship._length[0]
            if ship._hit == [True for i in range(ship_len)]:
                self._players[player_index].sunk_ships += 1
                print('\nKILLED!')
            else:
                print('\nWOUNDED!')
        except:
            return

        return ship


    def field_with_ships(self, index):
        """
        :param index: int
        :return: None

        Show player's field with opponent's shoots
        """
        print(self._field[index].field_with_ships())



    def field_without_ships(self, index):
        """
        :param index: int
        :return: None

        Show player's shoots on opponent's field
        """
        print(self._field[index].field_without_ships())


    def check_winner(self, player_index):
        """
        :param player_index: int
        :return: int or None
        """
        if self._players[player_index].sunk_ships >= 10: return player_index
