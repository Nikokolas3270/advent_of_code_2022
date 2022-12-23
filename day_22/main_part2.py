#!/usr/bin/env python3

import re

with open("input") as f:
    lines = f.readlines()
    matrix = [l[:-1] for l in lines[:-2]]
    orders = re.split("(R|L)", lines[-1])

size = 50
x, y = size, 0
dx, dy = 1, 0

#    111222
#    111222
#    111222
#    333
#    333
#    333
# 444555
# 444555
# 444555
# 666
# 666
# 666

def increase():
    global x, y, dx, dy

    if dy == -1:
        if y == 0:
            if x < 100: # From 1 to 6
                x, y = 0, x + 100
                dx, dy = 1, 0
            else: # From 2 to 6
                x, y = x - 100, 199
            return
        elif y == 100:
            if x < 50: # From 4 to 3
                x, y = 50, 50 + x
                dx, dy = 1, 0
                return
    elif dy == 1:
        if y == 49:
            if x >= 100: # From 2 to 3
                x, y = 99, x - 50
                dx, dy = -1, 0
                return
        elif y == 149:
            if x >= 50: # From 5 to 6
                x, y = 49, 100 + x
                dx, dy = -1, 0
                return
        elif y == 199: # From 6 to 2
            x, y = 100 + x, 0
            return
    elif dx == -1:
        if x == 0:
            if y < 150: # From 4 to 1
                x, y = 50, 149 - y
                dx, dy = 1, 0
            else: # From 6 to 1
                x, y = y - 100, 0
                dx, dy = 0, 1
            return
        elif x == 50:
            if y < 50: # From 1 to 4
                x, y = 0, 149 - y
                dx, dy = 1, 0
                return
            elif y < 100: # From 3 to 4
                x, y = y - 50, 100
                dx, dy = 0, 1
                return
    else: # dx == 1
        if x == 49:
            if y >= 150: # From 6 to 5
                x, y = y - 100, 149
                dx, dy = 0, -1
                return
        elif x == 99:
            if y >= 100: # From 5 to 2
                x, y = 149, 149 - y
                dx, dy = -1, 0
                return
            elif y >= 50: # From 3 to 2
                x, y = y + 50, 49
                dx, dy = 0, -1
                return
        elif x == 149: # From 2 to 5
            x, y = 99, 149 - y
            dx, dy = -1, 0
            return

    x, y = x + dx, y + dy

for order in orders:
    if order == "L":
        dx, dy = dy, -dx
    elif order == "R":
        dx, dy = -dy, dx
    else:
        count = int(order)
        while count:
            backup = x, y, dx, dy
            increase()
            if matrix[y][x] == '#':
                x, y, dx, dy = backup
                break
            count -= 1

passwd = 4*(x+1) + 1000*(y+1)

if (dx, dy) == (0, 1):
    passwd += 1
elif (dx, dy) == (-1, 0):
    passwd += 2
elif (dx, dy) == (0, -1):
    passwd += 3

print(passwd)