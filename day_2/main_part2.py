#!/usr/bin/env python3

with open("input") as f:
    score = 0

    for l in f.readlines():
        enemy, action = l.strip().split()

        # Enemy values
        # - Rock       A
        # - Paper      B
        # - Scissors   C

        # Possible actions
        # - Lose X
        # - Draw Y
        # - Win  Z

        # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

        if action == "X":
            if enemy == "A":
                score += 3 # Playing Scissors
            elif enemy == "B":
                score += 1 # Playing Rock
            else:
                score += 2 # Playing Paper
        elif action == "Y":
            score += 4 + ord(enemy) - ord('A')
        else:
            score += 6
            if enemy == "A":
                score += 2 # Playing Paper
            elif enemy == "B":
                score += 3 # Playing Scissors
            else:
                score += 1 # Playing Rock

    print(score)
