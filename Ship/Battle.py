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


def convert_coordinates(coord):
    """
    Converts sea battle coordinates to coordinates in list of field
    Returns coord in list by given coord in sea battle
    """
    from string import ascii_uppercase

    sb_coords = [(let, i) for let in ascii_uppercase[:10] for i in range(1, 10 + 1)]
    my_coords = [(i, j) for i in range(10) for j in range(10)]

    rel = dict(zip(sb_coords, my_coords))

    try:
        return rel[coord]
    except:
        return

# print(convert_coordinates(('J',11)))
