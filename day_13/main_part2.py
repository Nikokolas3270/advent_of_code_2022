#!/usr/bin/env python3

import functools
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

objs = []

with open("input") as f:
    for l in f.readlines():
        l = l.strip()

        if l:
            objs.append(json.loads(l))

div1 = [[2]]
div2 = [[6]]

objs.append(div1)
objs.append(div2)

objs.sort(key=functools.cmp_to_key(compare))

print((objs.index(div1)+1)*(objs.index(div2)+1))
