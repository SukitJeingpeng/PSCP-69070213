"""PICK THEM AGAIN !"""

NUMBERS = list(map(int, input().split()))
FOUND = False

for NUM in NUMBERS[::-1]:
    if not NUM % 3 or not NUM % 5:
        print(NUM)
        FOUND = True

if not FOUND:
    print("Nope")
