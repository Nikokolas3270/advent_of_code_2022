#!/usr/bin/env python3

with open("input") as f:
    res = 0

    for l in f.readlines():
        l = l.strip()
        m = len(l) >> 1
        p1 = l[:m]
        p2 = l[m:]

        for c in p1:
            if c in p2:
                if 'a' <= c and c <= 'z':
                    res += ord(c) - ord('a') + 1
                else:
                    res += ord(c) - ord('A') + 27
                #print(l, c, res)
                break

    print(res)