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


def read_field(filename):
    """
    :filename: str
    :return: list(list)
    """
    with open(filename, 'r') as file:
        field = []
        for line in file:
            field.append(list(line[:-1]))

    return field
#print(read_field('field.txt'))

def is_valid(field):
    """

    :param field: list(list)
    :return: bool
    """
    # req_sum should be 50
    req_sum = 0
    for i in range(10):
        for j in range(10):
            shp_size = ship_size(field,(i,j))
            if shp_size > 4:
                return False
            req_sum += shp_size
            #print((i,j), shp_size)
    #print(req_sum)
    return req_sum == 50
#print(is_valid(field))

def field_to_str(field):
    """
    Converts list of lists of field to string of field

    :param field: list(list)
    :return: str
    """
    output = ''
    for row in field:
        output += ''.join(row) + '\n'

    return output
#print(field_to_str(field))

def field_to_file(field):
    """
    Writes field in string to file

    :param field: str
    :return: None
    """
    with open('field.txt', 'w') as file:
        file.write(field)

#field_to_file(field_to_str(field))
