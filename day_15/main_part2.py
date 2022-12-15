#!/usr/bin/env python3

import re
import sys

regexp = re.compile("Sensor at x=(?P<Sx>-?\d+), y=(?P<Sy>-?\d+): closest beacon is at x=(?P<Bx>-?\d+), y=(?P<By>-?\d+)")

sensors = []

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        m = regexp.fullmatch(l)
        if not m:
            sys.exit("Unmatched line: " + l)

        sX, sY = int(m.group("Sx")), int(m.group("Sy"))
        bX, bY = int(m.group("Bx")), int(m.group("By"))
        d = abs(sX - bX) + abs(sY - bY)

        sensors.append((sX, sY, d))

for y in range(0, 4000001):
    x = 0
    while x <= 4000000:
        for sX, sY, d in sensors:
            if abs(x - sX) + abs(y - sY) <= d:
                x = sX + d - abs(y - sY) + 1
                break
        else:
            print(x*4000000+y)
            sys.exit()

print("Not found")