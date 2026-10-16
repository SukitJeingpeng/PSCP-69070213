"""FOUR DIRECTIONS"""
ARROWS = {
    'U': [
        "  *   ",
        " ***  ",
        "* * * ",
        "  *   ",
        "  *   "
    ],
    'D': [
        "  *   ",
        "  *   ",
        "* * * ",
        " ***  ",
        "  *   "
    ],
    'L': [
        "  *   ",
        " *    ",
        "***** ",
        " *    ",
        "  *   " 
    ],
    'R': [
        "  *   ",
        "   *  ",
        "***** ",
        "   *  ",
        "  *   "
    ]
}

LETTERS = input()
LETTERS = [ARROWS[c] for c in LETTERS]
for i in range(5):
    print("".join(row[i] for row in LETTERS))
