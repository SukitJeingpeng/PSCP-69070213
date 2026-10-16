"""ELONMUHHH"""

X, K = map(str, input().split())
NUM = int(X)
CHAR = ord(K)

if K == "#":
    for i in range(NUM):
        RESULT = ""
        for j in range(NUM):
            if i == j or j + i == (NUM - 1):
                RESULT += K
            else:
                RESULT += "-"
        print(RESULT)
else:
    if not NUM % 2:
        NUM1 = NUM // 2
        for i in range(NUM):
            RESULT = ""
            for j in range(NUM):
                if i == j or j+i == (NUM - 1):
                    if i <= ((NUM + 1) / 2) - 1 and CHAR + (NUM1 - i) <= 126:
                        RESULT += chr((CHAR+NUM1) - i)
                    elif i > ((NUM + 1) / 2) - 1 and (CHAR + i) - (NUM1 + 1) <= 126:
                        RESULT += chr((CHAR-NUM1) + i)
                    else:
                        RESULT += "-"
                else:
                    RESULT += "-"
            print(RESULT)
    else:
        NUM1 = (NUM - 1) // 2
        for i in range(NUM):
            RESULT = ""
            for j in range(NUM):
                if i == j or j+i == (NUM - 1):
                    if i <= ((NUM + 1) / 2) - 1 and CHAR + (NUM1 - i) <= 126:
                        RESULT += chr(CHAR+(NUM1-i))
                    elif i > ((NUM + 1) / 2)-1 and (CHAR + i) - NUM1 <= 126:
                        RESULT += chr((CHAR + i) - NUM1)
                    else:
                        RESULT += "-"
                else:
                    RESULT += "-"
            print(RESULT)
