"""BIGFRAME"""

WORDLIST = []
for _ in range(5):
    WORDLIST.append(input())

MAX = 0
for i in WORDLIST:
    if len(i) > MAX:
        MAX = len(i)

TOPBOTTOM = "*" * (MAX + 4)
print(TOPBOTTOM)
for j in WORDLIST:
    SPACE = MAX - len(j)
    FINAL = j + (" " * SPACE)
    print(f"* {FINAL} *")
print(TOPBOTTOM)
