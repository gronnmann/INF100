def render_histogram(values):
    max_size = max(values)

    buffer = ""

    for i in range(max_size):
        for j in values:
            to_draw = max_size - j  # dersom høgde er 5 og max 10 - bør være mellomrom de første 5 verdiane, så stjerne dei neste 5

            if i >= to_draw:
                buffer += "*"
            else:
                buffer += " "

        buffer += "\n"

    return buffer.rstrip("\n") #fjern siste \n
