def open_file(filename):

    with open(filename, "r+", encoding="UTF-8") as f:

        lines = [f">>>{x.strip()}<<<\n" for x in f.readlines()]

        f.seek(0)

        f.writelines(lines)

        return "".join(lines)


    # with open(filename, "w", encoding="UTF-8") as f:
    #     f.writelines(buffer)