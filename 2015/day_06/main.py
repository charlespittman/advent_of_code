#! /usr/bin/env python
# https://adventofcode.com/2015/day/6

import re

with open("input") as file:
    data = file.readlines()


def parse_line(line):
    instruction = re.search(r"(turn on)|(turn off)|(toggle)", line).group()
    coords = re.findall(r"\d+", line)
    start = (int(coords[0]), int(coords[1]))
    end = (int(coords[2]), int(coords[3]))
    return instruction, start, end


def solve(data):
    rows = 1000
    cols = 1000
    grid = [[0] * rows for _ in [0] * cols]

    for line in data:
        direction, (x1, y1), (x2, y2) = parse_line(line)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                light = grid[x][y]
                if direction == "turn on":
                    grid[x][y] = light + 1
                if direction == "turn off":
                    grid[x][y] = max(0, light - 1)
                if direction == "toggle":
                    grid[x][y] = light + 2
    return sum([sum(row) for row in grid])


solution = solve(data)
print(solution)
