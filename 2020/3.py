from framework import *

s = read_input_lines()

N = len(s[0])

x = 0
y = 0
t = 0
while y < len(s):
    x += 3
    y += 1
    if y < len(s): t += s[y][x % N] == '#'
print(t)


m = 1
for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    t = 0
    while y < len(s):
        x += dx
        y += dy
        if y < len(s): t += s[y][x % N] == '#'
    m *= t
print(m)
