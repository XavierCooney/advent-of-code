from framework import *

s = read_input_lines()

t = 0
for line in s:
    a, b, c = line.replace(':', '').split(' ')
    x, y = map(int, a.split('-'))
    if x <= c.count(b) <= y:
        t += 1
print(t)

t = 0
for line in s:
    a, b, c = line.replace(':', '').split(' ')
    x, y = map(int, a.split('-'))
    if (c[x-1]+c[y-1]).count(b) == 1:
        t += 1
print(t)