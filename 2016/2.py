from framework import *

s = read_input()

v = """1 2 3
4 5 6
7 8 9""".replace(' ', '').split('\n')

x, y = 0,0
p1 = ""
for line in s.split('\n'):
    for c in line:
        if c == 'U': y -= 1
        elif c == 'D': y += 1
        elif c == 'L': x -= 1
        elif c == 'R': x += 1
        x = min(max(x, -1), 1)
        y = min(max(y, -1), 1)
    # print(v[y + 1][x + 1], y, x)
    p1 += v[y + 1][x + 1]
print(p1)

v = """    1
  2 3 4
5 6 7 8 9
  A B C
    D""".split('\n')
v = dict(enumerate([dict(enumerate(line[::2])) for line in v]))

y = 2
x = 0

p2 = ""

for line in s.split('\n'):
    for c in line:
        oldx = x
        oldy = y
        if c == 'U': y -= 1
        elif c == 'D': y += 1
        elif c == 'L': x -= 1
        elif c == 'R': x += 1

        if y not in v or x not in v[y] or v[y][x] == ' ':
            x = oldx
            y = oldy
    # print(v[y + 1][x + 1], y, x)
    p2 += v[y][x]
print(p2)
