#!/usr/bin/env python3

with open("input") as f:
    sums = []
    s = 0

    for l in f.readlines():
        l = l.strip()
        if l:
            s += int(l)
        else:
            sums.append(s)
            s = 0

    sums.append(s)
    print(sorted(sums)[-3:])

    print(sum(list(sorted(sums))[-3:]))
