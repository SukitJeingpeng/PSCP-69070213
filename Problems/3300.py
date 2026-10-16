"""สมดุลลชีวิต"""
N = int(input())

WORK = []
for _ in range(N):
    WORK.append(int(input()))
HEAVY = 0
NORMAL = 0
for i in WORK:
    if i > 18:
        HEAVY += 1
    else:
        NORMAL += 1
if HEAVY > NORMAL + 1:
    DAYS = HEAVY + (HEAVY - 1)
else:
    DAYS = N
print(DAYS)
