#!/usr/bin/env python3

import sys

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

piecesCount = 0
piecesLimit = 1000000000000
mvtIdx = 0

matrix = [['.'] * 7 for _ in range(2000)]
droppedRowsCount = 0

currentTotal = None

def findTopY(y = 0):
    while y < len(matrix) and '#' not in matrix[y]:
        y += 1

    return y

def getTerrain(topY):
    terrain = []
    for x in range(7):
        y = topY
        while y < len(matrix) and matrix[y][x] != '#':
            y += 1
        terrain.append(y - topY)
    return tuple(terrain)

lastTopY = 2005

cache = {}

while piecesCount < piecesLimit:
    pieceIdx = piecesCount % len(pieces)
    lastTopY = findTopY(lastTopY - 5)

    if lastTopY < 10:
        sys.exit("lastTopY is way too small (%s)" % lastTopY)

    terrain = getTerrain(lastTopY)
    key = (pieceIdx, mvtIdx, terrain)
    currentResult = len(matrix) - lastTopY + droppedRowsCount
    if key in cache:
        lastPiecesCount, lastResult = cache[key]
        piecesIncrease = piecesCount - lastPiecesCount
        resultIncrease = currentResult - lastResult
        print("%s %s %s - piecesIncrease %s - resultIncrease %s" % (pieceIdx, mvtIdx, terrain, piecesIncrease, resultIncrease))
        chunksCount = (piecesLimit - 1 - piecesCount) // piecesIncrease
        piecesCount += chunksCount * piecesIncrease
        droppedRowsCount += chunksCount * resultIncrease
        cache = {}
    else:
        cache[key] = (piecesCount, currentResult)

    piece = pieces[pieceIdx]
    y = lastTopY - 3 - len(piece)

    if y < 10:
        matrix = [['.'] * 7 for _ in range(1000)] + matrix[:1000]
        lastTopY += 1000
        y += 1000
        droppedRowsCount += 1000

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
        mvt = mvts[mvtIdx]
        mvtIdx = (mvtIdx + 1) % len(mvts)

        dx = -1 if mvt == '<' else 1
        if canMove(dx, 0):
            x += dx

        if not canMove(0, 1):
            break

        y += 1

    froze()

    piecesCount += 1


print(len(matrix) - findTopY() + droppedRowsCount)