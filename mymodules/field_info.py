"""
File: Field_info.py
This module consists functions which give information about the field,
such as CHECK whether the point on field has a ship AND length of ship in point SEARCH
Created by Ivan Kosarevych
07.02.16 09:11:35
"""

def convert_coordinates(coord):
    """
    :coord: tuple
    :return: tuple

    Converts battleships coordinates to coordinates in list of field
    Returns coordinates in list by given coordinates in battleship
    ('A',1) -> (0,0)
    """
    from string import ascii_uppercase

    sb_coords = [(let, i) for let in ascii_uppercase[:10] for i in range(1, 10 + 1)]
    my_coords = [(i, j) for i in range(10) for j in range(10)]

    rel = dict(zip(sb_coords, my_coords))

    try:
        return rel[coord]
    except IndexError:
        return


def has_ship(field, list_coord):
    """
    :param field: list(list)
    :param list_coord: tuple
    :return: bool
    """
    return field[list_coord[0]][list_coord[1]] != ' '


def ship_size(field, list_coord):
    """
    :param field: list(list)
    :param list_coord: tuple
    :return: tuple

    Example: 1X4 ship will return (1,4)
    """
    row, column = list_coord[0], list_coord[1]
    if has_ship(field, list_coord):
        check = True
        orientation = 'row'
        # Ship in row
        # Go right in row
        if column + 1 <= 9 and field[row][column + 1] == '*':
            cur = column
            while field[row][cur] != ' ' and cur <= 9:
                cur += 1

            length = cur - column
            check = False

        # Go left in row
        if column - 1 >= 0 and field[row][column - 1] == '*':
            if check: length = 0

            cur = column
            while field[row][cur] != ' ' and cur >= 0:
                cur -= 1

            length += column - cur - 1 if not check else column - cur
            check = False

        # Ship in column
        # Go up in column
        if row + 1 <= 9 and field[row + 1][column] == '*':
            orientation = 'column'
            cur = row
            while field[cur][column] != ' ' and cur <= 9:
                cur += 1

            length = cur - row
            check = False

        # Go down in column
        if row - 1 >= 0 and field[row - 1][column] == '*':
            orientation = 'column'
            if check: length = 0
            cur = row
            while field[cur][column] != ' ' and cur >= 0:
                cur -= 1

            length += row - cur - 1 if not check else row - cur
            check = False

        if check: return (1, 1)
    else:
        return (0, 0)

    return (1, length) if orientation == 'row' else (length, 1)
