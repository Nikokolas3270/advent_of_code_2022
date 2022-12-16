#!/usr/bin/env python3

import re
import sys

regexp = re.compile("Valve (?P<V>.+) has flow rate=(?P<Vf>\d+); tunnels? leads? to valves? (?P<cVs>.+)")

valveToFlow = {}
valveToChildren = {}
maxValveFlow = 0

with open("input") as f:
    for l in f.readlines():
        m = regexp.fullmatch(l.strip())
        if not m:
            sys.exit("Unmatched line: " + l)

        v = m.group("V")
        vf = int(m.group("Vf"))
        valveToFlow[v] = vf
        maxValveFlow = max(maxValveFlow, vf)
        valveToChildren[v] = m.group("cVs").split(", ")

cache = {}
maxScore = 0

def findBestScore(myValve, elephantValve, openedValves, remainingTime, visits, scoreToBeat):
    global maxScore

    score = 0

    if elephantValve > myValve:
        myValve, elephantValve = elephantValve, myValve

    visit = myValve + "|" + elephantValve + "|" + "".join(sorted(openedValves))
    possibleOpeningCount = remainingTime >> 1
    if remainingTime > 0 and visit not in visits and possibleOpeningCount*possibleOpeningCount*maxValveFlow > scoreToBeat:
        cacheKey = visit + "|" + str(remainingTime)
        if cacheKey in cache:
            return cache[cacheKey]

        visits.add(visit)
        remainingTime -= 1

        if myValve not in openedValves and valveToFlow[myValve] > 0:
            openedValves.add(myValve)
            myScore = remainingTime * valveToFlow[myValve]
            
            if elephantValve not in openedValves and valveToFlow[elephantValve] > 0:
                openedValves.add(elephantValve)
                elephantScore = remainingTime * valveToFlow[elephantValve]
                score = myScore + elephantScore + findBestScore(myValve, elephantValve, openedValves, remainingTime, visits, scoreToBeat - myScore - elephantScore)
                openedValves.remove(elephantValve)

            for nextElephantValve in valveToChildren[elephantValve]:
                score = max(score, myScore + findBestScore(myValve, nextElephantValve, openedValves, remainingTime, visits, scoreToBeat - myScore))

            openedValves.remove(myValve)

        for myNextValve in valveToChildren[myValve]:
            if elephantValve not in openedValves and valveToFlow[elephantValve] > 0:
                openedValves.add(elephantValve)
                elephantScore = remainingTime * valveToFlow[elephantValve]
                score = max(score, elephantScore + findBestScore(myNextValve, elephantValve, openedValves, remainingTime, visits, scoreToBeat - elephantScore))
                openedValves.remove(elephantValve)

            for nextElephantValve in valveToChildren[elephantValve]:
                score = max(score, findBestScore(myNextValve, nextElephantValve, openedValves, remainingTime, visits, scoreToBeat))

        visits.remove(visit)

        cache[cacheKey] = score
        if score > maxScore:
            maxScore = score
            print("Best score so far: %s" % score)

    return score

print(findBestScore("AA", "AA", set(["AA"]), 26, set(), 1991))