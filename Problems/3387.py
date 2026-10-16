"""TUPLE'S SAD LIFE"""

TUPLE_DATA = tuple(input().split())
TARGET = input().strip()

INDEX = TUPLE_DATA.index(TARGET)
COUNT = TUPLE_DATA.count(TARGET)

for _ in range(COUNT):
    print(*([INDEX] * COUNT))
