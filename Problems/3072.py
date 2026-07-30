"""VOWEL"""

TEXT = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0

for j in TEXT:
    if j == "a":
        a += 1
    elif j == "e":
        e += 1
    elif j == "i":
        i += 1
    elif j == "o":
        o += 1
    elif j == "u":
        u += 1

if a:
    print(f"a : {a}")
if e:
    print(f"e : {e}")
if i:
    print(f"i : {i}")
if o:
    print(f"o : {o}")
if u:
    print(f"u : {u}")
