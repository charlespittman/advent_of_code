#! /usr/bin/env python
# https://adventofcode.com/2015/day/12

import re


def get_input(use_sample_data=False):
    if use_sample_data:
        result = "".join(
            [
                "[1,2,3]",
                '{"a":2,"b":4}',
                "[[[3]]]",
                '{"a":{"b":4},"c":-1}',
                '{"a":[-1,1]}',
                '[-1,{"a":1}]',
                "[]",
                "{}",
            ]
        )
    else:
        with open("input") as f:
            # result = [line.strip() for line in f.readlines()]
            result = f.readline().strip()
    return result


def part1(line):
    return sum([int(n) for n in re.findall(r"-?\d+", line)])


if __name__ == "__main__":
    data = get_input(use_sample_data=False)

    print("Part 1")
    print(part1(data))

    print("Part 2")
