i = 1
switched = False

while i > 0:
    print("--"*i + "*")

    i = i - 1 if switched else i + 1

    if i >= 5:
        switched = not switched
