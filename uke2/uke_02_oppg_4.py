info = [input("Hva er ditt navn? "), input("Hva er din adresse? "), input("Hva er ditt postnummer og poststed? ")]
print(len(max(info, key=len)))