def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Length mismatch")

    return sum([x[0] * x[1] for x in zip(a, b)])
