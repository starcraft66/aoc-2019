#!/usr/bin/env python3
sum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        value = int(line.strip())
        sum += int((value/3)-2)

print(sum)
