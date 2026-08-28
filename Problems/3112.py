"""CHANOMKAIMOOK"""

PTYPE, PGRAM = input().split()
PGRAM = float(PGRAM)

TTYPE, SWEETNESS, TEACC = input().split()
SWEETNESS = int(SWEETNESS)
TEACC = float(TEACC)

if PTYPE == "H":
    PEARL = PGRAM * 5
elif PTYPE == "O":
    PEARL = PGRAM * 3
elif PTYPE == "J":
    PEARL = PGRAM * 2
else:
    PEARL = 0

rate = 0
if TTYPE == "R":
    if SWEETNESS == 1:
        rate = 12
    elif SWEETNESS == 2:
        rate = 18
    elif SWEETNESS == 3:
        rate = 25
elif TTYPE == "T":
    if SWEETNESS == 1:
        rate = 15
    elif SWEETNESS == 2:
        rate = 20
    elif SWEETNESS == 3:
        rate = 30
elif TTYPE == "M":
    if SWEETNESS == 1:
        rate = 10
    elif SWEETNESS == 2:
        rate = 15
    elif SWEETNESS == 3:
        rate = 20

TEA = TEACC * rate

TOTAL = PEARL + TEA

if TOTAL.is_integer():
    print(int(TOTAL))
else:
    print(TOTAL)
