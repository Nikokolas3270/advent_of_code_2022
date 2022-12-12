#!/usr/bin/env python3

with open("input") as f:
    res = 0

    for l in f.readlines():
        rs = [list(map(int, r.split('-'))) for r in l.strip().split(',')]

        if rs[0][0] <= rs[1][0] and rs[1][1] <= rs[0][1]:
            res += 1
        elif rs[1][0] <= rs[0][0] and rs[0][1] <= rs[1][1]:
            res += 1

    print(res)