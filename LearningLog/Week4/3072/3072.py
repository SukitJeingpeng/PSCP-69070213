"""VOWEL"""

TEXT = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0

for j in range(len(TEXT)):
    if TEXT[j] == "a":
        a += 1
    elif TEXT[j] == "e":
        e += 1
    elif TEXT[j] == "i":
        i += 1
    elif TEXT[j] == "o":
        o += 1
    elif TEXT[j] == "u":
        u += 1

if a != 0:
      print(f"a : {a}")
if e != 0:
      print(f"e : {e}")
if i != 0:
      print(f"i : {i}")
if o != 0:
      print(f"o : {o}")
if u != 0:
      print(f"u : {u}")
