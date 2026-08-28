"""SCHOOL COOPERATIVE"""

MEMBER = input().strip()
N = int(input())
BEFORE = 0.0
for _ in range(N):
    BEFORE += float(input())

TOTALSATANG = int((BEFORE * 100) + 0.5)

if MEMBER == "Y":
    FINAL = (TOTALSATANG * 95 + 50) // 100
elif MEMBER == "N" and TOTALSATANG >= 50000:
    FINAL = (TOTALSATANG * 97 + 50) // 100
else:
    FINAL = TOTALSATANG

ROUND = FINAL / 100
print(f"{ROUND:.2f}")
