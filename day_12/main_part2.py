#!/usr/bin/env python3

from queue import Queue
import sys

exitPos = (-1, -1)

map = []

with open("input") as f:
    for y, l in enumerate(f.readlines()):
        l = l.strip()
        map.append([])
        for x, c in enumerate(l):
            if c == 'S':
                c = 'a'
            elif c == 'E':
                exitPos = (x, y)
                c = 'z'
            map[y].append(ord(c))

width = len(map[0])
height = len(map)
startElevation = ord('a')

queue =[(exitPos, 0)]
visitedPos = set()

while queue:
    pos, pathLength = queue.pop(0)

    if pos not in visitedPos:
        visitedPos.add(pos)
        x, y = pos
        elevation = map[y][x]

        if elevation == startElevation:
            print(pathLength)
            sys.exit(0)
        
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nextX, nextY = (x + dx, y + dy)
            if 0 <= nextX and nextX < width and 0 <= nextY and nextY < height:
                nextElevation = map[nextY][nextX]
                if elevation <= nextElevation + 1:
                    queue.append(((nextX, nextY), pathLength + 1))        

print(visitedPos)
print("Exit not reached!")