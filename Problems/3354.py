"""LUCKY NUMBER"""

OP_U, VAL_U = input().split()
OP_T, VAL_T = input().split()
OP_H, VAL_H = input().split()

VAL_U = int(VAL_U)
VAL_T = int(VAL_T)
VAL_H = int(VAL_H)

VALID_H = []
if OP_H == "==":
    VALID_H = [VAL_H]
elif OP_H == "!=":
    VALID_H = [d for d in range(10) if d != VAL_H]
elif OP_H == ">":
    VALID_H = list(range(VAL_H + 1, 10))
elif OP_H == "<":
    VALID_H = list(range(VAL_H))
elif OP_H == ">=":
    VALID_H = list(range(VAL_H, 10))
elif OP_H == "<=":
    VALID_H = list(range(VAL_H + 1))

VALID_T = []
if OP_T == "==":
    VALID_T = [VAL_T]
elif OP_T == "!=":
    VALID_T = [d for d in range(10) if d != VAL_T]
elif OP_T == ">":
    VALID_T = list(range(VAL_T + 1, 10))
elif OP_T == "<":
    VALID_T = list(range(VAL_T))
elif OP_T == ">=":
    VALID_T = list(range(VAL_T, 10))
elif OP_T == "<=":
    VALID_T = list(range(VAL_T + 1))

VALID_U = []
if OP_U == "==":
    VALID_U = [VAL_U]
elif OP_U == "!=":
    VALID_U = [d for d in range(10) if d != VAL_U]
elif OP_U == ">":
    VALID_U = list(range(VAL_U + 1, 10))
elif OP_U == "<":
    VALID_U = list(range(VAL_U))
elif OP_U == ">=":
    VALID_U = list(range(VAL_U, 10))
elif OP_U == "<=":
    VALID_U = list(range(VAL_U + 1))

for h in VALID_H:
    for t in VALID_T:
        for u in VALID_U:
            print(f"{h}{t}{u}")
