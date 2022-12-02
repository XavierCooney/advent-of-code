from framework import *

print(eval(read_input().replace(',', ' ').replace('\n', '')))

t = 0
seen = set([t])
for a in itertools.cycle([*map(int, read_input().split('\n'))]):
    t += a
    if t in seen:
        print(t)
        break
    seen.add(t)