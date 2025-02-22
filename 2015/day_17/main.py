#! /usr/bin/env python
# https://adventofcode.com/2015/day/17

from itertools import combinations


def get_input(use_sample_data: bool = False):
    if use_sample_data:
        result = [
            "20",
            "15",
            "10",
            "5",
            "5",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data: list[str]):
    return [int(line) for line in data]


def part1(containers):
    result = []
    for x in range(1, len(containers) + 1):
        combos = combinations(containers, x)
        for combo in combos:
            if sum(combo) == (25 if use_sample_data else 150):
                result.append(combo)
    return result


if __name__ == "__main__":
    use_sample_data = False
    data = get_input(use_sample_data)
    containers = parse_input(data)

    print("Part 1")
    print(len(part1(containers)))

    print("Part 2")
