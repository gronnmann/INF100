# Eksamen V2020, oppg 13
old_names = ["qwghlm.txt","qwerty.txt"]

for names in old_names:

    title = ""
    data = []

    with open(names, "r", encoding="UTF-8") as file:
        lines = file.readlines()

        title = lines[1].strip() + "_" + lines[0].strip() + ".txt"

        data = lines[2:]

    with open(title, "w", encoding="UTF-8") as file:
        file.writelines(data)