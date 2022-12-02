from framework import *

s = read_input_lines()

def f(n):
    return sum([
        any(l.count(c) == n for c in l)
        for l in s
    ])

print(f(2) * f(3))

p2 = None
for a in s:
    if p2: break
    for b in s:
        if a == b: continue
        for i in range(len(a)):
            if a[:i] + a[i+1:] == b[:i] + b[i+1:]:
                # print(a,b, a[:i] + a[i+1:])
                p2 = a[:i] + a[i+1:]
print(p2)