from framework import *

s = read_input_lines()

d = constant_value_default_dict(0)

for line in s:
    num, _, coord, size = line.split(' ')
    x, y = map(int, coord.replace(':', '').split(','))
    w, h = map(int, size.split('x'))

    for i in range(x, x + w):
        for j in range(y, y + h):
            d[(i, j)] += 1

print(sum(1 for v in d.values() if v >= 2))

for line in s:
    num, _, coord, size = line.split(' ')
    x, y = map(int, coord.replace(':', '').split(','))
    w, h = map(int, size.split('x'))

    has_overlap = False
    for i in range(x, x + w):
        for j in range(y, y + h):
            if d[(i, j)] > 1:
                has_overlap = True

    if not has_overlap: print(num.replace('#', ''))
