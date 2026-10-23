"""CLASSIFY"""

DATA = {}

while True:
    STUDENT_ID = input().strip()
    if STUDENT_ID == "END":
        break

    YEAR = STUDENT_ID[:2]
    FACULTY = int(STUDENT_ID[2:4])

    if YEAR not in DATA:
        DATA[YEAR] = {}

    if FACULTY not in DATA[YEAR]:
        DATA[YEAR][FACULTY] = 1
    else:
        DATA[YEAR][FACULTY] += 1

SORTED_YEARS = sorted(DATA.keys())

for year in SORTED_YEARS:
    FACULTIES = DATA[year]
    SORTED_FACULTIES = sorted(FACULTIES.keys())

    FIRST = True
    for faculty in SORTED_FACULTIES:
        count = FACULTIES[faculty]
        if FIRST:
            print(f"{year} {faculty} {count}")
            FIRST = False
        else:
            print(f"-- {faculty} {count}")
