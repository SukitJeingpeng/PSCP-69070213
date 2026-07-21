"""MAIN SURPRISIN VOTE"""

TOTALSCORE = float(input())
HIGHESTSCORE = float(input())

LOWESTSCORE = ((TOTALSCORE - HIGHESTSCORE) / 2) - 1

if LOWESTSCORE < 0:
    LOWESTSCORE = 0

if HIGHESTSCORE - LOWESTSCORE <= 2:
    print("Not surprising")
else:
    print("Surprising")
