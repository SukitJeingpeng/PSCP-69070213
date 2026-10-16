"""CUTECAT CUTEFOX"""

N = int(input())

CATS = {}
FOXES = {}
ALL_NAMES = set()

for _ in range(N):
    RAW_LINE = input().strip()

    CLEAN_LINE = RAW_LINE.replace("{", "").replace("}", "")
    PARTS = CLEAN_LINE.split(":")

    PART_1 = PARTS[0].strip().strip('"').strip("'")
    PART_2 = PARTS[1].strip().strip('"').strip("'")

    PREFIX = PART_1[:3]
    SUFFIX = PART_1[3:]

    if PREFIX in ("Cat", "Fox") and SUFFIX.isdigit():
        CODE = PART_1
        NAME = PART_2
    else:
        NAME = PART_1
        CODE = PART_2

    ALL_NAMES.add(NAME)

    NUMBER = int(CODE[3:])
    if CODE.startswith("Cat"):
        CATS[NUMBER] = (NAME, CODE)
    elif CODE.startswith("Fox"):
        FOXES[NUMBER] = (NAME, CODE)

HAS_CAT_1 = 1 in CATS
HAS_GARFIELD = "Garfield" in ALL_NAMES
if not HAS_CAT_1 and not HAS_GARFIELD:
    CATS[1] = ("Garfield", "Cat01")

HAS_FOX_1 = 1 in FOXES
HAS_FUBUKI = "Fubuki" in ALL_NAMES
if not HAS_FOX_1 and not HAS_FUBUKI:
    FOXES[1] = ("Fubuki", "Fox01")

print(f"Cat : {len(CATS)}")
print(f"Fox : {len(FOXES)}")

SORTED_CAT_NUMBERS = sorted(CATS.keys())
for number in SORTED_CAT_NUMBERS:
    name, code = CATS[number]
    print(f"{name} : {code}")

SORTED_FOX_NUMBERS = sorted(FOXES.keys())
for number in SORTED_FOX_NUMBERS:
    name, code = FOXES[number]
    print(f"{name} : {code}")
