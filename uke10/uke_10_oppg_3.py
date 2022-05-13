def r_w_file(infile, outfile):
    temps = []
    with open(infile, "r", encoding="UTF-8") as f:
        for line in f:
            day, temp = line.split()
            temps.append((day, float(temp)))

    temps = [x for x in temps if x[1] >= 23.5]

    with open(outfile, "w", encoding="UTF-8") as f:
        f.writelines([f"{x[0]} {x[1]}\n" for x in temps])
