from framework import *

s = [*read_input()]

t = 0
for a, b in zip(s, s[1:] + s[:-1]):
    if a == b: t += int(a)
print(t)

t = 0
N = len(s) // 2
for a, b in zip(s, s[N:] + s[:N]):
    if a == b: t += int(a)
print(t)
