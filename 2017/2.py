from framework import *

t = 0
s = read_input()
for line in s.split('\n'):
    data = [*map(int, line.split('\t'))]
    t += max(data) - min(data)
print(t)

t = 0
for line in s.split('\n'):
    data = [*map(int, line.split('\t'))]
    for a in data:
        for b in data:
            if a != b and a % b == 0:
                t += a // b
print(t)