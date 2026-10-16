"""RABBIT LANGUAGE"""
CHECK = input().upper()
LETTER = len(CHECK)
if all(c in "IT" for c in CHECK):
    print("unknown", LETTER)
else:
    BEST = 0
    COUNT = 0
    ERROR = -1
    for i in range(LETTER):
        AT = CHECK[i]
        if AT not in "RABIT":
            ERROR = i
            break
        if AT == "A":
            if not i or CHECK[i-1] not in "RA":
                ERROR = i
                break
            COUNT += 1
            BEST = max(BEST, COUNT)
        else:
            COUNT = 0
        if AT == "R" and (i == LETTER-1 or CHECK[i+1] != "A"):
            ERROR = i + 1 if i + 1 < LETTER else i
            break
        if AT == "B" and (i == LETTER-1 or CHECK[i+1] not in "IT"):
            ERROR = i + 1 if i + 1 < LETTER else i
            break
    if ERROR != -1:
        print("no", ERROR)
    else:
        print("yes", BEST)
