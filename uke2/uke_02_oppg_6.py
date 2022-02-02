haiku = [input("Første raden: "), input("Andre raden: "), input("Tredje raden: ")]

print()

lineSize = len(max(haiku, key=len))

border = "@" * (lineSize+4);

print(border)

for line in haiku:
    lineSpaces = (lineSize-len(line)) * " "
    print(f"@ {lineSpaces}{line} @")

print(border)