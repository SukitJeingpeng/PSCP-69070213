"""ARCADE OF TIME : STORE CHECK"""

first = input().split()
num = int(first[0])
stores = []

for _ in range(num):
    store = input().split()
    start = int(store[0])
    stop = int(store[1])
    stores.append([start, stop])

queries = input().split()

results = []
for q in queries:
    time_val = int(q)
    count = 0
    for s in stores:
        if s[0] <= time_val < s[1]:
            count += 1
    results.append(str(count))

print(*results)
