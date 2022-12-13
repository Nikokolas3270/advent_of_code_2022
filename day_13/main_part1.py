#!/usr/bin/env python3

import json

def compare(obj1, obj2):
    if isinstance(obj1, list):
        if isinstance(obj2, list):
            for item1, item2 in zip(obj1, obj2):
                itemCompare = compare(item1, item2)
                if itemCompare != 0:
                    return itemCompare

            return len(obj1) - len(obj2)
        else:
            return compare(obj1, [obj2])
    else:
        if isinstance(obj2, list):
            return compare([obj1], obj2)
        else:
            return obj1 - obj2

    return True

score = 0
index = 1
left = None

with open("input") as f:
    for l in f.readlines():
        l = l.strip()

        if l:
            obj = json.loads(l)

            if left == None:
                left = obj
            elif compare(left, obj) < 0:
                score += index
        else:
            index += 1
            left = None

print(score)
