from framework import *

s = read_input_lines()

[*x] = map(int, s)

c = 0
for a, b in zip(x, x[1:]):
    if b > a: c += 1
print(c)

d = []
for a, b, c in zip(x, x[1:], x[2:]):
    d += [a + b + c]

c = 0
for a, b in zip(d, d[1:]):
    if b > a: c += 1
print(c)