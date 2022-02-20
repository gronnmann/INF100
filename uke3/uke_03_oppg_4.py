ord = [input("Skriv et ord: "), input("Skriv et annet ord: "), input("Skrive et siste ord: ")]



maxLen = 0;
for x in ord:
    ordLen = len(x)
    if ordLen > maxLen:
        lengstOrd = []
        maxLen = ordLen
        lengstOrd = x

print(f"\n{lengstOrd}")