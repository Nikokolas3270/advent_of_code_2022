#!/usr/bin/env python3

map = []

with open("input") as f:
    for l in f.readlines():
        map.append([int(c) for c in l.strip()])

height = len(map)
width = len(map[0])

def isVisible(x, y):
    size = map[y][x]

    for xx in range(x):
        if map[y][xx] >= size:
            break
    else:
        return True

    for xx in range(x+1,width):
        if map[y][xx] >= size:
            break
    else:
        return True

    for yy in range(y):
        if map[yy][x] >= size:
            break
    else:
        return True

    for yy in range(y+1,height):
        if map[yy][x] >= size:
            break
    else:
        return True
    
    return False

visibleCount = 0

for x in range(width):
    for y in range(height):
        if isVisible(x, y):
            visibleCount += 1

print(visibleCount)