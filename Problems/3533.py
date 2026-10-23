"""HORIZONTAL HISTOGRAM"""

TEXT = input()

COUNTS = {}
for char in TEXT:
    if char in COUNTS:
        COUNTS[char] += 1
    else:
        COUNTS[char] = 1

LOWER_CHARS = []
UPPER_CHARS = []

for char in COUNTS:
    if char.islower():
        LOWER_CHARS.append(char)
    elif char.isupper():
        UPPER_CHARS.append(char)

LOWER_CHARS.sort()
UPPER_CHARS.sort()

ALL_CHARS = LOWER_CHARS + UPPER_CHARS

for char in ALL_CHARS:
    FREQ = COUNTS[char]
    BAR = ""
    for i in range(1, FREQ + 1):
        BAR += "-"
        if not i % 5 and i < FREQ:
            BAR += "|"
    print(f"{char} : {BAR}")
