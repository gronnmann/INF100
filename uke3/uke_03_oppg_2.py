aar = int(input("Angi år: "))

if (aar % 4 == 0 and aar % 100 != 0) or aar % 400 == 0:
    print("Dette er et skuddår")
else:
    print("Dette er ikke et skuddår")