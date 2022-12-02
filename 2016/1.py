from framework import *

dy = 1
dx = 0

a, b = 0, 0

for l in read_input().split(', '):
    c, *x = [*l]
    x = int(''.join(x))

    if c == 'L':
        dx, dy = -dy, dx
    elif c == 'R':
        dx, dy = dy, -dx

    a += int(x) * dx
    b += int(x) * dy

print(abs(a) + abs(b))

####################################################################

dy = 1
dx = 0

a, b = 0, 0

p2 = None

locs = [(0, 0)]

for l in read_input().split(', '):
    c, *x = [*l]
    x = int(''.join(x))

    if c == 'L':
        dx, dy = -dy, dx
    elif c == 'R':
        dx, dy = dy, -dx

    for i in range(int(x)):
        a += dx
        b += dy

        if (a, b) in locs and p2 is None:
            p2 = abs(a) + abs(b)

        locs.append((a, b))

print(p2)

