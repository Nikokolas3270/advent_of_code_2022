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

        self._robotsMinOreCost = min(robotsOreCosts)
        self._robotsMaxOreCost = max(robotsOreCosts)
    
    def simulate(self):
        maxGeodesCount = 0
        queue = [(24, 1, 0, 0, 0, 0, 0, 0, 0, False, False, False, False)]

        while queue:
            time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount, oreCount, clayCount, obsidianCount, geodesCount, couldHaveCreatedOreRobot, couldHaveCreatedClayRobot, couldHaveCreatedObsidianRobot, couldHaveCreatedGeodeRobot = queue.pop()

            if time > 0:
                if geodesCount + geodeRobotsCount*time + 2 * (time-1) * time <= maxGeodesCount:
                   continue

                time -= 1

                oreNextCount, clayNextCount, obsidianNextCount, geodesNextCount = oreCount + oreRobotsCount, clayCount + clayRobotsCount, obsidianCount + obsidianRobotsCount, geodesCount + geodeRobotsCount

                robotsQueueItems = []

                needCollecting = False
                canCreateOreRobot = self._oreRobotCost <= oreCount
                canCreateClayRobot = self._clayRobotCost <= oreCount
                canCreateObsidianRobot = self._obsidianRobotOreCost <= oreCount and self._obsidianRobotClayCost <= clayCount
                canCreateGeodeRobot = self._geodeRobotOreCost <= oreCount and self._geodeRobotObsidianCost <= obsidianCount

                if not couldHaveCreatedOreRobot and canCreateOreRobot:
                    robotsQueueItems.append((time, oreRobotsCount + 1, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount, oreNextCount - self._oreRobotCost, clayNextCount, obsidianNextCount, geodesNextCount,
                        False, False, False, False))
                else:
                    needCollecting = True

                if not couldHaveCreatedClayRobot and canCreateClayRobot:
                    robotsQueueItems.append((time, oreRobotsCount, clayRobotsCount + 1, obsidianRobotsCount, geodeRobotsCount, oreNextCount - self._clayRobotCost, clayNextCount, obsidianNextCount, geodesNextCount,
                        False, False, False, False))
                else:
                    needCollecting = True

                if not couldHaveCreatedObsidianRobot and canCreateObsidianRobot:
                    robotsQueueItems.append((time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount + 1, geodeRobotsCount, oreNextCount - self._obsidianRobotOreCost, clayNextCount - self._obsidianRobotClayCost, obsidianNextCount, geodesNextCount,
                        False, False, False, False))
                elif clayRobotsCount > 0:
                    needCollecting = True

                if not couldHaveCreatedGeodeRobot and canCreateGeodeRobot:
                    robotsQueueItems.append((time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount + 1, oreNextCount - self._geodeRobotOreCost, clayNextCount, obsidianNextCount - self._geodeRobotObsidianCost, geodesNextCount,
                        False, False, False, False))
                elif obsidianRobotsCount > 0:
                    needCollecting = True

                if needCollecting:
                    robotsQueueItems.insert(0, (time, oreRobotsCount, clayRobotsCount, obsidianRobotsCount, geodeRobotsCount, oreNextCount, clayNextCount, obsidianNextCount, geodesNextCount,
                        couldHaveCreatedOreRobot or canCreateOreRobot,
                        couldHaveCreatedClayRobot or canCreateClayRobot,
                        couldHaveCreatedObsidianRobot or canCreateObsidianRobot,
                        couldHaveCreatedGeodeRobot or canCreateGeodeRobot))

                queue.extend(robotsQueueItems)
            else:
                maxGeodesCount = max(maxGeodesCount, geodesCount)

        print("Geodes opened with factory #%s: %s" % (self._id, maxGeodesCount))
        
        return maxGeodesCount

    def qualityLevel(self):
        return self._id * self.simulate()

score = 0


with open("input") as f:

    for l in f.readlines():
        score += Factory(l.strip()).qualityLevel()

print(score)