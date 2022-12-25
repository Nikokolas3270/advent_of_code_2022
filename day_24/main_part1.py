#!/usr/bin/env python3

from collections import deque

initialMatrix = []

with open("input") as f:
    for l in f.readlines()[1:-1]:
        row = []
        for c in l.strip()[1:-1]:
            v = 0
            for k, d in enumerate(("^", "v", "<", ">")):
                if c == d:
                    v |= 1 << k
            row.append(v)
        initialMatrix.append(row)

timeToMatrix = {0: initialMatrix}

height = len(initialMatrix)
width = len(initialMatrix[0])

def getMatrixForTime(t):
    if t in timeToMatrix:
        return timeToMatrix[t]

    oldMatrix = timeToMatrix[t-1]
    matrix = [[0] * width for _ in range(height)]

    for y, row in enumerate(oldMatrix):
        for x, v in enumerate(row):
            if v & 1:
                matrix[(y-1) % height][x] |= 1
            if v & 2:
                matrix[(y+1) % height][x] |= 2
            if v & 4:
                matrix[y][(x-1) % width] |= 4
            if v & 8:
                matrix[y][(x+1) % width] |= 8

    timeToMatrix[t] = matrix

    print("Time: %s" % t)

    return matrix

visits = set()

queue = deque([(0, 0, -1)])

while queue:
    visit = queue.popleft()
    if visit in visits:
        continue

    visits.add(visit)
    t, x, y = visit

    if (x, y) == (width - 1, height):
        print(t)
        break

    matrix = getMatrixForTime(t)

    if (x, y) == (0, -1) or (0 <= x and x < width and 0 <= y and y < height and matrix[y][x] == 0):
        t += 1
        queue.append((t, x, y+1))
        queue.append((t, x+1, y))
        queue.append((t, x, y))
        queue.append((t, x-1, y))
        queue.append((t, x, y-1))