""" 
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

Your puzzle answer was 400410.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.
 """

import re

with open("input") as file:
    data = file.readlines()


def parse_line(line):
    instruction = re.search(r"(turn on)|(turn off)|(toggle)", line).group()
    coords = re.findall(r"\d+", line)
    start = (int(coords[0]), int(coords[1]))
    end = (int(coords[2]), int(coords[3]))
    return instruction, start, end


def solve(data):
    rows = 1000
    cols = 1000
    grid = [[0] * rows for _ in [0] * cols]

    for line in data:
        direction, (x1, y1), (x2, y2) = parse_line(line)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                light = grid[x][y]
                if direction == "turn on":
                    grid[x][y] = light + 1
                if direction == "turn off":
                    grid[x][y] = max(0, light - 1)
                if direction == "toggle":
                    grid[x][y] = light + 2
    return sum([sum(row) for row in grid])


solution = solve(data)
print(solution)
