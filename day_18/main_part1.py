#!/usr/bin/env python3

cubes = set()

with open("input") as f:
    for l in f.readlines():
        cubes.add(tuple(map(int, l.strip().split(','))))

surface = 0

for x, y, z in cubes:
    surface += 6
    if (x-1, y, z) in cubes:
        surface -= 1
    if (x+1, y, z) in cubes:
        surface -= 1
    if (x, y-1, z) in cubes:
        surface -= 1
    if (x, y+1, z) in cubes:
        surface -= 1
    if (x, y, z-1) in cubes:
        surface -= 1
    if (x, y, z+1) in cubes:
        surface -= 1

print(surface)