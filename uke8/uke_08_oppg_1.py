def pearson_corr(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    dx = [a - mean_x for a in x]
    dy = [a - mean_y for a in y]

    dxy = zip(dx, dy)
    dxy_multiplied = [a[0] * a[1] for a in dxy]

    sum_dxdy = sum(dxy_multiplied)

    dx2 = sum([a**2 for a in dx])
    dy2 = sum([a**2 for a in dy])

    sqr_dx2dy2 = (dx2 * dy2)**(1/2)

    return sum_dxdy / sqr_dx2dy2




