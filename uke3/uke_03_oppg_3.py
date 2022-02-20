
aar = float(input("Angi menneskeår: "))

utrekna = 0;

if aar <= 2:
    utrekna = aar*10.5
else:
    aar = aar-2.0
    utrekna = aar * 4.0 + 10.5*2;

print(f"Dette tilsvarer {utrekna:.1f} hundeår.")