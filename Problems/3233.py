"""MAIN LOTTERY"""

REAL = input()
GUESS = input()

LETTERREAL = REAL[0]
GUESSREAL = GUESS[0]

if REAL == GUESS:
    print("1000000")
elif GUESSREAL != LETTERREAL and REAL[2:8] == GUESS[2:8]:
    print("100000")
elif GUESSREAL == LETTERREAL and REAL[4:7] == GUESS[4:7]:
    print("2000")
elif GUESSREAL == LETTERREAL and REAL[5:7] == GUESS[5:7]:
    print("1000")
elif GUESSREAL != LETTERREAL and REAL[4:7] == GUESS[4:7]:
    print("200")
elif GUESSREAL != LETTERREAL and REAL[5:7] == GUESS[5:7]:
    print("100")
elif GUESSREAL == LETTERREAL:
    print("20")
else:
    print("0")
