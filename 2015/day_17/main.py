#! /usr/bin/env python
# https://adventofcode.com/2015/day/17

from itertools import combinations
from math import inf


def get_input(use_sample_data: bool = False) -> list[str]:
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


def parse_input(data: list[str]) -> list[int]:
    return [int(line) for line in data]


def combos_equal_to_sum(
    containers: list[int], total: int = 150
) -> list[tuple[int, ...]]:
    result = []
    for x in range(1, len(containers) + 1):
        combos = combinations(containers, x)
        for combo in combos:
            if sum(combo) == (25 if use_sample_data else total):
                result.append(combo)
    return result


def smallest_set_of_containers(
    containers: list[tuple[int, ...]]
) -> list[tuple[int, ...]]:
    min_length = inf
    for c in containers:
        if len(c) <= min_length:
            min_length = len(c)
    return [c for c in containers if len(c) == min_length]


if __name__ == "__main__":
    use_sample_data = False
    data = get_input(use_sample_data)
    containers = parse_input(data)

    print("Part 1")
    # print(combos_equal_to_sum(containers))
    print(len(combos_equal_to_sum(containers)))

    print("Part 2")
    # print(smallest_set_of_containers(combos_equal_to_sum(containers)))
    print(len(smallest_set_of_containers(combos_equal_to_sum(containers))))
