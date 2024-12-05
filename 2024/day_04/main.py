#! /usr/bin/env python
# https://adventofcode.com/2024/day/4

import re

test_input = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines: list[str]):
    data = []
    for line in lines:
        data.append(re.findall(r"\w", line))
    return data


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()


def part1(grid: list[list[str]], word: str = "XMAS") -> int:
    # For each coord, search 8 directions to see if the chars match word
    x_len = len(grid[0])
    y_len = len(grid)

    # NW, N, NE, W, E, SW, S, SE
    x_dir = (-1, 0, 1, -1, 1, -1, 0, 1)
    y_dir = (-1, -1, -1, 0, 0, 1, 1, 1)

    matches = 0
    potential_starts = []

    for y in range(y_len):
        for x in range(x_len):
            if grid[y][x] == word[0]:
                potential_starts.append((x, y))

    for x, y in potential_starts:
        for direction in range(len(x_dir)):
            cur = []
            for i in range(len(word)):
                x1 = x + i * x_dir[direction]
                y1 = y + i * y_dir[direction]
                if x1 >= 0 and x1 < x_len and y1 >= 0 and y1 < y_len:
                    cur.append(grid[y1][x1])
            if "".join(cur) == word:
                matches += 1

    return matches


def part2(grid: list[list[str]]) -> int:
    x_len = len(grid[0])
    y_len = len(grid)

    matches = 0
    potential_starts = []

    # Plan is to look for the A in the center of the cross, so don't need to check 1st or last row/column. Should also mean that we don't need to check bounds
    for y in range(1, y_len - 1):
        for x in range(1, x_len - 1):
            # print("x,y = ({},{})".format(x, y))
            if grid[y][x] == "A":
                potential_starts.append((x, y))

    for x, y in potential_starts:
        left_cross = "".join([grid[y - 1][x - 1], grid[y][x], grid[y + 1][x + 1]])
        right_cross = "".join([grid[y + 1][x - 1], grid[y][x], grid[y - 1][x + 1]])
        # print("left_cross = {}, right_cross = {}".format(left_cross, right_cross))
        if (left_cross == "MAS" or left_cross == "SAM") and (
            right_cross == "MAS" or right_cross == "SAM"
        ):
            matches += 1

    return matches


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    grid = parse_input(data)

    print("Part 1")
    print(part1(grid))

    print("Part 2")
    print(part2(grid))
