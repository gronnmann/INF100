from datetime import date

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

counter = 0

for d_ordinal in range(start_date.toordinal(), end_date.toordinal()):  # Stack Overflow,
    # https://stackoverflow.com/questions/43692340/how-to-find-number-of-mondays-or-any-other-weekday-between-two
    # -dates-in-python/43692481, 21.04.2022
    to_date = date.fromordinal(d_ordinal)

    if to_date.weekday() == 4 and to_date.day == 2:
        counter += 1

print(counter)
