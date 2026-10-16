"""CUTECAT CUTEFOX"""

N = int(input())
CATS = {}
FOXES = {}
ALL_NAMES = set()

for _ in range(N):
    LINE = input().strip().lstrip("{").rstrip("}")
    PART_1, PART_2 = LINE.split(":", 1)
    PART_1 = PART_1.strip().strip("'\"")
    PART_2 = PART_2.strip().strip("'\"")

    IS_P1_CODE = (PART_1.startswith("Cat") or PART_1.startswith("Fox")) and len(PART_1) > 3 and PART_1[3:].isdigit()
    if IS_P1_CODE:
        CODE, NAME = PART_1, PART_2
    else:
        NAME, CODE = PART_1, PART_2

    ALL_NAMES.add(NAME)
    NUM = int(CODE[3:])
    if CODE.startswith("Cat"):
        CATS[NUM] = (NAME, CODE)
    else:
        FOXES[NUM] = (NAME, CODE)

if 1 not in CATS and "Garfield" not in ALL_NAMES:
    CATS[1] = ("Garfield", "Cat01")

if 1 not in FOXES and "Fubuki" not in ALL_NAMES:
    FOXES[1] = ("Fubuki", "Fox01")

print(f"Cat : {len(CATS)}")
print(f"Fox : {len(FOXES)}")

for _, (name, code) in sorted(CATS.items()):
    print(f"{name} : {code}")

for _, (name, code) in sorted(FOXES.items()):
    print(f"{name} : {code}")
