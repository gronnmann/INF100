def line_best_fit(coords):
    split_coords = list(zip(*coords))

    split_x = split_coords[0]
    split_y = split_coords[1]

    n = len(split_x)

    print(f"xCoords: {split_x}, yCoords: {split_y}, varNum: {n}")

    sum_x = float(sum(split_x))
    avg_x = sum_x / n

    sum_y = float(sum(split_y))
    avg_y = sum_y / n

    print(f"Coords: {coords}, sumX: {sum_x}, avgX: {avg_x}, sumY: {sum_y}, avgY: {avg_y}")


    mTop = sum_x * sum_y - ( (sum_x + sum_y) / (n)  )
    mBottom = sum_x**2 - ( (sum_x**2) / n  )

    m = mTop / mBottom

    print(f"mValues: mTop: {mTop}, mBot: {mBottom}, totalM: {m}")

    b = avg_y - m * avg_x

    print(f"b: {b}")


coord_1 = ((1, 1), (2, 2.1), (3, 2.9))
line_best_fit(coord_1)

print("=========")

coord_2 = ((0, 0), (1, 1), (2, 2), (3, 3))
line_best_fit(coord_2)