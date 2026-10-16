"""SHORTEN"""

NUMS = []
while True:
    VAL = int(input())
    if VAL == -1:
        break
    NUMS.append(VAL)

if NUMS:
    RANGES = []
    START = NUMS[0]
    PREV = NUMS[0]

    for x in NUMS[1:]:
        if x == PREV + 1:
            PREV = x
        else:
            if START == PREV:
                RANGES.append(str(START))
            else:
                RANGES.append(f"{START}-{PREV}")
            START = x
            PREV = x

    if START == PREV:
        RANGES.append(str(START))
    else:
        RANGES.append(f"{START}-{PREV}")

    print(", ".join(RANGES))
