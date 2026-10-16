"""Muddled Menu"""

MENU = []

while True:
    LINE = input()
    if LINE == "DONE":
        break
    if LINE == "CLOSED":
        MENU.clear()
        break
    if LINE == "SOMETHING'S WRONG":
        MENU.clear()
    elif LINE.startswith("Can't do: "):
        DISH = LINE[10:]
        while DISH in MENU:
            MENU.remove(DISH)
    else:
        DISH, POS = LINE.rsplit(" #", 1)
        if POS == "N":
            MENU.append(DISH)
        else:
            MENU.insert(int(POS) - 1, DISH)

print(f"Full Course: {MENU} Reversed: {MENU[::-1]}")
