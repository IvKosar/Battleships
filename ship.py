"""

"""
from field_generator import *

class Ship(object):
    """

    """
    def __init__(self, length, bow, horizontal = True):
        """
        :param length:
        :param bow:
        :param horizontal:
        """
        self.__length = length
        self.bow = bow
        self.horizontal = horizontal
        self.__hit = []
        position_in_length = 1 if self.horizontal else 0
        for i in range(self.__length[position_in_length]):
            self.__hit.append(False)


    def shoot_at(self, point):
        if self.horizontal:
            deck = point[1] - self.bow[1]
        else:
            deck = point[0] - self.bow[0]

        self.__hit[deck] = True


class Field:
    def __init__(self):
        self._ships = [[None for i in range(10)] for j in range(10)]
        ships_size = [4, 3, 2, 1]
        field = []

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

                field.extend(ship_coordiantes)
                length = (1, ships_size[count]) if horizontal else (ships_size[count], 1)
                ship_object = Ship(length, ship_coordiantes[0], horizontal = horizontal)
                for coord in ship_coordiantes:
                    self._ships[coord[0]][coord[1]] = ship_object


    def shoot_at(self, point):
        """

        :param point:
        :return:
        """
        row,column = point
        if self._ships[row][column]:
            self._ships[row][column].shoot_at(point)

        self._ships[row][column] = True



    def field_with_ships(self):
        """

        :return:
        """
        field_str = ''
        for row in range(10):
            for column in range(10):
                if self._ships[row][column] is True:
                    field_str += 'X'
                elif self._ships[row][column]:
                    field_str += '*'
                else:
                    field_str += ' '

            field_str += '\n'

        return field_str


    def field_without_ships(self):
        """

        :return: str
        """
        field = Field.field_with_ships(self)
        field.replace('*', ' ')

        return field




field = Field()

field.shoot_at((0,0))
print(field._ships)
print(field.field_with_ships())