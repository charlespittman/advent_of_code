#! /usr/bin/env python
# https://adventofcode.com/2015/day/3

with open("input") as file:
    data = file.read()

directions = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def solve(data):
    santa_x, santa_y = (0, 0)
    robot_x, robot_y = (0, 0)
    presents = {(0, 0): 2}
    santas_turn = True

    for direction in data:
        x2, y2 = directions[direction]
        if santas_turn:
            santas_turn = not santas_turn
            santa_x += x2
            santa_y += y2
            presents[(santa_x, santa_y)] = presents.get((santa_x, santa_y), 0) + 1
        else:
            santas_turn = not santas_turn
            robot_x += x2
            robot_y += y2
            presents[(robot_x, robot_y)] = presents.get((robot_x, robot_y), 0) + 1

    houses_visited = len(presents)

    return houses_visited


solution = solve(data)
print(solution)
