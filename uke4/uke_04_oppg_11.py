binary = int(input("Binært tall: "))


binAsStr = str(binary)
binLen = len(binAsStr) - 1 #-1 pga vil ha med at siste teikn er potens 0 og ikke 1

buffer = 0

for i in binAsStr:
    if i == "1":
        buffer += 2**binLen

    binLen -= 1

print(buffer)