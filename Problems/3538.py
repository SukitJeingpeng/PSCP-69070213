"""B - FULLY PAIR?"""

TEXT = input().strip()

CHAR_COUNTS = {}
for CHAR in TEXT:
    CURRENT_COUNT = CHAR_COUNTS.get(CHAR, 0)
    CHAR_COUNTS[CHAR] = CURRENT_COUNT + 1

UNPAIRED_LETTERS = []
for CHAR, COUNT in CHAR_COUNTS.items():
    if COUNT % 2:
        UNPAIRED_LETTERS.append(CHAR)

if UNPAIRED_LETTERS:
    RESULT_STRING = "".join(UNPAIRED_LETTERS)
    print(RESULT_STRING)
else:
    print("fully paired")
