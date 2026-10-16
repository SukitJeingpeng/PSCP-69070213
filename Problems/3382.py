"""Day08-0_02-Backward"""

LINES = []

while True:
    DATA = input()
    if DATA == "NULL":
        break
    LINES.append(DATA)

for x in reversed(LINES):
    print(x)
