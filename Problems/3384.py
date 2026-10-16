"""PICKTHEM"""

TEXT = input().replace("[", "").replace("]", "").strip()
FOUND = False

if TEXT:
    for x in TEXT.split(","):
        VAL = int(x.strip())
        if not VAL % 2:
            print(VAL)
            FOUND = True

if not FOUND:
    print("Nope")
