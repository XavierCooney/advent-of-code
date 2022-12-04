from framework import *

s = read_input_lines()
p1 = 0
p2 = 0
for line in s:
    a, b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    x = set(range(a1, a2 + 1))
    y = set(range(b1, b2 + 1))
    if x <= y or y <= x:
        p1 += 1
    if x & y:
        p2 += 1
print(p1)
print(p2)