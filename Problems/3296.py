"""MAIN"""
RED1, GREEN1, BLUE1 = map(int, input().split())
RED2, GREEN2, BLUE2 = map(int, input().split())

AVGRED = (RED1 + RED2) // 2
AVGGREEN = (GREEN1 + GREEN2) // 2
AVGBLUE = (BLUE1 + BLUE2) // 2

print(f"{AVGRED} {AVGGREEN} {AVGBLUE}")
