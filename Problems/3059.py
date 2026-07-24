"""MAIN ผลการสอบ"""

FIRSTSCORE = int(input())
SECONDSCORE = int(input())
THIRDSCORE = int(input())

PERCENT1 = 10 / 2
PERCENT2 = 40 / 2
PERCENT3 = 50 / 2

if FIRSTSCORE < PERCENT1 or SECONDSCORE <  PERCENT2 or THIRDSCORE < PERCENT3:
    print("fail")
else:
    if FIRSTSCORE + SECONDSCORE + THIRDSCORE >= 50:
        print("pass")
    else:
        print("fail")
