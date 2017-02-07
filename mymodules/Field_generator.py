

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

#field = generate_field()############################


#print(is_valid(field))