#! /usr/bin/env python
# https://adventofcode.com/2015/day/5

import re

with open("input") as file:
    data = file.readlines()


def is_nice(line):
    double_letters = re.search(r"([a-z])\1", line)
    three_vowels = re.search(r"[aeiou].*[aeiou].*[aeiou]", line)
    bad_doubles = re.search(r"(ab)|(cd)|(pq)|(xy)", line)
    two_pair = re.search(r"([a-z][a-z]).*\1", line)
    interrupted_double = re.search(r"([a-z]).\1", line)
    return bool(two_pair) and bool(interrupted_double)


def solve(data):
    nice_strings = []
    for line in data:
        if is_nice(line):
            nice_strings.append(line.strip())
    return nice_strings


solution = solve(data)
print(solution)
print(len(solution))
