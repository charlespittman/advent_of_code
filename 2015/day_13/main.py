#! /usr/bin/env python
# https://adventofcode.com/2015/day/13

import re
from itertools import permutations


def get_input(use_sample_data=False):
    if use_sample_data:
        result = [
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol.",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
            # result = f.readline().strip()
    return result


def parse_input(data):
    result = {}
    for line in data:
        person, net, val, other = re.match(
            r"([A-Z]\S*).*(lose|gain) (\d*).*([A-Z]\S*).", line
        ).groups()
        val = int(val)
        if net == "lose":
            val *= -1
        result[(person, other)] = val
    return result


def score_arrangement(arrangement, seat_preferences):
    total = 0
    for idx, person in enumerate(arrangement):
        if idx == 0:
            total += seat_preferences.get((person, arrangement[1]), 0)
            total += seat_preferences.get((person, arrangement[-1]), 0)
        elif idx == len(arrangement) - 1:
            total += seat_preferences.get((person, arrangement[0]), 0)
            total += seat_preferences.get((person, arrangement[-2]), 0)
        else:
            total += seat_preferences.get((person, arrangement[idx + 1]), 0)
            total += seat_preferences.get((person, arrangement[idx - 1]), 0)
    return total


def part1(seat_preferences):
    attendees = set([p[0] for p in seat_preferences])
    possible_arrangements = permutations(attendees)
    max_happiness = -1

    for p in possible_arrangements:
        current_score = score_arrangement(p, seat_preferences)
        if current_score > max_happiness:
            max_happiness = current_score
    return max_happiness


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    seat_preferences = parse_input(data)

    print("Part 1")
    print(part1(seat_preferences))

    print("Part 2")
