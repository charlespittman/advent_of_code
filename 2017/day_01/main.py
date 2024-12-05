#! /usr/bin/env python
# https://adventofcode.com/2017/day/1

test_input = ["12131415"]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines: list[str]):
    return [int(x) for x in list(lines[0])]


def part1(captcha: list[int]) -> int:
    total = 0
    for idx, digit in enumerate(captcha):
        next_idx = (idx + 1) % len(captcha)
        if digit == captcha[next_idx]:
            total += digit
    return total


def part2(captcha: list[int]) -> int:
    total = 0
    for idx, digit in enumerate(captcha):
        next_idx = (idx + int(len(captcha) / 2)) % len(captcha)
        if digit == captcha[next_idx]:
            total += digit
    return total


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    captcha = parse_input(data)

    print("Part 1")
    print(part1(captcha))

    print("Part 2")
    print(part2(captcha))
