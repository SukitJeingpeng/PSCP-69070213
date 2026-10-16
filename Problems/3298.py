"""RABBIT LOVE BUU"""
WORD = input()
RESULT = 0
for i, char in enumerate(WORD):
    if char.lower() == 'b':
        COUNTER = 0
        POINTER = i + 1
        while POINTER < len(WORD) and WORD[POINTER].lower() == 'u':
            COUNTER += 1
            POINTER += 1
        RESULT = max(RESULT, COUNTER)
if RESULT >= 2:
    print("Yes", RESULT)
elif 'b' in WORD.lower():
    i = WORD.lower().index('b')
    print(WORD[:i + 1] + 'U' * (len(WORD) - i - 1))
else:
    print(('BUU' * len(WORD))[:len(WORD)])
