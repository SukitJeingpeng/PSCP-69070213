"""CAESARV2"""

TEXT = input()

COMMON = {
    "what",
    "when",
    "why",
    "which",
    "this",
    "there",
    "where",
    "the",
    "is",
    "am",
    "are",
    "you",
    "we",
    "they",
    "he",
    "she",
    "it",
}

BEST_TEXT = ""
BEST_SCORE = -1

for i in range(26):
    DECRYPTED_CHARS = []
    for j in TEXT:
        if "a" <= j <= "z":
            DECRYPTED_CHARS.append(chr((ord(j) - ord("a") - i) % 26 + ord("a")))
        elif "A" <= j <= "Z":
            DECRYPTED_CHARS.append(chr((ord(j) - ord("A") - i) % 26 + ord("A")))
        else:
            DECRYPTED_CHARS.append(j)

    DECRYPTED_TEXT = "".join(DECRYPTED_CHARS)

    WORDS = []
    CURRENT_WORD = []
    for j in DECRYPTED_TEXT:
        if j.isalpha():
            CURRENT_WORD.append(j.lower())
        else:
            if CURRENT_WORD:
                WORDS.append("".join(CURRENT_WORD))
                CURRENT_WORD = []
    if CURRENT_WORD:
        WORDS.append("".join(CURRENT_WORD))

    SCORE = 0
    for word in WORDS:
        if word in COMMON:
            SCORE += 1

    if SCORE > BEST_SCORE:
        BEST_SCORE = SCORE
        BEST_TEXT = DECRYPTED_TEXT

print(BEST_TEXT)
