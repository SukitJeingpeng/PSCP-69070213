"""FILTER"""

RAW_DICT = input().strip()
FILTER_SCORE = float(input())

CLEAN_DICT = RAW_DICT.lstrip("{").rstrip("}").strip()

STUDENTS = {}
if CLEAN_DICT:
    PAIRS = CLEAN_DICT.split(",")
    for pair in PAIRS:
        KEY, VALUE = pair.split(":")
        STUDENT_ID = KEY.strip().strip('"').strip("'")
        SCORE = float(VALUE.strip())
        STUDENTS[STUDENT_ID] = SCORE

QUALIFIED_STUDENTS = []
for student_id, score in sorted(STUDENTS.items()):
    if score >= FILTER_SCORE:
        QUALIFIED_STUDENTS.append((student_id, score))

if QUALIFIED_STUDENTS:
    for student_id, score in QUALIFIED_STUDENTS:
        print(f"{student_id}\t{score:.2f}")
else:
    print("Nope")
