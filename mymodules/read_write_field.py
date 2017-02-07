"""
File: Read_write_field.py
This module reads a field from text file, checks field validity,
converts field in list to field in string, writes field in string to text file
Created by Ivan Kosarevych
05.02.16 17:57:12
"""

from field_info import ship_size


def read_field(filename):
    """
    :filename: str
    :return: list(list)

    Reads field from file and puts it into list of lists,
    each list is a row on field, each element in inner lists is a point
    """
    with open(filename, 'r') as file:
        field = []
        for line in file:
            field.append(list(line[:-1]))

    return field


def is_valid(field):
    """
    :param field: list(list)
    :return: bool

    Checks whether field has 1 4xShip, 2 3xShips, 3 2xShips, 4 1xShips
    and whether there are no 5&moreXships
    """
    # req_sum should be 50(4*4*1 + 3*3*2 + 2*2*3 + 1*1*4)
    req_sum = 0
    for i in range(10):
        for j in range(10):
            shp_size = ship_size(field, (i, j))[1]
            if shp_size > 4:
                return False
            req_sum += shp_size

    return req_sum == 50


def field_to_str(field):
    """
    :param field: list(list)
    :return: str

    Converts list of lists of field to string of field
    """
    output = ''
    for row in field:
        output += ''.join(row) + '\n'

    return output


def field_to_file(field):
    """
    Writes field in string to file

    :param field: str
    :return: None
    """
    with open('field.txt', 'w') as file:
        file.write(field)
