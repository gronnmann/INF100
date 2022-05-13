week_precip = {
  "monday": 0,
  "tuesday": 0.7,
  "wednesday": 0,
  "thursday": 4.7,
  "friday": 10
}

week_temps = [7.0, 8.0, 10.0, 9.0, 10.0]

print("Dictionary Keys:")

for keys in week_precip.keys():
  print(keys)

print()
print("Dictionary Values:")

for values in week_precip.values():
  print(values)

print()
print("Dictionary keys/value:")

for key, value in week_precip.items():
  print(f"{key} {value}")

print()
print("List values:")

for value in week_temps:
  print(value)

print()
print("List indices/value:")

for i, value in enumerate(week_temps):
  print(f"{i} {value}")

