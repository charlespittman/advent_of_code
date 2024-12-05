#! /usr/bin/env python
# https://adventofcode.com/2024/day/3

import re
from itertools import chain

MUL_PATTERN = r"mul\(\d+,\d+\)"
DO_PATTERN = r"do\(\)"
DONOT_PATTERN = r"don't\(\)"

test_input = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
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
        data.append(
            re.findall(re.compile(f"{MUL_PATTERN}|{DO_PATTERN}|{DONOT_PATTERN}"), line)
        )
    return list(chain(*data))


def part1(lines):
    total = 0
    for statement in statements:
        if statement.startswith("mul"):
            a, b = re.findall(r"\d+", statement)
            total += int(a) * int(b)
    return total


def part2(lines):
    total = 0
    enabled = True
    for statement in statements:
        if statement == "do()":
            enabled = True
        elif statement == "don't()":
            enabled = False
        else:
            if enabled:
                a, b = re.findall(r"\d+", statement)
                total += int(a) * int(b)
    return total


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    statements = parse_input(data)

    print("Part 1")
    print(part1(statements))

    print("Part 2")
    print(part2(statements))
