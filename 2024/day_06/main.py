#! /usr/bin/env python
# https://adventofcode.com/2024/day/6

test_input = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines: list[str]) -> list[list[str]]:
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def find_guard(grid: list[list[str]]) -> tuple[int]:
    guard_cursor = ["^", ">", "v", "<"]
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            # print(x, y, grid[y][x])
            if grid[y][x] in guard_cursor:
                return (x, y)


def rotate_clockwise(grid: list[list[str]], x: int, y: int) -> None:
    cursor = grid[y][x]
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    grid[y][x] = turn[cursor]


def move_forward(grid: list[list[str]]) -> tuple[int]:
    move_dir = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    x_len = len(grid[0])
    y_len = len(grid)

    x, y = find_guard(grid)
    cursor = grid[y][x]
    x1 = x + move_dir[cursor][0]
    y1 = y + move_dir[cursor][1]

    # print("x={}, y={}, cursor={}, x1={}, y1={}".format(x, y, cursor, x1, y1))

    if x1 < 0 or x1 >= x_len or y1 < 0 or y1 >= y_len:
        grid[y][x] = "X"
        return None
    if grid[y1][x1] == "#" or grid[y1][x1] == "0":
        rotate_clockwise(grid, x, y)
    else:
        grid[y][x] = "X"
        grid[y1][x1] = cursor
    return (x1, y1)


def part1(grid):
    while find_guard(grid):
        move_forward(grid)

    count = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x] == "X":
                count += 1
    return count


def part2(grid):
    init_pos = find_guard(grid)
    seen_pos = []
    pos_count = {}
    loops = []

    part1(grid)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x] == "X":
                seen_pos.append((x, y))
                pos_count[(x, y)] = 1
    seen_pos.remove(init_pos)  # Can't put an object where the guard starts

    for pos in seen_pos:
        cur_count = pos_count
        grid[init_pos[1]][init_pos[0]] = "^"
        grid[pos[1]][pos[0]] = "0"
        while find_guard(grid):
            move = move_forward(grid)
            cur_count[move] = cur_count.get(move, 0)
            if cur_count[move] > 5:
                loops.append(move)
                grid[pos[1]][pos[0]] = "X"
                break
    print(loops)


if __name__ == "__main__":
    data = get_input(use_sample_data=True)
    grid = parse_input(data)

    print_grid(grid)

    # TODO: Should be copying the grid in each function so they don't overwrite each other. Make more functional.
    # print("Part 1")
    # print(part1(grid))
    # print_grid(grid)

    print("Part 2")
    print(part2(grid))
    print_grid(grid)
