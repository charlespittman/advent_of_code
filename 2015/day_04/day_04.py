#! /usr/bin/env python
# https://adventofcode.com/2015/day/4

import hashlib

with open("input") as file:
    data = file.read()


def solve(data):
    coin = 0
    while (
        not hashlib.md5(bytes(data + str(coin), "utf-8"))
        .hexdigest()
        .startswith("000000")
    ):
        coin += 1
    return coin


solution = solve(data)
print(solution)
