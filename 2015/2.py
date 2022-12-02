from framework import *

s = read_input()

t = 0
for line in s.split('\n'):
    a, b, c = map(int, line.split('x'))
    t += 2 * (a*b + b*c + a*c) + min(a*b, b*c, a*c)
print(t)


t = 0
for line in s.split('\n'):
    a, b, c = map(int, line.split('x'))
    t += a*b*c + 2 * (a + b + c - max(a,b,c))
print(t)
