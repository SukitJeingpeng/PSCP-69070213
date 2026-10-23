"""DIGITV3"""

NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

RAW_INPUT = input().strip()
WORDS = RAW_INPUT.lower().replace("-", " ").split()

TOTAL = 0
CURRENT = 0

for word in WORDS:
    if word == "thousand":
        if not CURRENT:
            CURRENT = 1
        CURRENT *= 1000
        TOTAL += CURRENT
        CURRENT = 0
    elif word == "hundred":
        if not CURRENT:
            CURRENT = 1
        CURRENT *= 100
    elif word in NUMBER_WORDS:
        CURRENT += NUMBER_WORDS[word]

TOTAL += CURRENT

print(TOTAL)
