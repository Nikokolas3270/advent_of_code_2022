#!/usr/bin/env python3

from collections import deque

elvesPos = set()

with open("input") as f:
    for y, l in enumerate(f.readlines()):
        for x, c in enumerate(l.strip()):
            if c == '#':
                elvesPos.add((x, y))

def bounds():
    xMin = xMax = yMin = yMax = None

    for x, y in elvesPos:
        if xMin is None:
            xMin = xMax = x
            yMin = yMax = y
        else:
            xMin = min(xMin, x)
            xMax = max(xMax, x)
            yMin = min(yMin, y)
            yMax = max(yMax, y)
    
    return  xMin, xMax, yMin, yMax

def printElves():
    xMin, xMax, yMin, yMax = bounds()

    for y in range(yMin, yMax+1):
        print(''.join(['#' if (x, y) in elvesPos else '.' for x in range(xMin, xMax+1)]))

    print()

round = 1
deltas = deque([(0, -1), (0, 1), (-1, 0), (1, 0)])

while True:
    newPosToOldPos = {}
    forbiddenPos = set()

    for x, y in elvesPos:
        allNewPos = []
        for dx, dy in deltas:
            newPos = (x + dx, y + dy)
            if newPos not in elvesPos:
                if dx == 0:
                    if (x - 1, y + dy) not in elvesPos and (x + 1, y + dy) not in elvesPos:
                        allNewPos.append(newPos)
                else: # dy == 0
                    if (x + dx, y - 1) not in elvesPos and (x + dx, y + 1) not in elvesPos:
                        allNewPos.append(newPos)

        if allNewPos and len(allNewPos) != 4:
            newPos = allNewPos[0]
            if newPos in newPosToOldPos:
                del newPosToOldPos[newPos]
                forbiddenPos.add(newPos)
            elif newPos not in forbiddenPos:
                newPosToOldPos[newPos] = (x, y)
    
    if not newPosToOldPos:
        break

    elvesPos.difference_update(newPosToOldPos.values())
    elvesPos |= newPosToOldPos.keys()

    deltas.append(deltas.popleft())
    round += 1

print(round)