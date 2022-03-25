def sonar_depth_increase_cnt(sonar_depths_ticker):
    to_depth_list = [int(x) for x in sonar_depths_ticker.split(" ")]

    counter = 0

    for i, depth in enumerate(to_depth_list):
        what_happened = "N/A - no previous measurement"

        if i > 0:
            if to_depth_list[i - 1] < depth:
                counter += 1
                what_happened = "increased"
            elif to_depth_list[i - 1] == depth:
                what_happened = "no change"
            else:
                what_happened = "decreased"

        print(f"{depth} ({what_happened})")

    return counter


def sonar_depth_increase_cnt_avg(sonar_depths_ticker):
    to_depth_list = [int(x) for x in sonar_depths_ticker.split(" ")]

    three_vals = []

    for i in range(len(to_depth_list) - 2):
        three_vals.append(to_depth_list[i] + to_depth_list[i + 1] + to_depth_list[i + 2])

    return sonar_depth_increase_cnt(" ".join([str(x) for x in three_vals]))
