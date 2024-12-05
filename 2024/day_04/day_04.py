#! /usr/bin/env python
""" 
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2618.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

"""

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
