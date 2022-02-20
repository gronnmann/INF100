import math

startPos = float(input("Stenen droppes fra høyde: "))
tid = 0

y = startPos

while y > 0:
    print(f"{y:.1f} m")

    tid += 1

    y = startPos - (1/2)* 9.81 * tid**2

print("0 m")

nedreGrense = tid-1 #-1 pga at print kommer før tid+1 og dermed 1 sekund feil

print(f"Stenen lander mellom {nedreGrense} og {nedreGrense+1} sekunder etter at den droppes.")
