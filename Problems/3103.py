"""VOWELS"""

CHECK = int(input())
VOWELS = ["A","E","I","O","U"]
COUNT = 0

for i in range(CHECK):
    i = input().upper()
    if i in VOWELS:
        COUNT += 1

print(COUNT)
