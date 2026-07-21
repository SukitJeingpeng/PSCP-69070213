"""MAIN Temperature"""

TEMPERATURE = float(input())
TEMPERATURE1 = input()
TEMPERATURE2 = input()
C = 0

if TEMPERATURE1 == "C":
    C = TEMPERATURE
elif TEMPERATURE1 == "K":
    C = TEMPERATURE - 273.15
elif TEMPERATURE1 == "F":
    C = ((TEMPERATURE  - 32) * 5) / 9
elif TEMPERATURE1 == "R":
    C = (TEMPERATURE * 5) / 9 - 273.15

if TEMPERATURE2 == "K":
    print(f"{C + 273.15:.2f}")
elif TEMPERATURE2 == "F":
    print(f"{(C * 9) / 5 + 32:.2f}")
elif TEMPERATURE2 == "R":
    print(f"{(C + 273.15) * 9 / 5:.2f}")
else:
    print(f"{C:.2f}")
