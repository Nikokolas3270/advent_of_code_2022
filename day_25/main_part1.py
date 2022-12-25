#!/usr/bin/env python3

score = 0

with open("input") as f:
    for l in f.readlines():
        n = 0
        for c in l.strip():
            if c == '=':
                d = -2
            elif c == '-':
                d = -1
            else:
                d = int(c)
            n = n*5 +d
        score += n

print("Dec: %s" % score)

base = 1
while score / base > 2.5:
    base *= 5

digits = []
while base:
    d = round(abs(score) / base)
    if d == 0 or score >= 0:
        digits.append(str(d))
    else:
        d = -d
        if d == -1:
            digits.append('-')
        else:
            digits.append('=')
    score += -d * base
    base = base // 5

print("".join(digits))