#!/usr/bin/env python3

map = []

with open("input") as f:
    for l in f.readlines():
        map.append([int(c) for c in l.strip()])

height = len(map)
width = len(map[0])

def scenicScore(x, y):
    totalScore = 1
    size = map[y][x]

    score = 0
    for xx in range(x-1, -1, -1):
        score += 1
        if map[y][xx] >= size:
            break
    totalScore *= score 

    score = 0
    for xx in range(x+1,width):
        score += 1
        if map[y][xx] >= size:
            break
    totalScore *= score 

    score = 0
    for yy in range(y-1, -1, -1):
        score += 1
        if map[yy][x] >= size:
            break
    totalScore *= score 

    score = 0
    for yy in range(y+1,height):
        score += 1
        if map[yy][x] >= size:
            break
    totalScore *= score 
    
    return totalScore

bestScenicScore = 0

for x in range(width):
    for y in range(height):
        bestScenicScore = max(bestScenicScore, scenicScore(x, y))

print(bestScenicScore)