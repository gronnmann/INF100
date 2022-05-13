def write_turtle_str(file_in):
    buffer = ["import turtle as t"]

    # try:
    #     f = open(file_in, "r")
    # except FileNotFoundError:
    #     return None

    with open(file_in, "r", encoding="UTF-8") as f:
        for line in f:
            split = line.split()

            if split[0] == "up" or split[0] == "down":
                buffer.append(f"t.{split[0]}()")
            else:
                buffer.append(f"t.{split[0]}({split[1]})")

    buffer.append("t.done()")

    return "\n".join(buffer).strip()


def turtle_file_out(turtle_str, file_out):
    with open(file_out, "w", encoding="UTF-8") as f:
        f.write(turtle_str)
