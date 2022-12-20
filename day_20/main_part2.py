#!/usr/bin/env python3

with open("input") as f:
    numbers = [int(l.strip()) * 811589153 for l in f.readlines()]

ranks = list(range(len(numbers)))

for _ in range(10):
    for rank, number in enumerate(numbers):
        index = ranks.index(rank)
        newIndex = (index + number) % (len(ranks) - 1)
        if index != newIndex:
            d = 1 if newIndex > index else -1
            for k in range(index, newIndex, d):
                ranks[k] = ranks[k+d]
            ranks[newIndex] = rank

index0 = ranks.index(numbers.index(0))

def getFromIndex0(k):
    return numbers[ranks[(index0 + k) % len(ranks)]]

print(getFromIndex0(1000) + getFromIndex0(2000) + getFromIndex0(3000))