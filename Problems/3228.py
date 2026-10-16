"""MAIN"""

TEXT = input().lower()
VOWELS = ("a","e","i","o","u")
COUNT = 0

for i in TEXT:
    if i in VOWELS:
        COUNT += 1

print(COUNT)
