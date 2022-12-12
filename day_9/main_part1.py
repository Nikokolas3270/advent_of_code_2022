#!/usr/bin/env python3

def sign(v):
    return 1 if v >= 0 else -1

class Pos:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __hash__(self):
        return hash((self._x, self._y))

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __repr__(self):
        return "(%s, %s)" % (self._x, self._y)
    
    def add(self, other):
        return Pos(self._x + other._x, self._y + other._y)

    def dist(self, other):
        return max(abs(self._x - other._x), abs(self._y - other._y))
    
    def attract(self, other):
        d = self.dist(other)

        if d <= 1:
            return other
        elif d == 2:
            if abs(self._x - other._x) < abs(self._y - other._y):
                return Pos(self._x, self._y + sign(other._y - self._y))
            else:
                return Pos(self._x + sign(other._x - self._x), self._y)
        else:
            raise Exception("%s cannot attract %s, distance (%s) is bigger than 2" % (self, other, d))

headPos = Pos(0, 0)
tailPos = headPos
visitedTailPos = set([tailPos])

with open("input") as f:
    for l in f.readlines():
        if l.startswith("R"):
            dir = Pos(1, 0)
        elif l.startswith("U"):
            dir = Pos(0, -1)
        elif l.startswith("L"):
            dir = Pos(-1, 0)
        elif l.startswith("D"):
            dir = Pos(0, 1)
        else:
            raise Exception("Unexpected input: %s" % l)

        count = int(l.strip()[2:])

        while count > 0:
            headPos = headPos.add(dir)
            tailPos = headPos.attract(tailPos)
            visitedTailPos.add(tailPos)
            count -= 1

    print(len(visitedTailPos))
