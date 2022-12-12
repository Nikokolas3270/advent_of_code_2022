#!/usr/bin/env python3

with open("input") as f:
    score = 0

    for l in f.readlines():
        l = l.strip()

        # Rock       A or X
        # Paper      B or Y
        # Scissors   C or Z

        if l in ("A X", "B Y", "C Z"):
            score += 3
        elif l in ("C X", "B Z", "A Y"): # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
            score += 6

        score += ord(l.split()[1]) - ord('W')

    print(score)
