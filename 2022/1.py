from framework import *

s = read_input().split('\n\n')

a = [*(sum(map(int, t.split('\n'))) for t in s)]
a.sort()
print(a)

print(sum(a[-3:]))
