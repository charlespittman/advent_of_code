#! /usr/bin/env python
# https://adventofcode.com/2015/day/2

with open("input") as file:
    data = [line.strip().split("x") for line in file.readlines()]
    for row in data:
        for idx, item in enumerate(row):
            row[idx] = int(item)


def ribbon(length, width, height):
    bow = length * width * height
    side_1, side_2 = sorted([length, width, height])[:2]
    wrap = 2 * (side_1 + side_2)
    return bow + wrap


def wrapping_paper(length, width, height):
    xy_area = length * width
    yz_area = width * height
    xz_area = height * length
    surface_area = 2 * sum([xy_area, yz_area, xz_area])
    return surface_area + min([xy_area, yz_area, xz_area])


def solve(data):
    total_paper = 0
    total_ribbon = 0
    for length, width, height in data:
        total_paper += wrapping_paper(length, width, height)
        total_ribbon += ribbon(length, width, height)
    return total_paper, total_ribbon


solution = solve(data)
print(solution)
