"""SMART TRASH COLLECTOR"""

N = int(input())

for _ in range(N):
    PLASTIC, CAN, GLASS = map(float, input().split())
    TOTAL = PLASTIC + CAN + GLASS

    OUTPUT_PARTS = [f"{TOTAL:.1f}"]

    if TOTAL > 50.0:
        OUTPUT_PARTS.append("Overloaded")
    if PLASTIC > 20.0:
        OUTPUT_PARTS.append("Check Type Plastic")
    if CAN > 20.0:
        OUTPUT_PARTS.append("Check Type Can")
    if GLASS > 20.0:
        OUTPUT_PARTS.append("Check Type Glass")

    print(", ".join(OUTPUT_PARTS))
