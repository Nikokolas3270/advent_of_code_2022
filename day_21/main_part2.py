#!/usr/bin/env python3

import sys

exprs = {}
parents = {}
litterals = {}

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        k = l.index(": ")
        if k == -1:
            raise Exception("Unexpected input line: " + l)
        
        monkey = l[:k]
        value = l[k+2:]

        if monkey != "humn":
            try:
                litterals[monkey] = int(value)
            except:
                expr = tuple(value.split())
                if len(expr) != 3 and expr[1] not in("+", "-", "*", "/"):
                    raise Exception("Unexpected expression: " + value)
                exprs[monkey] = expr
                for child in (expr[0], expr[2]):
                    if child not in parents:
                        parents[child] = set()
                    parents[child].add(monkey)

monkeysToConsider = set()

for monkey in litterals.keys():
    monkeysToConsider |= parents[monkey]

while monkeysToConsider:
    newMonkeysToConsider = set()

    for monkey in monkeysToConsider:
        expr = exprs[monkey]
        firstChild, secondChild = expr[0], expr[2]
        if firstChild in litterals and secondChild in litterals:
            firstLitteral, secondLitteral = litterals[firstChild], litterals[secondChild]
            op = expr[1]
            if op == "+":
                value = firstLitteral + secondLitteral
            elif op == "-":
                value = firstLitteral - secondLitteral
            elif op == "*":
                value = firstLitteral * secondLitteral
            else: # op == "/"
                value = firstLitteral / secondLitteral

            litterals[monkey] = value
            newMonkeysToConsider |= parents[monkey]
    
    monkeysToConsider = newMonkeysToConsider

monkeysToConsiderInitially = set()

for monkey in litterals.keys():
    monkeysToConsiderInitially |= parents[monkey]

def eval(humnValue):
    localLitterals = {"humn": humnValue}

    monkeysToConsider = monkeysToConsiderInitially

    while monkeysToConsider:
        newMonkeysToConsider = set()

        for monkey in monkeysToConsider:
            expr = exprs[monkey]
            childLitterals = []
            for child in (expr[0], expr[2]):
                if child in litterals:
                    childLitterals.append(litterals[child])
                elif child in localLitterals:
                    childLitterals.append(localLitterals[child])
            if len(childLitterals) == 2:
                firstLitteral, secondLitteral = childLitterals[0], childLitterals[1]
                op = expr[1]
                if monkey == "root":
                    return firstLitteral - secondLitteral
                elif op == "+":
                    value = firstLitteral + secondLitteral
                elif op == "-":
                    value = firstLitteral - secondLitteral
                elif op == "*":
                    value = firstLitteral * secondLitteral
                else: # op == "/"
                    value = firstLitteral / secondLitteral

                localLitterals[monkey] = value
                newMonkeysToConsider |= parents[monkey]
        
        monkeysToConsider = newMonkeysToConsider

    print("Did not eval till root :(")

    return 0

minHumnValue = 3200000000000
maxHumnValue = 3300000000000

while minHumnValue < maxHumnValue:
    humnValue = (minHumnValue + maxHumnValue) // 2
    rootValue = eval(humnValue)
    print("%s -> %s" % (humnValue, rootValue))

    if rootValue == 0:
        print(humnValue)
        break
    elif rootValue < 0:
        maxHumnValue = humnValue
    else:
        minHumnValue = humnValue