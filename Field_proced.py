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
        print('1,',length)

        cur = column
        try:
            while field[row][cur] != ' ':
                cur -= 1
        except:
            pass
        length += column - cur - 1
        print('2,',length)
        if length > 1: return  length

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
        print(length)
    else:
        length = 0

    return length
#print(field[2][4])
field = read_field('field.txt')
print(ship_size(field, (6,0)))


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
            print((i,j), shp_size)
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

    return output
#print(field_to_str(field))


def generate_field():
    """

    :return:
    """
    import random

    ships_size = [4,3,2,1]

    field = generate_ship(4)

    #count is a quantity of each type of ship
    for count in range(1, len(ships_size)):
        for i in range(count + 1):
            ship = generate_ship(ships_size[count])
            ship_area = make_shp_area(ship)
            while set(ship_area).intersection(set(field)) != set():
                ship = generate_ship(ships_size[count])
                ship_area = make_shp_area(ship)

            field.extend(ship)

    # make list of field in stars and spaces
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

    :return: list
    """
    import random

    # Choose rotation(horizontal/vertical)
    rotations = ['horizontal', 'vertical']
    rotation = random.choice(rotations)
    row_col = random.randrange(0,10)
    first_point = random.randrange(0, 10 - size)

    # find ship coordinates
    if rotation == 'horizontal':
        ship_coord = [(row_col, i) for i in range(first_point, first_point + size)]
    else:
        ship_coord = [(i, row_col) for i in range(first_point, first_point + size)]

    return ship_coord


def make_shp_area(shp_coords):
    """

    :param shp_coords:
    :return:
    """
    row_start = shp_coords[0][0] - 1 if shp_coords[0][0] - 1 > 0 else 0
    #print(row_start)
    row_end = shp_coords[-1][0] + 1 if shp_coords[-1][0] + 1 < 9 else 9
    #print(row_end)
    col_start = shp_coords[0][1] - 1 if shp_coords[0][1] - 1 > 0 else 0
    #print(col_start)
    col_end = shp_coords[-1][1] + 1 if shp_coords[-1][1] + 1 < 9 else 9

    area = []
    for row in range(row_start, row_end + 1):
        for column in range(col_start, col_end + 1):
            area_dot = (row,column)
            area.append(area_dot)

    return area

#make_shp_area([(0,9),(1,9)])
#field = generate_field()############################
#print(field_to_str(field))
#print(is_valid(field))

'''count = 0
for i in range(1000):
    if is_valid(generate_field()):
        count += 1

print(count)'''

def field_to_file(field):
    with open('field.txt', 'w') as file:
        file.write(field)

#field_to_file(field_to_str(field))
#print(is_valid(field))