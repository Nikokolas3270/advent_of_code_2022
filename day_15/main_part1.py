#!/usr/bin/env python3

import re
import sys

regexp = re.compile("Sensor at x=(?P<Sx>-?\d+), y=(?P<Sy>-?\d+): closest beacon is at x=(?P<Bx>-?\d+), y=(?P<By>-?\d+)")

sensors = []
beacons = []
xMin = xMax = None

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        m = regexp.fullmatch(l)
        if not m:
            sys.exit("Unmatched line: " + l)

        sX, sY = int(m.group("Sx")), int(m.group("Sy"))
        bX, bY = int(m.group("Bx")), int(m.group("By"))
        d = abs(sX - bX) + abs(sY - bY)

        if xMin is None or xMin > sX - d:
            xMin = sX - d
        if xMax is None or xMax < sX + d:
            xMax = sX + d
        
        sensors.append((sX, sY, d))
        beacons.append((bX, bY))

y = 2000000

count = 0

for x in range(xMin, xMax + 1):
    for sX, sY, d in sensors:
        if abs(x - sX) + abs(y - sY) <= d and (x, y) not in beacons:
            count += 1
            break

print(count)