def first_letter_last_word(filename):
    with open(filename, "r") as f:
        words = [x.split(" ")[-1] for x in f.readlines()]

        return "".join([x[0] for x in words])
