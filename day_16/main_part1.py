#!/usr/bin/env python3

import re
import sys

regexp = re.compile("Valve (?P<V>.+) has flow rate=(?P<Vf>\d+); tunnels? leads? to valves? (?P<cVs>.+)")

valveToFlow = {}
valveToChildren = {}

with open("input") as f:
    for l in f.readlines():
        m = regexp.fullmatch(l.strip())
        if not m:
            sys.exit("Unmatched line: " + l)

        v = m.group("V")
        valveToFlow[v] = int(m.group("Vf"))
        valveToChildren[v] = m.group("cVs").split(", ")

cache = {}

def findBestScore(currentValve, openedValves, remainingTime, visits):
    score = 0

    visit = currentValve + "|" + "".join(sorted(openedValves))
    if remainingTime > 0 and visit not in visits:
        cacheKey = visit + "|" + str(remainingTime)
        if cacheKey in cache:
            return cache[cacheKey]

        visits.add(visit)
        remainingTime -= 1
        if currentValve not in openedValves and valveToFlow[currentValve] > 0:
            openedValves.add(currentValve)
            score = remainingTime * valveToFlow[currentValve] + findBestScore(currentValve, openedValves, remainingTime, visits)
            openedValves.remove(currentValve)

        for childValve in valveToChildren[currentValve]:
            score = max(score, findBestScore(childValve, openedValves, remainingTime, visits))
        visits.remove(visit)

        cache[cacheKey] = score

    return score

print(findBestScore("AA", set(["AA"]), 30, set()))