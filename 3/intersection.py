#!/usr/bin/env python3
sum = 0

with open("input.txt", "r") as f:
    board = {}
    for line in f.readlines():
        codes = line.split(",")
        x = 0
        y = 0
        for code in codes:
            if code[0] == "U":
                step = int(code[1:])
                for ystep in range(y, y+step):
                    if (x, ystep) in board:
                        print("cross", (x, ystep))
                        board[(x, ystep)] = True
                    else:
                        board[(x, ystep)] = False
                y += step

            if code[0] == "D":
                step = int(code[1:])
                for ystep in range(y, y-step):
                    if (x, ystep) in board:
                        print("cross", (x, ystep))
                        board[(x, ystep)] = True
                    else:
                        board[(x, ystep)] = False
                y -= step

            if code[0] == "L":
                step = int(code[1:])
                for xstep in range(x, x-step):
                    if (xstep, y) in board:
                        print("cross", (xstep, y))
                        board[(xstep, y)] = True
                    else:
                        board[(xstep, y)] = False
                x -= step

            if code[0] == "R":
                step = int(code[1:])
                for xstep in range(x, x+step):
                    if (xstep, y) in board:
                        print("cross", (xstep, y))
                        board[(xstep, y)] = True
                    else:
                        board[(xstep, y)] = False
                x += step
    
    distance = 99999999999
    for key, value in board.items():
        if value == True:
            manhattan = abs(key[0]) + abs(key[1])
            if manhattan < distance:
                distance = manhattan

    print(distance)
