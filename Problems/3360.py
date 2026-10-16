"""หั่นขนมปัง"""

W, H, M, N = map(int, input().split())
X_POINTS = [0] + list(map(int, input().split())) + [W]
Y_POINTS = [0] + list(map(int, input().split())) + [H]

DX = []
for i in range(M + 1):
    DX.append(X_POINTS[i + 1] - X_POINTS[i])

DY = []
for i in range(N + 1):
    DY.append(Y_POINTS[i + 1] - Y_POINTS[i])

DX.sort(reverse=True)
DY.sort(reverse=True)

TOP1 = DX[0] * DY[0]
TOP2 = max(DX[1] * DY[0], DX[0] * DY[1])

print(f"{TOP1} {TOP2}")
