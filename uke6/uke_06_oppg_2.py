

def find_highest(coords_list):
    best_index = [0, 0]

    for x in range(len(coords_list)):
        coords = coords_list[x]

        if coords[1] > best_index[1]:
            best_index = [x, coords[1]]

    return best_index[0]

