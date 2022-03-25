def generate_a_array(tall):
    arr = []
    i = 1
    while i < tall:
        arr.append(i)
        i = i * 2

    return arr


def generate_b_array(tall, iterations):
    arr = []
    for i in range(iterations):
        arr.append(tall)
        tall = tall * 2

    return arr


def generate_marked_array(tall, tall_array):
    # array blir [bool_1, bool_2, ..., bool_n] der n er lengda på tall_array
    arr = []

    for i in range(len(tall_array)):
        arr.append(False)

    for i in range(len(tall_array) - 1, -1, -1):
        curr_num = tall_array[i]

        # print(f"Tall: {tall}, Tall_array: {tall_array}, i: {i}, currNum: {curr_num}")

        if curr_num <= tall:
            arr[i] = True
            tall = tall - curr_num

            if tall <= 0:
                break

    return arr


# tall_input = [19, 23]
tall_input = [int(input("Factor A: ")), int(input("Factor B: "))]
tall_input.sort()

a = tall_input[0]
b = tall_input[1]

a_array = generate_a_array(a)
b_array = generate_b_array(b, len(a_array))

marked_a = generate_marked_array(a, a_array)

# print(f"A: {a}, B: {b}")

print("=========================")

for j, aVal in enumerate(a_array):
    # print(f"{'X' if marked_a[i] else ''} \t {aVal} \t {b_array[i]}")

    print("{:>1}\t{:<2}\t{:<2}".format('X' if marked_a[j] else '', aVal, b_array[j]))

print("=========================")

zipped = list(zip(a_array, b_array, marked_a))
zipped_only_true = [(x[0], x[1]) for x in zipped if x[2]]

unzipped = list(zip(*zipped_only_true))

# print(f"Zipped: {zipped}")
# print(f"TrueZipped: {zipped_only_true}")
# print(f"Unzipped: {unzipped}")

unzipped_a = unzipped[0]
unzipped_b = unzipped[1]

sum_a = sum(unzipped_a)
sum_b = sum(unzipped_b)

print(f"{' + '.join([str(x) for x in unzipped_a])} = {sum_a}")
print(f"{' + '.join([str(x) for x in unzipped_b])} = {sum_b}")

print("=========================")

print(f"{a} * {b} = {a * b}")
