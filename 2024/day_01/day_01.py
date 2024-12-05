#! /usr/bin/env python
# https://adventofcode.com/2024/day/1

test_input = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
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
    a_list = []
    b_list = []
    for line in lines:
        a, b = line.split()
        a_list.append(int(a))
        b_list.append(int(b))
    return sorted(a_list), sorted(b_list)


def part1(left: list[int], right: list[int]) -> int:
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    return distance


def part2(left: list[int], right: list[int]) -> int:
    similarity = 0
    for l in left:
        similarity += l * right.count(l)
    return similarity


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    left, right = parse_input(data)

    # Part 1
    distance = part1(left, right)
    print("part 1:", distance)

    # Part 2
    similarity = part2(left, right)
    print("part 2:", similarity)
