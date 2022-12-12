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

    smallDirSize = 0

    for dirPath, dirSize in pathToSize.items():
        if dirSize <= 100000:
            smallDirSize += dirSize

    print(smallDirSize)
