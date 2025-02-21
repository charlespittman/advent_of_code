#! /usr/bin/env python
# https://adventofcode.com/2015/day/16


def get_input(use_sample_data: bool = False):
    if use_sample_data:
        result = [
            "Sue 1: children: 3, cats: 7",
            "Sue 2: cats: 0",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data: list[str]):
    result = {}
    for line in data:
        clues = {
            "akitas": None,
            "cars": None,
            "cats": None,
            "children": None,
            "goldfish": None,
            "perfumes": None,
            "pomeranians": None,
            "samoyeds": None,
            "trees": None,
            "vizslas": None,
        }

        sue, tail = line.split(": ", maxsplit=1)
        result[sue] = clues
        for e in tail.split(", "):
            t, n = e.split(": ")
            n = int(n)
            result[sue][t] = n

    return result


def solve(sues):
    for sue in sues:
        if all(
            [
                sues[sue]["akitas"] == None or sues[sue]["akitas"] == 0,
                sues[sue]["cars"] == None or sues[sue]["cars"] == 2,
                sues[sue]["cats"] == None or sues[sue]["cats"] == 7,
                sues[sue]["children"] == None or sues[sue]["children"] == 3,
                sues[sue]["goldfish"] == None or sues[sue]["goldfish"] == 5,
                sues[sue]["perfumes"] == None or sues[sue]["perfumes"] == 1,
                sues[sue]["pomeranians"] == None or sues[sue]["pomeranians"] == 3,
                sues[sue]["samoyeds"] == None or sues[sue]["samoyeds"] == 2,
                sues[sue]["trees"] == None or sues[sue]["trees"] == 3,
                sues[sue]["vizslas"] == None or sues[sue]["vizslas"] == 0,
            ]
        ):
            return sue


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    sues = parse_input(data)

    print("Part 1")
    print(solve(sues))
    print("Part 2")
