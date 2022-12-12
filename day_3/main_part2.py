#!/usr/bin/env python3

with open("input") as f:
    res = 0
    g = []

    for l in f.readlines():
        l = l.strip()
        g.append(l)

        if len(g) == 3:
            for c in l:
                if c in g[0] and c in g[1]:
                    if 'a' <= c and c <= 'z':
                        res += ord(c) - ord('a') + 1
                    else:
                        res += ord(c) - ord('A') + 27
                    #print(g, c, res)
                    break
            g = []

    print(res)