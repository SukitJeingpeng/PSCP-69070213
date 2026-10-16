"""ARRAY HAHA"""

ARRAY = [0] * 50

for i in range(3):
    ARRAY[i] = int(input())
    print(f"Input number {i + 1} stored.")

while True:
    MENU = int(input())
    if not MENU:
        break
    if MENU == 1:
        print(f"Original order: {ARRAY[0]} {ARRAY[1]} {ARRAY[2]}")
    elif MENU == 2:
        DESC = sorted(ARRAY[:3], reverse=True)
        print(f"Descending order: {DESC[0]} {DESC[1]} {DESC[2]}")
    elif MENU == 3:
        ASC = sorted(ARRAY[:3])
        print(f"Ascending order: {ASC[0]} {ASC[1]} {ASC[2]}")
