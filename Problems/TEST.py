"""MAIN"""

TEXT = input()

ANS = 1
FIND = False

for c in TEXT:
    if c > "0":  # ตรวจสอบว่าเป็นเลข '1' ถึง '9'
        ANS *= int(c)
        FIND = True

if FIND:
    print(ANS)
else:
    print(0)
