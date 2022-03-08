def draw_haiku_frame(r1, r2, r3):
    haiku = [r1, r2, r3]

    buffer = "";

    lineSize = len(max(haiku, key=len))

    border = "@" * (lineSize + 4);

    buffer += border + "\n"

    for line in haiku:
        lineSpaces = (lineSize - len(line)) * " "
        buffer += f"@ {lineSpaces}{line} @" + "\n"

    buffer += border + "\n"

    return buffer