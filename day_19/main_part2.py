#!/usr/bin/env python3

import re

regexp = re.compile("Blueprint (?P<id>\d+): Each ore robot costs (?P<oreRobotCost>\d+) ore. Each clay robot costs (?P<clayRobotCost>\d+) ore. Each obsidian robot costs (?P<obsidianRobotOreCost>\d+) ore and (?P<obsidianRobotClayCost>\d+) clay. Each geode robot costs (?P<geodeRobotOreCost>\d+) ore and (?P<geodeRobotObsidianCost>\d+) obsidian.")

class Factory:
    def __init__(self, desc):
        m = regexp.fullmatch(desc)

        if not m:
            raise Exception("Unable to create a factory from below description:\n" + desc)

        self._id = int(m.group("id"))

        self._oreRobotCost = int(m.group("oreRobotCost"))

        self._clayRobotCost = int(m.group("clayRobotCost"))

        self._obsidianRobotOreCost = int(m.group("obsidianRobotOreCost"))
        self._obsidianRobotClayCost = int(m.group("obsidianRobotClayCost"))

        self._geodeRobotOreCost = int(m.group("geodeRobotOreCost"))
        self._geodeRobotObsidianCost = int(m.group("geodeRobotObsidianCost"))

        robotsOreCosts = (self._oreRobotCost, self._clayRobotCost, self._obsidianRobotOreCost, self._geodeRobotOreCost)

        self._maxGeodesCount = 0
        self._cache = {}
    
    def compute(self, time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount, oreCount, clayCount, obsidianCount, geodesCount, couldHaveCreatedOreRobot, couldHaveCreatedClayRobot, couldHaveCreatedObsidianRobot, couldHaveCreatedGeodeRobot):
        key = (time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount, oreCount, clayCount, obsidianCount)
        if key in self._cache:
            return self._cache[key] + geodesCount

        if time == 0:
            return geodesCount

        t = time
        if not clayCount:
            t -= 1
        if not obsidianCount:
            t -= 1

        if geodesCount + geodeRobotsCount*t + 2 * (t-1) * t <= self._maxGeodesCount:
            return 0

        time -= 1

        oreNextCount, clayNextCount, obsidianNextCount, geodesNextCount = oreCount + oreRobotsCount, clayCount + clayRobotsCount, obsidianCount + obsidianRobotsCount, geodesCount + geodeRobotsCount

        canCreateOreRobot = self._oreRobotCost <= oreCount
        canCreateClayRobot = self._clayRobotCost <= oreCount
        canCreateObsidianRobot = self._obsidianRobotOreCost <= oreCount and self._obsidianRobotClayCost <= clayCount
        canCreateGeodeRobot = self._geodeRobotOreCost <= oreCount and self._geodeRobotObsidianCost <= obsidianCount

        resultingGeodesCount = 0

        if not couldHaveCreatedGeodeRobot and canCreateGeodeRobot:
            resultingGeodesCount = max(resultingGeodesCount, self.compute(time,
                oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount + 1,
                oreNextCount - self._geodeRobotOreCost, clayNextCount, obsidianNextCount - self._geodeRobotObsidianCost, geodesNextCount,
                False, False, False, False))

        if not couldHaveCreatedObsidianRobot and canCreateObsidianRobot:
            resultingGeodesCount = max(resultingGeodesCount, self.compute(time,
                oreRobotsCount, clayRobotsCount, obsidianRobotsCount + 1, geodeRobotsCount,
                oreNextCount - self._obsidianRobotOreCost, clayNextCount - self._obsidianRobotClayCost, obsidianNextCount, geodesNextCount,
                False, False, False, False))

        if not couldHaveCreatedClayRobot and canCreateClayRobot:
            resultingGeodesCount = max(resultingGeodesCount, self.compute(time,
                oreRobotsCount, clayRobotsCount + 1, obsidianRobotsCount, geodeRobotsCount,
                oreNextCount - self._clayRobotCost, clayNextCount, obsidianNextCount, geodesNextCount,
                False, False, False, False))

        if not couldHaveCreatedOreRobot and canCreateOreRobot:
            resultingGeodesCount = self.compute(time,
                oreRobotsCount + 1, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount,
                oreNextCount - self._oreRobotCost, clayNextCount, obsidianNextCount, geodesNextCount,
                False, False, False, False)

        couldHaveCreatedOreRobot |= canCreateOreRobot
        couldHaveCreatedClayRobot |= canCreateClayRobot
        couldHaveCreatedObsidianRobot |= canCreateObsidianRobot
        couldHaveCreatedGeodeRobot |= canCreateGeodeRobot

        if not (couldHaveCreatedOreRobot and couldHaveCreatedClayRobot and couldHaveCreatedObsidianRobot and couldHaveCreatedGeodeRobot):
            resultingGeodesCount = max(resultingGeodesCount, self.compute(time,
                oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount,
                oreNextCount, clayNextCount, obsidianNextCount, geodesNextCount,
                couldHaveCreatedOreRobot, couldHaveCreatedClayRobot, couldHaveCreatedObsidianRobot, couldHaveCreatedGeodeRobot))

        self._cache[key] = resultingGeodesCount - geodesCount
        
        if resultingGeodesCount > self._maxGeodesCount:
            self._maxGeodesCount = resultingGeodesCount
            print("Max so far: %s" % self._maxGeodesCount)

        return resultingGeodesCount

    def simulate(self):
        self.compute(32, 1, 0, 0, 0, 0, 0, 0, 0, False, False, False, False)

        print("Geodes opened with factory #%s: %s" % (self._id, self._maxGeodesCount))

        return self._maxGeodesCount

score = 1

with open("input") as f:
    for l in f.readlines()[:3]:
        score *= Factory(l.strip()).simulate()

print(score)