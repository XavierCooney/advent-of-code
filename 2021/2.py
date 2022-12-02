from framework import *

s = read_input().strip().split('\n')

y = 0
x = 0
for line in s:
    d, a = line.split(' ')
    a = int(a)
    if d == 'down': y += a
    if d == 'up': y -= a
    if d == 'forward': x += a

print(x * y)


y = 0
x = 0

aim = 0

for line in s:
    d, a = line.split(' ')
    a = int(a)
    if d == 'down': aim += a
    if d == 'up': aim -= a
    if d == 'forward':
        x += a
        y += a * aim

print(x * y)