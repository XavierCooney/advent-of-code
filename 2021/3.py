from framework import *


s = read_input()
s = splitlines(s)

gamma = ''
eps = ''

for i in range(12):
    total = sum(
        line[i] == '1'
        for line in s
    )
    x = int(total > len(s) / 2)
    gamma += str(x)
    eps += str(1-x)
print(int(gamma, 2) * int(eps, 2))

oxy = [*s]
for i in range(12):
    if len(oxy) == 1: break

    most_common = str(int(sum(
        line[i] == '1'
        for line in oxy
    ) >= len(oxy) / 2))
    oxy = [
        o
        for o in oxy
    if o[i] == most_common
    ]


co2 = [*s]
for i in range(12):
    if len(co2) == 1: break

    least_common = str(1 - int(sum(
        line[i] == '1'
        for line in co2
    ) >= len(co2) / 2))
    co2 = [
        o
        for o in co2
        if o[i] == least_common
    ]

print(int(oxy[0], 2) * int(co2[0], 2))