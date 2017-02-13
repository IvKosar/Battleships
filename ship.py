"""

"""

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


    def shoot_at(self, tuple):
        if self.horizontal:
            deck = tuple[1] - self.bow[1]
        else:
            deck = tuple[0] - self.bow[0]

        self.__hit[deck] = True
        print(self.__hit)

class Field:
    def __init__(self):
        self.ships = [[None for i in range(10)] for j in range(10)]
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
                for coor in ship_coordiantes:
                    self.ships[coord[0]][coord[1]] = ship_object



def generate_ship(size):
    """
    :param size: int
    :return: list(list)

    Generates coordinates for ship of given size
    Example for size 4: [(1,2),(1,3),(1,4),(1,5)]
    """
    import random

    # Choose rotation(horizontal/vertical)
    orientations = ['horizontal', 'vertical']
    orientation = random.choice(orientations)
    # Choose number of a row/column
    row_col = random.randrange(0, 10)
    # Choose first point of ship
    first_point = random.randrange(0, 10 - size)

    # find ship coordinates
    if orientation == 'horizontal':
        ship_coord = [(row_col, i) for i in range(first_point, first_point + size)]
    else:
        ship_coord = [(i, row_col) for i in range(first_point, first_point + size)]

    horizontal = True if orientation == 'horizontal' else False

    return horizontal, ship_coord


def make_shp_area(shp_coords):
    """
    :param shp_coords: list
    :return: list

    Generates coordinates of area around a ship with this ship,
    where others ships aren't allowed to be placed
    Example of shp_cooords: [(1,1),(1,2),(1,3)] - every tuple is a coordinate of point on field
    Example of area:
    xxxx
    x**x
    xxxx
    """
    row_start = shp_coords[0][0] - 1 if shp_coords[0][0] - 1 > 0 else 0
    row_end = shp_coords[-1][0] + 1 if shp_coords[-1][0] + 1 < 9 else 9

    col_start = shp_coords[0][1] - 1 if shp_coords[0][1] - 1 > 0 else 0
    col_end = shp_coords[-1][1] + 1 if shp_coords[-1][1] + 1 < 9 else 9

    area = []
    for row in range(row_start, row_end + 1):
        for column in range(col_start, col_end + 1):
            area_point = (row, column)
            area.append(area_point)

    return area

field = Field()