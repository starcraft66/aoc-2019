#!/usr/bin/env python3
with open("input.txt", "r") as f:
    for line in f.readlines():
        opcodes = list(map(int,line.split(",")))
        opcodes[1] = 12
        opcodes[2] = 2
        opidx = -4
        while True:
            opidx += 4
            opcode = opcodes[opidx]

            if opcode == 1:
                opcodes[opcodes[opidx+3]] = opcodes[opcodes[opidx+1]] + opcodes[opcodes[opidx+2]]
                continue

            if opcode == 2:
                opcodes[opcodes[opidx+3]] = opcodes[opcodes[opidx+1]] * opcodes[opcodes[opidx+2]]
                continue

            if opcode == 99:
                break

        print(opcodes[0])