"""
 File: Field_generator.py
 This module generates field for game
 Created by Ivan Kosarevych
 07.02.16 13:50:56
"""

def generate_field():
    """
    :return: list(list)

    This function puts all ships on the field using func. generate_ship
    and make_ship_area
    """
    import random

    ships_size = [4, 3, 2, 1]

    # put 4xShip on field
    field = generate_ship(4)

    # put other ships
    # count is a quantity of each type of ship
    for count in range(1, len(ships_size)):
        # put as many ships of each type as required
        for i in range(count + 1):
            # generate ship and check whether it doesn't touch others,
            # otherwise regenerate it until it touches no other ship
            ship = generate_ship(ships_size[count])
            ship_area = make_shp_area(ship)
            while set(ship_area).intersection(set(field)) != set():
                ship = generate_ship(ships_size[count])
                ship_area = make_shp_area(ship)

            field.extend(ship)

    # make list of field in stars for part of ships and spaces for empty points
    res_field = []
    for i in range(10):
        row = []
        for j in range(10):
            if (i, j) in field:
                row.append('*')
            else:
                row.append(' ')
        res_field.append(row)

    return res_field


def generate_ship(size):
    """
    :param size: int
    :return: list(list)

    Generates coordinates for ship of given size
    Example for size 4: [(1,2),(1,3),(1,4),(1,5)]
    """
    import random

    # Choose rotation(horizontal/vertical)
    rotations = ['horizontal', 'vertical']
    rotation = random.choice(rotations)
    # Choose number of a row/column
    row_col = random.randrange(0, 10)
    # Choose first point of ship
    first_point = random.randrange(0, 10 - size)

    # find ship coordinates
    if rotation == 'horizontal':
        ship_coord = [(row_col, i) for i in range(first_point, first_point + size)]
    else:
        ship_coord = [(i, row_col) for i in range(first_point, first_point + size)]

    return ship_coord


def make_shp_area(shp_coords):
    """
    :param shp_coords: list
    :return: list

    Generates coordinates of area around a ship with this ship,
    where others ships aren't allowed to be placed
    Example:
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
