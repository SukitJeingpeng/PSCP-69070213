"""MAIN RONGRAM WITH NO FLOOR 13"""

KEY = input()
ONE = ""
TWO = ""
THREE = ""

if int(KEY[0]) > 5:
    ONE = 9
elif int(KEY[1]) > 5:
    ONE = 10
elif int(KEY[2]) > 5:
    ONE = 11
elif int(KEY[3]) > 5:
    ONE = 12
elif int(KEY[4]) > 5:
    ONE = 14
else:
    ONE = 13

if KEY == KEY[::-1]:
    if int(KEY[0]) + int(KEY[4]) > 5:
        TWO = 1
    elif int(KEY[1]) * int(KEY[3]) > 5:
        TWO = 2
    else:
        TWO = 0

elif KEY != KEY[::-1]:
    if int(KEY[4]) and int(KEY[0]) // int(KEY[4]) > 5:
        TWO = 1
    elif int(KEY[1]) - int(KEY[4]) > 5:
        TWO = 2
    else:
        TWO = 0

if int(KEY[0]) + int(KEY[1]) + int(KEY[2]) + int(KEY[3]) + int(KEY[4]) > 25:
    THREE = 1
elif int(KEY[0]) * int(KEY[1]) * int(KEY[2]) * int(KEY[3]) * int(KEY[4]) > 55:
    THREE = 2
else:
    THREE = 0

print(f"{ONE}{TWO}{THREE}")
