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
                value = firstLitteral // secondLitteral
            if monkey == "root":
                print(value)
                sys.exit()
            litterals[monkey] = value
            newMonkeysToConsider |= parents[monkey]
    
    monkeysToConsider = newMonkeysToConsider

print("Did not eval till root :(")