"""BRIDGE"""

A = int(input())
B = int(input())
GOAL = int(input())

USEB = GOAL // 5
if USEB > B:
    USEB = B

REMAIN = GOAL - (USEB * 5)
USEA = REMAIN

if USEA <= A:
    print(USEA)
else:
    print("-1")
