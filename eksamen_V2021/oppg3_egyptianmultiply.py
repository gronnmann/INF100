tall_1 = int(input("Tall 1: "))
tall_2 = int(input("Tall 2: "))
a = max(1, min(tall_1, tall_2))
b = min(99, max(tall_1, tall_2))


print(f"Factor A: {a}")
print(f"Factor B: {b}")

selected_numbers = []

while a > 0:
    temp_x2 = 1
    temp_x2_to_remove = 1

    while temp_x2 <= a:
        temp_x2_to_remove = temp_x2
        temp_x2 *= 2

    selected_numbers.append(temp_x2_to_remove)
    a -= temp_x2_to_remove

how_many_times = round(selected_numbers[0] ** (1/2)) + 1

structure = []

for i in range(0, how_many_times):
    structure.append(
        (
            2**i,
            2**i in selected_numbers,
            2**i * b
        )
    )

print("==============")

for line in structure:
    print("{:<1}\t{:<2}\t{:<4}".format(
        "X" if line[1] else "",
        line[0],
        line[2],
    ))

print("==============")
sum_a = [x[0] for x in structure if x[1]]
sum_b= [x[2] for x in structure if x[1]]

c = sum(sum_a)
d = sum(sum_b)

print(f"{' + '.join([str(x) for x in sum_a])} = {c}")
print(f"{' + '.join(str(x) for x in sum_b)} = {d}")

print("==============")

print(f"{c} * {b} = {d}")