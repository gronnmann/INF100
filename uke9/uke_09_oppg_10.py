import math

numbers = {  # 0,1,2,3,12 og 10 henta fra Eksempel 4
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def number_name(n):
    if n > 1000:  # Kunstig avgrenser til 1000
        return None

    if n == 1000:
        return "one thousand"

    start_string = ""

    hundreds = math.floor(n / 100)

    n = n % 100

    # manage hundreds
    if hundreds > 0:
        start_string += f"{numbers[hundreds]} {numbers[100]}"  # ... hundred

        if n != 0:  # ... hundred and ...
            start_string += " and "

    # manage tens
    tens = math.floor(n / 10)
    n = n % 10

    if tens > 0:

        if tens == 1:
            start_string += f"{numbers[tens * 10 + n]}"  # annleis for talla under 20 (eleven, twelve, thirteen osv og
            # ikkje ten-one, ten-two osv)
        else:
            start_string += f"{numbers[tens * 10]}"  # twenty, thirty, forty, osv

            if n != 0:
                start_string += f"-{numbers[n]}" # x-one, x-two, x-three, osv

    else:
        if n != 0:
            start_string += numbers[n] # one, two, three, osv, enkle tall

    return start_string


def chars_in_number(n):
    return len(number_name(n).replace(" ", "").replace("-", ""))


def all_numbernames(n):
    buffer = 0

    for i in range(1, n + 1):
        buffer += chars_in_number(i)

    return buffer


def solve_euler_17():
    return all_numbernames(1000)

# print(number_name(342) + " | " + number_name(115))
# print(f"{chars_in_number(342)} , {chars_in_number(115)}")
#
# print(all_numbernames(5))
# print(solve_euler_17())

# for i in range(0, 11):
#     print(f"{i} : {number_name(i)}")
#
# for i in range(0, 100, 10):
#     print(f"{i} : {number_name(i)}")
#
# for i in range(0, 1000, 100):
#     print(f"{i} : {number_name(i)}")
#
# for i in range(0, 11):
#     r = random.randrange(0, 1000)
#     print(f"{r} : {number_name(r)}")
