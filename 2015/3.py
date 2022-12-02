from framework import *

s = read_input()

seen = set()
x = 0
y = 0

for c in s:
    seen.add((x, y))
    if c == '^': y -= 1
    if c == 'v': y += 1
    if c == '>': x += 1
    if c == '<': x -= 1
    seen.add((x, y))
print(len(seen))



##################################################

from framework import *

s = read_input()

seen = set()
x = 0
y = 0

for c in s[::2]:
    seen.add((x, y))
    if c == '^': y -= 1
    if c == 'v': y += 1
    if c == '>': x += 1
    if c == '<': x -= 1
    seen.add((x, y))
x = 0
y = 0

for c in s[1::2]:
    seen.add((x, y))
    if c == '^': y -= 1
    if c == 'v': y += 1
    if c == '>': x += 1
    if c == '<': x -= 1
    seen.add((x, y))
print(len(seen))