#! /usr/bin/env python
# https://adventofcode.com/2024/day/7

test_input = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines):
    equations = []
    for line in lines:
        y, operands = line.split(":")
        equations.append([int(y), [int(op) for op in operands.split()]])
    return equations


def concat(a, b):
    return str(a) + str(b)


def solve(target: int, nums: list[int], part2: bool):
    if len(nums) == 1:
        return target == nums[0]
    x = nums[0]
    y = nums[1]
    z = nums[2:]
    if solve(target, [x + y] + z, part2):
        return True
    if solve(target, [x * y] + z, part2):
        return True
    if part2:
        if solve(target, [int(concat(x, y))] + z, part2):
            return True
    return False


def part1(equations):
    total = 0
    for eqn in equations:
        target = eqn[0]
        nums = eqn[1]
        if solve(target, nums, part2=False):
            total += target
    return total


def part2(equations):
    total = 0
    for eqn in equations:
        target = eqn[0]
        nums = eqn[1]
        if solve(target, nums, part2=True):
            total += target
    return total


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    equations = parse_input(data)

    print("Part 1")
    print(part1(equations))

    print("Part 2")
    print(part2(equations))
