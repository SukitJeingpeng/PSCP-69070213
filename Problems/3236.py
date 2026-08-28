"""TECPASS"""

LONGLEN = int(input())
PASS1 = input()
PASS2 = input()
FALSESSS = 0

for i in range(LONGLEN):
    if int(PASS1[i]) + int(PASS2[i]) == 9:
        FALSESSS += 0
    else:
        FALSESSS += 1

if FALSESSS >= 1:
    print(f"NO {FALSESSS}")
else:
    print("YES")
