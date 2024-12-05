#! /usr/bin/env python
# https://adventofcode.com/2015/day/1

with open("input") as file:
    data = file.read()


def solve(data):
    basement = -1
    floor = 0
    for idx, direction in enumerate(data):
        if direction == "(":
            floor += 1
        if direction == ")":
            floor -= 1
        if floor == -1:
            return idx + 1


print(solve(data))
