#!/usr/bin/env python3

with open("input") as f:
    maxSum = -1
    sum = 0

    for l in f.readlines():
        l = l.strip()
        if l:
            sum += int(l)
        else:
            maxSum = max(sum, maxSum)
            sum = 0

    print(max(sum, maxSum))
