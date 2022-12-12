#!/usr/bin/env python3

with open("input") as f:
    score = 0

    for l in f.readlines():
        l = l.strip()
        buf = []

        for k, c in enumerate(l):
            if len(buf) == 14:
                buf = buf[1:]
            buf.append(c)

            if len(buf) == 14:
                for c in buf:
                    if buf.count(c) != 1:
                        break
                else:
                    print(k+1)
                    break
