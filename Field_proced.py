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
    Converts sea battle coordinates to coordinates in list of field
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

#list_coordinates = convert_coordinates(get_coordinates())
#print(list_coordinates)
# print(convert_coordinates(('J',11)))

def read_field(filename):
    """
    Returns 
    """
    with open(filename, 'r') as file:
        field = []
        for line in file:
            field.append(list(line[:-1]))

    return field


# print(read_field('field.txt'))


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
        # Ship in row
        cur = column
        try:
            while field[row][cur] != ' ':
                cur += 1
        except:
            pass
        length = cur - column

        cur = column
        try:
            while field[row][cur] != ' ':
                cur -= 1
        except:
            pass
        length += column - cur - 1
        if length != 1: return  length

        # Ship in column
        cur = row
        try:
            while field[cur][column] != ' ':
                cur += 1
        except:
            pass
        length = cur - row

        cur = row
        try:
          while field[cur][column] != ' ':
              cur -= 1
        except:
            pass
        length += row - cur - 1
    else:
        length = 0

    return length
#print(field[2][4])
#print(ship_size(field, (2,4)))


def is_valid(field):
    """

    :param field:
    :return:
    """
    # req_sum should be 50
    req_sum = 0
    for i in range(10):
        for j in range(10):
            shp_size = ship_size(field,(i,j))
            if shp_size > 4:
                return False
            req_sum += shp_size
            print(i,j,req_sum)
    print(req_sum)
    return req_sum == 50
#print(is_valid(field))


def field_to_str(field):
    """

    :param field:
    :return:
    """
    output = ''
    for row in field:
        output += ''.join(row) + '\n'

    return  output
#print(field_to_str(field))


def generate_field():
    """

    :return:
    """
    import random

