def get_coordinates():
    """
    input: A,1
    :return: tuple
    """
    btlshp_coord = input().split(',')
    btlshp_coord[-1] = int(btlshp_coord[-1])
    return tuple(btlshp_coord)


def convert_coordinates(coord):
    """
    Converts battleships coordinates to coordinates in list of field
    Returns coord in list by given coord in sea battle
    ('A',1) -> (0,0)
    """
    from string import ascii_uppercase

    sb_coords = [(let, i) for let in ascii_uppercase[:10] for i in range(1, 10 + 1)]
    my_coords = [(i, j) for i in range(10) for j in range(10)]

    rel = dict(zip(sb_coords, my_coords))

    try:
        return rel[coord]
    except:
        return


def has_ship(field, list_coord):
    """

    """
    #list_coord = convert_coordinates(coord)
    return field[list_coord[0]][list_coord[1]] != ' '

field = read_field('field.txt')
#print(has_ship(field, ('G',10)))


def ship_size(field, list_coord):
    """
    :param field:
    :param coord:
    :return:
    """
    #lst_coord = convert_coordinates(coord)
    row, column = list_coord[0],list_coord[1]
    if has_ship(field, list_coord):
        check = True
        # Ship in row
        if column + 1 <= 9 and field[row][column + 1] == '*':
            cur = column
            while field[row][cur] != ' ' and cur <= 9:
                cur += 1

            length = cur - column
            check = False

        if column - 1 >= 0 and field[row][column - 1] == '*':
            if check: length = 0

            cur = column
            while field[row][cur] != ' ' and cur >= 0:
                cur -= 1

            length += column - cur - 1 if not check else column - cur
            check = False

        # Ship in column
        if row + 1 <= 9 and field[row + 1][column] == '*':
            cur = row
            while field[cur][column] != ' ' and cur <= 9:
                cur += 1

            length = cur - row
            check = False

        if row - 1 >= 0 and field[row - 1][column] == '*':
            if check: length = 0
            cur = row
            while field[cur][column] != ' ' and cur >= 0:
                cur -= 1

            length += row - cur - 1 if not check else row - cur
            check = False

        if check: return 1
    else:
        length = 0

    return length
#print(field[2][4])
#field = read_field('field.txt')
#print(ship_size(field, (9,0)))





