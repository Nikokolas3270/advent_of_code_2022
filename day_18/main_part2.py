#!/usr/bin/env python3

from collections import deque

xMin = xMax = yMin = yMax = zMin = zMax = None
lavaCubes = set()

with open("input") as f:
    for l in f.readlines():
        cube = tuple(map(int, l.strip().split(',')))
        x, y, z = cube

        if xMin is None:
            xMin = xMax = x
            yMin = yMax = y
            zMin = zMax = z
        else:
            xMin = min(xMin, x)
            xMax = max(xMax, x)
            yMin = min(yMin, y)
            yMax = max(yMax, y)
            zMin = min(zMin, z)
            zMax = max(zMax, z)

        lavaCubes.add(cube)

xMin -= 1
xMax += 1
yMin -= 1
yMax += 1
zMin -= 1
zMax += 1

airCubes = set()

queue = deque([(xMin, yMin, zMin)])
while queue:
    cube = queue.popleft()
    x, y, z = cube
    if xMin <= x and x <= xMax and yMin <= y and y <= yMax and zMin <= z and z <= zMax and cube not in lavaCubes and cube not in airCubes:
        airCubes.add(cube)

        queue.append((x-1, y, z))
        queue.append((x+1, y, z))
        queue.append((x, y-1, z))
        queue.append((x, y+1, z))
        queue.append((x, y, z-1))
        queue.append((x, y, z+1))

surface = 0

for x, y, z in lavaCubes:
    if (x-1, y, z) in airCubes:
        surface += 1
    if (x+1, y, z) in airCubes:
        surface += 1
    if (x, y-1, z) in airCubes:
        surface += 1
    if (x, y+1, z) in airCubes:
        surface += 1
    if (x, y, z-1) in airCubes:
        surface += 1
    if (x, y, z+1) in airCubes:
        surface += 1

print(surface)