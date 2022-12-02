from framework import *

s = read_input()

print(s.count('(') - s.count(')'))

i = 0
for j, c in enumerate(s):
    if c == '(': i += 1
    if c == ')': i -= 1
    if i == -1:
        print(j + 1)
        break