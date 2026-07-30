"""TICKET"""

OLD = int(input())
STATUS = input().lower()

if OLD < 18 or STATUS == "s":
    print("20")
else:
    print("50")
