def open_file(filename):
    with open(filename, encoding="UTF-8") as f:
        return "".join(f.readlines())
