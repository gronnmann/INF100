def line_best_fit(coords):
    split_coords = list(zip(*coords))

    #print(f"Coords: {coords}, split: {split_coords}")

    split_x = split_coords[0]
    split_y = split_coords[1]

    n = len(split_x)

    #print(f"xCoords: {split_x}, yCoords: {split_y}, varNum: {n}")

    sum_x = float(sum(split_x))
    avg_x = sum_x / n

    sum_y = float(sum(split_y))
    avg_y = sum_y / n

    #print(f"Coords: {coords}, sumX: {sum_x}, avgX: {avg_x}, sumY: {sum_y}, avgY: {avg_y}")

    sigma_xy_packed = [c[0] * c[1] for c in coords]
    sigma_xy = sum(sigma_xy_packed)
    #print(f"Sigma xy: {sigma_xy_packed}, sum: {sigma_xy}")

    sigma_x2 = sum(c**2 for c in split_x)

    mTop = sigma_xy - ( (sum_x * sum_y) / (n)  )
    mBottom = sigma_x2 - ( (sum_x**2) / n  )

    m = mTop / mBottom

    #print(f"mValues: mTop: {mTop}, mBot: {mBottom}, totalM: {m}")

    b = avg_y - m * avg_x

    #print(f"b: {b}")

    to_append = ""

    if b > 0.0:
        to_append = f"+ {b:.2f}"

    return f"y = {m:.2f}x" + to_append


coord_1 = ((1, 1), (2, 2.1), (3, 2.9))
print(line_best_fit(coord_1))


coord_2 = ((0, 0), (1, 1), (2, 2), (3, 3))
print(line_best_fit(coord_2))