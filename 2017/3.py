from framework import *

s = int(read_input())

x = 0
y = 0

i = 1
n = 1
while True:
    for j in range(i): # right
        if n < s: x += 1
        n += 1

    for j in range(i): # up
        if n < s: y -= 1
        n += 1

    i += 1

    for j in range(i): # left
        if n < s: x -= 1
        n += 1

    for j in range(i): # down
        if n < s: y += 1
        n += 1

    if n >= s: break

    i += 1

print(abs(x) + abs(y))

final_x = x
final_y = y

s = int(read_input())

x = 0
y = 0

i = 1
n = 1

d = constant_value_default_dict(0)
d[(0, 0)] = 1

def place(dx, dy):
    global n, x, y, s

    if n >= s: return

    total = 0
    x += dx
    y += dy
    n += 1

    total = 0
    for ddx, ddy in ADJACENT_8:
        total += d[(x + ddx, y + ddy)]
    if total > s:
        print(total)
        n = s + 1
    # print(x, y, total)
    d[(x, y)] = total

while True:
    for j in range(i): # right
        place(1, 0)

    for j in range(i): # up
        place(0, -1)

    i += 1

    for j in range(i): # left
        place(-1, 0)

    for j in range(i): # down
        place(0, 1)

    if n >= s: break

    i += 1

print(final_x, x, final_y, y, d[(x, y)])