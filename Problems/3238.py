"""MAIN ASCII FOR ELONMUHHH"""
X,K = input().split()
X = int(X)
CAL = ord(K)
Middle = int((X + 1) / 2)

if K == "#":
    for i in range(1,X+1):
        for j in range(1,X+1):
            if j==i or (j + i) - 1 == X:
                print("#", end="")
            else:
                print("-", end="")
        print("")
else:
    for i in range(1,X+1):
        for j in range(1,X+1):
            if j==i or (j + i) - 1 == X:
                if X % 2 == 1:
                    if i < Middle:
                        TEXTASNUM = CAL + (Middle - i)
                        TEXT = chr(TEXTASNUM)
                        if TEXTASNUM >= 127:
                            print("-", end="")
                        else:
                            print(TEXT, end="")
                    elif i == Middle:
                        print(K, end="")
                    elif i > Middle:
                        TEXTASNUM = CAL + (i - Middle)
                        TEXT = chr(TEXTASNUM)
                        if TEXTASNUM >= 127:
                            print("-", end="")
                        else:
                            print(TEXT, end="")
                else:
                    if i < Middle:
                        TEXTASNUM = CAL + (Middle - i)
                        TEXT = chr(TEXTASNUM)
                        if TEXTASNUM >= 127:
                            print("-", end="")
                        else:
                            print(TEXT, end="")
                    elif i == Middle:
                        print(K, end="")
                    elif i > Middle:
                        TEXTASNUM = CAL + (i - Middle) - 1
                        TEXT = chr(TEXTASNUM)
                        if TEXTASNUM >= 127:
                            print("-", end="")
                        else:
                            print(TEXT, end="")
            else:
                print("-", end="")
        print("")
