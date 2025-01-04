#! /usr/bin/env python
# https://adventofcode.com/2015/day/10

from itertools import groupby


def get_input(use_sample_data=False):
    if use_sample_data:
        result = ["111322211"]
    else:
        with open("input") as f:
            # result = [line.strip() for line in f.readlines()]
            result = f.readline().strip()
    return result


def parse_input(data):
    pass


def look_and_say(iterations, sequence="1"):
    arr = [sequence]

    def get_sequence(arr, iterations, sequence):
        if iterations == 0:
            return arr
        else:
            curr = "".join(
                str(len(list(group))) + key for key, group in groupby(sequence)
            )
            arr.append(curr)
            get_sequence(arr, iterations - 1, curr)
        return arr

    return get_sequence(arr, iterations, sequence)


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    data = get_input(use_sample_data=False)

    print("Part 1")
    print(len(look_and_say(40, data)[-1]))

    print("Part 2")
    print(len(look_and_say(50, data)[-1]))
