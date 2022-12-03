from framework import *

s = read_input_lines()

def make_path(line):
    x = 0
    y = 0

    points = set()

    for cmd in line.split(','):
        d, *amt = [*cmd]
        amt = int(''.join(amt))

        points.add((x,y))
        for i in range(amt):
            if d == 'L': x -= 1
            if d == 'R': x += 1
            if d == 'U': y -= 1
            if d == 'D': y += 1
            points.add((x,y))
        points.add((x,y))
    return points

a1 = make_path(s[0])
b1 = make_path(s[1])
i = [abs(x) + abs(y) for x, y in (a1 & b1) - {(0, 0)}]

print(min(i))


from framework import *

s = read_input_lines()

def make_path_2(line):
    x = 0
    y = 0
    z = 1

    points = {}

    for cmd in line.split(','):
        d, *amt = [*cmd]
        amt = int(''.join(amt))

        for i in range(amt):
            if d == 'L': x -= 1
            if d == 'R': x += 1
            if d == 'U': y -= 1
            if d == 'D': y += 1
            if (x,y) not in points: points[(x, y)] = z
            z += 1

    return points

a2 = make_path_2(s[0])
b2 = make_path_2(s[1])

ii = [
    (b2[p] + a2[p], p) if p in b2 else (float('inf'), p) for p in a2.keys()
]

print(min(ii)[0])
