"""CALCULATOR V2"""

N = int(input())

if N == 1:
    print(1)
else:
    TOTAL_DIGITS = 0
    POWER_OF_TEN = 1

    while POWER_OF_TEN <= N:
        NUMBERS_COUNT = N - POWER_OF_TEN + 1
        TOTAL_DIGITS += NUMBERS_COUNT
        POWER_OF_TEN *= 10

    TOTAL_PRESSES = TOTAL_DIGITS + N
    print(TOTAL_PRESSES)
