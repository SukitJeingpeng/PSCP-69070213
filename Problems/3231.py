"""ROLLL !"""

GUESS = int(input())
REAL = int(input())

if 0 < GUESS < 7 and 0 < REAL < 7:
    if GUESS == REAL:
        print("Correct!")
    else:
        print("Wrong!")
else:
    print("Invalid")
