from framework import *

s = read_input_lines()

t = 0
for line in s:
    a, b = line.split(' ')

    beats = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    t += ord(b) - ord('X') + 1
    o = chr(ord(b) - ord('X') + ord('A'))
    if a == o:
        t += 3
    if beats[o] == a:
        t += 6
print(t)

t = 0
for line in s:
    a, b = line.split(' ')

    beats = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    beaten = inverse_dictionary(beats)

    if b == 'X': # lose
        o = beats[a]
    if b == 'Y': # draw
        o = a
    if b == 'Z': # win
        o = beaten[a]

    t += ord(o) - ord('A') + 1
    if a == o:
        t += 3
    if beats[o] == a:
        t += 6
print(t)