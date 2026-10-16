"""NAME OF CARD"""

RANKS = {
    "A": "Ace",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
}

SUITS = {
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs",
}

CARD = input().strip()
RANK = CARD[:-1].upper()
SUIT = CARD[-1].upper()

RANK_NAME = RANKS.get(RANK, RANK)
SUIT_NAME = SUITS[SUIT]

print(f"{RANK_NAME} of {SUIT_NAME}")
