"""PAI 44 BAI"""

CARD = input().upper()
NUMBER = ("2","3","4","5","6","7","8","9","10")
ONE = ""
TWO = ""

if len(CARD) == 2:
    if CARD[0] in NUMBER:
        ONE = CARD[0]
    if CARD[0] == "A":
        ONE = "ace"
    if CARD[0] == "J":
        ONE = "jack"
    if CARD[0] == "Q":
        ONE = "queen"
    if CARD[0] == "K":
        ONE = "king"
    if CARD[1] == "D":
        TWO = "diamonds"
    if CARD[1] == "H":
        TWO = "hearts"
    if CARD[1] == "S":
        TWO = "spades"
    if CARD[1] == "C":
        TWO = "clubs"

if len(CARD) == 3:
    ONE = "10"
    if CARD[2] == "D":
        TWO = "diamonds"
    if CARD[2] == "H":
        TWO = "hearts"
    if CARD[2] == "S":
        TWO = "spades"
    if CARD[2] == "C":
        TWO = "clubs"

print(f"{ONE} of {TWO}")
