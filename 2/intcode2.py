#!/usr/bin/env python3
from sys import exit
with open("input.txt", "r") as f:
    for line in f.readlines():
        for x in range(100):
            for y in range(100):
                opcodes = list(map(int,line.split(",")))
                opcodes[1] = x
                opcodes[2] = y
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
                
                if opcodes[0] == 19690720:
                    print(100 * x + y)
                    exit()