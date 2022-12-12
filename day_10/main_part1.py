#!/usr/bin/env python3

with open("input") as f:
    score = 0
    cycleNumber = 1
    X = 1

    def finishCycle():
        global score
        global cycleNumber

        if (cycleNumber - 20) % 40 == 0 and cycleNumber <= 220:
            score += cycleNumber * X
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

    print(score)
