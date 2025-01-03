#! /usr/bin/env python
# https://adventofcode.com/2015/day/9

import re
from itertools import pairwise, permutations
from math import inf


def get_input(use_sample_data=False):
    result = None
    test_input = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]

    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data):
    trips = {}
    for line in data:
        src, dst, dist = re.match(r"(\w+) to (\w+) = (\d*)", line).groups()
        trips[(src, dst)] = int(dist)
        trips[(dst, src)] = int(dist)
    return trips


def part1():
    pass


def part2():
    pass


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    trips = parse_input(data)
    locations = set([t[0] for t in trips])
    possible_trips = permutations(locations)

    shortest_trip = inf
    longest_trip = -inf
    for p in possible_trips:
        total_distance = 0
        for leg in pairwise(p):
            total_distance += trips[leg]
        if total_distance < shortest_trip:
            shortest_trip = total_distance
        if total_distance > longest_trip:
            longest_trip = total_distance

    print("Part 1")
    print(shortest_trip)

    print("Part 2")
    print(longest_trip)
