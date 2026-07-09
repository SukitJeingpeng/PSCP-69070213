'''MAIN'''

A = input()
B = int(input())

if A == "H" and B == 4567:
    print("safe unlocked")
elif A == "H" and B != 4567:
    print("safe locked - change digit")
elif A != "H" and B == 4567:
    print("safe locked - change char")
else:
    print("safe locked")
