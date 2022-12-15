#!/usr/bin/env python3

import sys

def sign(v):
    return 1 if v >= 0 else -1

xMin = 500
xMax = 500
yMax = 0
matrix = [['+']]

def resize(x, y):
    global xMin, xMax, yMax

    if x < xMin:
        widthIncrease = xMin - x
        for i in range(len(matrix)):
            matrix[i] = [' '] * widthIncrease + matrix[i]
        xMin = x
    if x > xMax:
        widthIncrease = x - xMax
        for row in matrix:
            row.extend([' '] * widthIncrease)
        xMax = x
    if y > yMax:
        width = len(matrix[0])
        for _ in range(y - yMax):
            matrix.append([' '] * width)
        yMax = y

with open("input") as f:
    for l in f.readlines():
        path = [tuple(map(int, p.strip().split(','))) for p in l.strip().split("->")]

        previousX, previousY = None, None

        for x, y in path:
            resize(x, y)

            if previousX is not None:
                if x == previousX:
                    j = x - xMin
                    for yy in range(previousY, y, sign(y - previousY)):
                        matrix[yy][j] = '#'
                else:
                    for j in range(previousX - xMin, x - xMin, sign(x - previousX)):
                        matrix[y][j] = '#'

            matrix[y][x - xMin] = '#'
            previousX, previousY = x, y

resize(500, yMax + 2)
matrix[yMax] = ['#'] * len(matrix[yMax])

def resizeWithFloor(x, y):
    resize(x, y)
    matrix[yMax][0] = '#'
    matrix[yMax][-1] = '#'

sandCount = 1

def quit():
    print('\n'.join([''.join(row) for row in matrix]))
    print(sandCount)
    sys.exit()

while True:
    x, y = 500, 0

    while True:
        if x <= xMin:
            resizeWithFloor(x-1, y)
        elif x >= xMax:
            resizeWithFloor(x+1, y)
                
        y += 1

        if y > yMax:
            print("Going under the floor (bug!)")
            quit()

        if matrix[y][x - xMin] != ' ':
            if matrix[y][x - xMin - 1] == ' ':
                x -= 1
            elif matrix[y][x - xMin + 1] == ' ':
                x += 1
            else:
                y -= 1
                if y == 0:
                    quit()
                matrix[y][x - xMin] = 'O'
                break

    sandCount += 1