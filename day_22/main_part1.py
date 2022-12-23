#!/usr/bin/env python3

import re

with open("input") as f:
    lines = f.readlines()
    matrix = [l[:-1] for l in lines[:-2]]
    orders = re.split("(R|L)", lines[-1])

width = max([len(row) for row in matrix])
height = len(matrix)

for y, row in enumerate(matrix):
    matrix[y] = row + (" " * (width - len(row)))

x, y = 0, 0
dx, dy = 1, 0
facing = 0

while matrix[0][x] != '.':
    x += 1

for order in orders:
    if order == "L":
        dx, dy = dy, -dx
    elif order == "R":
        dx, dy = -dy, dx
    else:
        count = int(order)
        while count:
            nextX, nextY = (x+dx) % width, (y+dy) % height
            while matrix[nextY][nextX] == ' ':
                nextX, nextY = (nextX+dx) % width, (nextY+dy) % height 
            if matrix[nextY][nextX] == '#':
                break
            x, y = nextX, nextY
            count -= 1

passwd = 4*(x+1) + 1000*(y+1)

if (dx, dy) == (0, 1):
    passwd += 1
elif (dx, dy) == (-1, 0):
    passwd += 2
elif (dx, dy) == (0, -1):
    passwd += 3

print(passwd)