"""PASSWORD KEY"""

SCHOOL = input()
FIRST = ord(SCHOOL[0].upper())
LAST = ord(SCHOOL[-1].upper())
n = len(SCHOOL)

ANSLIST = []

for i in range(10):
    if not i or not i % 2:
        ANSLIST.append(((i + FIRST) % n) % 10)
    else:
        ANSLIST.append(((LAST - i) % n) % 10)

print(*ANSLIST[2:8])
