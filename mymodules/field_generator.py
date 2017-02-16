"""
 File: Field_generator.py
 This module generates field for game
 Created by Ivan Kosarevych
 07.02.16 13:50:56
"""

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
