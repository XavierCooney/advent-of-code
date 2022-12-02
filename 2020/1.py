from framework import *

d = set([*map(int, read_input_lines())])

for x in d:
    if 2020 - x in d:
        print((2020 - x) * x)
        break

p2 = None

for x in d:
    for y in d:
        if 2020 - x - y in d:
            p2 = (2020 - x - y) * x * y
            break
print(p2)