#!/usr/bin/env python3

import os

with open("input") as f:
    pathToSize = {}
    currentPath = "/"

    for l in f.readlines():
        l = l.strip()

        if l.startswith("$ "):
            cmd = l[2:]

            if cmd.startswith("cd "):
                relPath = cmd[3:]

                if relPath == "/":
                    currentPath = "/"
                elif relPath == "..":
                    currentPath = os.path.dirname(currentPath)
                else:
                    currentPath = os.path.join(currentPath, relPath)
        else:
            if not l.startswith("dir "):
                fileSize = int(l.split()[0])
                dirPath = currentPath
                while True:
                    pathToSize[dirPath] = pathToSize.get(dirPath, 0) + fileSize
                    if dirPath == "/":
                        break
                    dirPath =  os.path.dirname(dirPath)

    sizeToFree = 30000000 - (70000000 - pathToSize["/"])

    if sizeToFree > 0:
        smallestDirSize = -1

        for dirPath, dirSize in pathToSize.items():
            if dirSize >= sizeToFree and (smallestDirSize == -1 or dirSize < smallestDirSize):
                smallestDirSize = dirSize

        print(smallestDirSize)
