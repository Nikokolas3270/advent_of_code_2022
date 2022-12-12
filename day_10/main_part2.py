#!/usr/bin/env python3

with open("input") as f:
    screen = [[' ' for x in range(40)] for y in range(6)]
    cycleNumber = 0
    X = 1

    def finishCycle():
        global cycleNumber

        x = cycleNumber % 40
        y = cycleNumber // 40

        if abs(x - X) <= 1:
            screen[y][x]='#'

        cycleNumber += 1

    for l in f.readlines():
        l = l.strip()

        if l == "noop":
            finishCycle()
        elif l.startswith("addx "):
            finishCycle()
            finishCycle()
            X += int(int(l[5:]))
        else:
            raise Exception("Unknown instruction: " + l)

    print('\n'.join([''.join(row) for row in screen]))
