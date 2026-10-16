"""MAGIC COIN"""

N = int(input())

TOTAL_FIRE = 0
TOTAL_WATER = 0
TOTAL_EARTH = 0

for _ in range(N):
    F1, W1, E1, F2, W2, E2 = map(int, input().split())
    TOTAL_FIRE += max(F1, F2)
    TOTAL_WATER += max(W1, W2)
    TOTAL_EARTH += max(E1, E2)

TOTAL = TOTAL_FIRE + TOTAL_WATER + TOTAL_EARTH

print(f"Total: {TOTAL}")
print(f"Fire: {TOTAL_FIRE}")
print(f"Water: {TOTAL_WATER}")
print(f"Earth: {TOTAL_EARTH}")

if TOTAL_FIRE > TOTAL_WATER + TOTAL_EARTH:
    print("Bonus: YES")
else:
    print("Bonus: NO")
