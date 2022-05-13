import csv

with open("2019-06-01_Oslo.csv") as csvfile:
    datareader = csv.reader(csvfile, delimiter=" ")

    for row in datareader:
        print(row[0])