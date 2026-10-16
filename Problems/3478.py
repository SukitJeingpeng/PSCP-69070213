"""HISTOGRAM"""

TEXT = input()

for i in range(26):
    LOWER = chr(ord("a") + i)
    UPPER = chr(ord("A") + i)
    if LOWER in TEXT:
        print(f"{LOWER} = {TEXT.count(LOWER)}")
    if UPPER in TEXT:
        print(f"{UPPER} = {TEXT.count(UPPER)}")
