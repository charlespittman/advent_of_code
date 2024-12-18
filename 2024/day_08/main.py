#! /usr/bin/env python
# https://adventofcode.com/2024/day/8

from typing import NamedTuple
from itertools import combinations
from math import dist, isclose

DEBUG = False


class Point(NamedTuple):
    x: int
    y: int


def get_input(use_sample_data=False):
    result = None
    test_input = [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]

    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines):
    grid = []
    for line in lines:
        grid.append([c for c in line])
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) == 0


def antinode(location: Point, a1: Point, a2: Point) -> bool:
    a1_dist = dist(location, a1)
    a2_dist = dist(location, a2)
    return collinear(location, a1, a2) and (
        isclose(a1_dist, 2 * a2_dist) or isclose(2 * a1_dist, a2_dist)
    )


def get_frequencies(grid: list[list[str]]) -> dict[str, list[Point]]:
    frequencies: dict[str, list[Point]] = {}
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] != ".":
                antenna = grid[y][x]
                if antenna in frequencies:
                    frequencies[antenna].append(Point(x, y))
                else:
                    frequencies[antenna] = [Point(x, y)]
    return frequencies


def part1(grid: list[list[str]], frequencies: dict) -> int:
    antinodes = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            loc = Point(x, y)
            for freq, points in frequencies.items():
                for pair in combinations(points, 2):
                    a1, a2 = pair
                    a1_dist = dist(loc, a1)
                    a2_dist = dist(loc, a2)
                    anode = antinode(loc, a1, a2)
                    if DEBUG:
                        print(
                            "loc={}, freq={}, a1={}, a2={}, a1_dist={}, a2_dist={}, anode={}".format(
                                loc, freq, a1, a2, a1_dist, a2_dist, anode
                            )
                        )
                    if anode:
                        antinodes.add(loc)
    return len(antinodes)


def part2(grid, frequencies):
    antinodes = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            loc = Point(x, y)
            for freq, points in frequencies.items():
                for pair in combinations(points, 2):
                    a1, a2 = pair
                    if collinear(loc, a1, a2):
                        antinodes.add(loc)
    return len(antinodes)


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    grid = parse_input(data)
    print_grid(grid)

    frequencies = get_frequencies(grid)
    for freq in sorted(frequencies.keys()):
        print("{}: {}".format(freq, frequencies[freq]))

    print("Part 1")
    print(part1(grid, frequencies))

    print("Part 2")
    print(part2(grid, frequencies))
