tid = 0
temp = 25.0

progress = 0.625

while temp < 100.0:
    print(f"{tid}s = {temp:.1f}°C")

    temp = temp + progress
    tid += 1

print(f"100.0°C i {round(tid/10)*10} sekunder")