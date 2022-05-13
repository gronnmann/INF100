commands = {
    "forward": (1, 0),
    "down": (0, 1),
    "up": (0, -1)
}


def add_coords(coordinate_list, direction, how_far):
    try:
        coordinate_list[0] += direction[0] * how_far
        coordinate_list[1] += direction[1] * how_far

    except Exception:
        return None


def sub_course_positions(path):
    coords = [0, 0]

    try:
        f = open(path, "r")
    except FileNotFoundError:
        return {
            "forward": 0,
            "depth": 0,
        }

    with open(path, "r", encoding="UTF-8") as f:
        for line in f:
            direction, how_far = line.split()

            add_coords(coords, commands.get(direction), int(how_far))

    return {
        "forward": coords[0],
        "depth": coords[1]
    }


def sub_course(path):
    coords = sub_course_positions(path)

    return coords["forward"] * coords["depth"]
