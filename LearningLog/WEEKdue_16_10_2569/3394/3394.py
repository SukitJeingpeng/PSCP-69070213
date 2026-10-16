"""ส่งต่อ"""

N, S = map(int, input().split())
FORWARD = [0] * (N + 1)

for i in range(1, N + 1):
    FORWARD[i] = int(input())

VISITED = set()
CURR = S

while CURR and CURR not in VISITED:
    VISITED.add(CURR)
    CURR = FORWARD[CURR]

print(len(VISITED))
