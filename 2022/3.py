from framework import *

s = read_input_lines()

in_both = set(string.ascii_letters)

t = 0
for line in s:
    a, b = line[:len(line)//2], line[len(line)//2:]
    assert len(a) == len(b)

    x = set(a) & set(b)
    assert len(x) == 1
    x = x.pop()
    if x in string.ascii_lowercase:
        t += ord(x) - ord('a') + 1
    if x in string.ascii_uppercase:
        t += ord(x) - ord('A') + 27
print(t)
# Golfed!
# print(sum((c:=min({*l[:(N:=len(l)>>1)]}&{*l[N:]}))%32-c//32*26+78for l in open('2022/3.in','rb')))

##############################################################

s = read_input_lines()

in_both = set(string.ascii_letters)

t = 0
for p, q, r in zip(s[::3], s[1::3], s[2::3]):

    x = set(p) & set(q) & set(r)
    assert len(x) == 1
    x = x.pop()
    if x in string.ascii_lowercase:
        t += ord(x) - ord('a') + 1
    if x in string.ascii_uppercase:
        t += ord(x) - ord('A') + 27
print(t)