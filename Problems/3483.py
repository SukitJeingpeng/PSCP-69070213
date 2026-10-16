"""มาเป็นทีม"""

N, M = map(int, input().split())

if not (1 <= N <= 10 and 1 <= M <= 20):
    print("Data Incorrect")
else:
    SCORES = []
    VALID = True
    for _ in range(N):
        ROW = list(map(int, input().split()))
        if len(ROW) != M:
            VALID = False
        for s in ROW:
            if s < 0 or s > 100:
                VALID = False
        SCORES.append(ROW)

    if not VALID:
        print("Data Incorrect")
    else:
        TOTAL_ALL = 0
        for i in range(N):
            TEAM_SUM = sum(SCORES[i])
            TEAM_AVG = TEAM_SUM / M
            TEAM_MAX = max(SCORES[i])
            TOTAL_ALL += TEAM_SUM
            print(f"Team {i + 1}: Average = {TEAM_AVG:.2f}, Max = {TEAM_MAX}")
        print(f"Total Score of All Teams = {TOTAL_ALL}")
