#!/usr/bin/env python3

with open("input") as f:
    isInInit = True
    stacks = []

    for l in f.readlines():
        l = l.strip()

        if isInInit:
            if l:
                if l[0] == '[':
                    stacksCount = (len(l)+1) >> 2
                    while len(stacks) < stacksCount:
                        stacks.append([])
                    k = 0
                    for i in range(1, len(l), 4):
                        if l[i] != ' ':
                            stacks[k].insert(0, l[i])
                        k += 1
            else:
                isInInit = False
                print(stacks)
        else:
            elts = l.split()
            count = int(elts[1])
            src = int(elts[3]) - 1
            dest = int(elts[5]) - 1

            stacks[dest].extend(stacks[src][-count:])
            stacks[src] = stacks[src][:-count]

print("".join([stack[-1] for stack in stacks]))