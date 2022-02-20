ord = [input("Skriv et ord: "), input("Skriv et annet ord: "), input("Skrive et siste ord: ")]


lengstOrd = []


maxLen = 0;
for x in ord:
    ordLen = len(x)
    if ordLen > maxLen:
        lengstOrd = []
        maxLen = ordLen
        lengstOrd.append(x)
    elif ordLen == maxLen:
        lengstOrd.append(x)

print()
for x in lengstOrd:
    print(x)