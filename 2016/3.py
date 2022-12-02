from framework import *

s = read_input_lines()

t = 0
for line in s:
    data = [*map(int, filter(None, line.split()))]
    t += max(data) < sum(data) - max(data)
print(t)

t = 0
for a, b, c in zip(s[::3], s[1::3], s[2::3]):
    datas = [[*map(int, filter(None, line.split()))] for line in (a, b, c)]
    for i in range(3):
        data = datas[0][i], datas[1][i], datas[2][i]
        t += max(data) < sum(data) - max(data)
print(t)