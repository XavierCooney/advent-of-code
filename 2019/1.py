from framework import *

s = read_input()

t1 = 0
t2 = 0
for line in s.split('\n'):
    x = int(line)
    t1 += int(x) // 3 - 2
    while x > 0:
        x = int(x) // 3 - 2
        if x > 0:
            t2 += x
print(t1)
print(t2)