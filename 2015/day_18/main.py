#! /usr/bin/env python
# https://adventofcode.com/2015/day/18

from math import sqrt


def get_input(use_sample_data: bool = False) -> list[str]:
    if use_sample_data:
        result = [
            ".#.#.#",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            "####..",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data: list[str]) -> dict[tuple[int, int], str]:
    return {(x, y): val for y, line in enumerate(data) for x, val in enumerate(line)}


def print_grid(grid: dict[tuple[int, int], str]) -> None:
    xl = min(x for x, y in grid.keys())
    xh = max(x for x, y in grid.keys())
    yl = min(y for x, y in grid.keys())
    yh = max(y for x, y in grid.keys())
    print(
        "\n".join(
            "".join(grid[(x, y)] for x in range(xl, xh + 1)) for y in range(yl, yh + 1)
        )
    )


def get_neighbors(grid: dict[tuple[int, int], str], pos: tuple[int, int]):
    x0, y0 = pos
    candidates = [
        (x0 - 1, y0 - 1),  # NW
        (x0, y0 - 1),  # N
        (x0 + 1, y0 - 1),  # NE
        (x0 + 1, y0),  # E
        (x0 + 1, y0 + 1),  # SE
        (x0, y0 + 1),  # S
        (x0 - 1, y0 + 1),  # SW
        (x0 - 1, y0),  # W
    ]
    return [p for p in candidates if p in grid]


def light_next_step(grid: dict[tuple[int, int], str], pos: tuple[int, int]) -> bool:
    neighbors = get_neighbors(grid, pos)
    current_light_on = True if grid[pos] == "#" else False
    next_light_on = False
    neighbors_on = 0
    neighbors_off = 0

    for neighbor in neighbors:
        if grid[neighbor] == "#":
            neighbors_on += 1
        elif grid[neighbor] == ".":
            neighbors_off += 1

    if current_light_on:
        next_light_on = True if (neighbors_on == 2 or neighbors_on == 3) else False
    else:
        next_light_on = True if (neighbors_on == 3) else False

    return next_light_on


def grid_next_step(
    grid: dict[tuple[int, int], str], part: int = 1
) -> dict[tuple[int, int], str]:
    next_grid = {}
    grid_length = int(sqrt(len(grid)))  # grid should be square

    if part == 2:
        grid[(0, 0)] = "#"
        grid[(0, grid_length - 1)] = "#"
        grid[(grid_length - 1, 0)] = "#"
        grid[(grid_length - 1, grid_length - 1)] = "#"

    for pos in grid:
        next_grid[pos] = "#" if light_next_step(grid, pos) else "."

    if part == 2:
        next_grid[(0, 0)] = "#"
        next_grid[(0, grid_length - 1)] = "#"
        next_grid[(grid_length - 1, 0)] = "#"
        next_grid[(grid_length - 1, grid_length - 1)] = "#"
    return next_grid


def count_lights_on(grid: dict[tuple[int, int], str]) -> int:
    count = 0
    for pos in grid:
        if grid[pos] == "#":
            count += 1
    return count


if __name__ == "__main__":
    use_sample_data = False
    data = get_input(use_sample_data)
    grid = parse_input(data)
    steps = 5 if use_sample_data else 100

    print("Part 1")
    grid_1 = grid
    for x in range(steps):
        grid_1 = grid_next_step(grid_1)
    print(count_lights_on(grid_1))

    print("Part 2")
    grid_2 = grid
    for x in range(steps):
        grid_2 = grid_next_step(grid_2, part=2)
    print(count_lights_on(grid_2))
