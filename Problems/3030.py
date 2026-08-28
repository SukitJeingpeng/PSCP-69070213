"""MAIN"""
import math as m

WID = int(input())
SIT = int(input())
UPDOWN = int(input())
RUN = int(input())
CANWID = int(input())
CANSIT = int(input())
CANRUN = int(input())
CANUPDOWN = int(input())

a = WID/CANWID
b = SIT/CANSIT
c = UPDOWN/CANUPDOWN
d = RUN/CANRUN

RESULT = m.ceil(max(a,b,c,d))
print(f"{RESULT:.0f}")
