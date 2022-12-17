#!/usr/bin/env python3

pieces = [
    ["####"],

    [".#",
     "###",
     ".#"],

    ["..#",
     "..#",
     "###"],

    ["#",
     "#",
     "#",
     "#"],

    ["##",
     "##"]
]


with open("input") as f:
    for l in f.readlines():
        mvts = l.strip()
        break

pieceCount = 0
mvtIdx = 0

matrix = []

def findTopY():
    y = 0
    while y < len(matrix) and '#' not in matrix[y]:
        y += 1

    return y

while pieceCount < 2022:
    piece = pieces[pieceCount % len(pieces)]

    y = findTopY() - 3 - len(piece)

    if y < 0:
        matrix = [['.'] * 7 for _ in range(-y)] + matrix
        y = 0

    x = 2

    def canMove(dx, dy):
        for py in range(len(piece)):
            yy = y + py + dy
            for px in range(len(piece[py])):
                xx = x + px + dx
                if xx < 0 or xx >= 7 or yy >= len(matrix) or (piece[py][px] == '#' and matrix[yy][xx] == '#'):
                    return False

        return True

    def froze():
        for py in range(len(piece)):
            for px in range(len(piece[py])):
                if piece[py][px] == '#':
                    matrix[y+py][x+px] = '#'

    while True:
        mvt = mvts[mvtIdx % len(mvts)]
        mvtIdx += 1

        dx = -1 if mvt == '<' else 1
        if canMove(dx, 0):
            x += dx

        if not canMove(0, 1):
            break

        y += 1

    froze()

    pieceCount += 1

print(len(matrix) - findTopY())