'''MAIN'''

NAME = input()
SURNAME = input()
OLD = input()

if len(NAME) >= 5 and len(SURNAME) >= 5:
    print(f"{NAME[0]}{NAME[1]}{SURNAME[-1]}{OLD[-1]}")
else:
    print(f"{NAME[0]}{OLD}{SURNAME[-1]}")
