#! /usr/bin/env python
# https://adventofcode.com/2015/day/14

import re
from collections import namedtuple


def get_input(use_sample_data=False):
    if use_sample_data:
        result = [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data):
    ReindeerStat = namedtuple("ReindeerStat", ["speed", "run_time", "rest_time"])
    result = {}
    for line in data:
        reindeer, speed, run_time, rest_time = re.match(
            r"([A-Z]\S*)\D*(\d+)\D*(\d+)\D*(\d+)", line
        ).groups()
        result[reindeer] = ReindeerStat(int(speed), int(run_time), int(rest_time))
    return result


def distance_at_time(race_time, reindeer_stat):
    distance = 0
    time_elapsed = 0
    speed = reindeer_stat.speed
    run_time = reindeer_stat.run_time
    rest_time = reindeer_stat.rest_time

    while time_elapsed <= race_time:
        if time_elapsed + run_time <= race_time:
            distance += speed * run_time
        else:
            distance += speed * (race_time - time_elapsed)
        time_elapsed += run_time + rest_time

    return distance


def part1(reindeer_stats, duration=2503):
    first_place = (None, -1)
    for reindeer in reindeer_stats:
        distance = distance_at_time(duration, reindeer_stats[reindeer])
        if distance > first_place[1]:
            first_place = (reindeer, distance)
    return first_place


def part2(reindeer_stats, duration=2053):
    scores = {}
    for tick in range(1, duration + 1):
        winner, _ = part1(reindeer_stats, tick)
        scores[winner] = scores.get(winner, 0) + 1
    print(scores)


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    reindeer_stats = parse_input(data)

    print("Part 1")
    print(part1(reindeer_stats))

    print("Part 2")
    part2(reindeer_stats, duration=2503)
