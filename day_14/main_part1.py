#!/usr/bin/env python3

import sys

def sign(v):
    return 1 if v >= 0 else -1

xMin = 500
xMax = 500
yMax = 0
matrix = [['+']]

with open("input") as f:
    for l in f.readlines():
        path = [tuple(map(int, p.strip().split(','))) for p in l.strip().split("->")]

        previousX, previousY = None, None

        for x, y in path:
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

sandCount = 0

def quit():
    print('\n'.join([''.join(row) for row in matrix]))
    print(sandCount)
    sys.exit()

while True:
    y, j = 0, 500 - xMin

    while True:
        y += 1
        if y > yMax:
            quit()
        if matrix[y][j] != ' ':
            if j == 0:
                quit()
            elif matrix[y][j - 1] == ' ':
                j -= 1
            elif xMin + j == xMax:
                quit()
            elif matrix[y][j + 1] == ' ':
                j += 1
            else:
                y -= 1
                if y == 0:
                    print("Filled to the top (bug!)")
                    quit()
                matrix[y][j] = 'O'
                break

    sandCount += 1