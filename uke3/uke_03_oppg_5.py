oktav4 = [440.00, 493.88, 261.63, 293.66, 329.63, 349.23, 392.00] # A, B, C, D, E, F, G

note = input("Enter note: ").upper()
octave = float(input("Enter octave: "))

noteIndex = ord(note) - 65 #Konverterer til ASCII nummer


hz = oktav4[noteIndex] / (2**(4-octave))
print(f"{note}{octave:.0f} is {hz} Hz.")