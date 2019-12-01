#!/usr/bin/env python3
total_sum = 0

def calculate_fuel(mass: int) -> int:
    part = int((mass/3)-2)
    if part <= 0:
        return 0
    print(part)
    return part + calculate_fuel(part)

with open("input.txt", "r") as f:
    for line in f.readlines():
        value = int(line.strip())
        total_sum += calculate_fuel(value)

print(total_sum)
