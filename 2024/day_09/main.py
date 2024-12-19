#! /usr/bin/env python
# https://adventofcode.com/2024/day/9

from itertools import batched

DEBUG = True


def get_input(use_sample_data=False):
    result = None
    test_input = "2333133121414131402"

    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = f.readline().strip()
    return result


def parse_input(line):
    if len(line) % 2 != 0:
        line = line + "0"
    line = [int(x) for x in line]
    disk_in = batched(line, 2)
    disk_img = []
    for idx, (size, free) in enumerate(disk_in):
        for s in range(size):
            disk_img.append(str(idx))
        for f in range(free):
            disk_img.append(".")
        if DEBUG:
            print("idx={}, size={}, free={}".format(idx, size, free))
    return list(disk_img)


def calculate_checksum(disk: list[str]) -> int:
    checksum = 0
    for idx, file_id in enumerate(disk):
        if file_id != ".":
            checksum += idx * int(file_id)
    return checksum


def find_free(disk: list[str], size: int) -> int | None:
    # Scans disk and returns index of first instance of contiguous space of at least size.
    idx = 0
    while idx < len(disk):
        if not is_free(disk, idx):
            idx += 1
            continue
        if disk[idx : idx + size] == list("." * size):
            return idx
        else:
            idx = idx + size - 1
    return None


def is_free(disk: list[str], index: int) -> bool:
    if disk[index] == ".":
        return True
    return False


def part1(disk: list[str]) -> int:
    disk = disk[:]
    left = 0
    right = len(disk) - 1
    for block in disk:
        if left >= right:
            break

        if not is_free(disk, left):
            left += 1
            continue
        if is_free(disk, right):
            right -= 1
            continue

        disk[left] = disk[right]
        disk[right] = "."
        left += 1
        right -= 1

    if DEBUG:
        print(disk)

    return calculate_checksum(disk)


def part2(disk: list[str]) -> int:
    pass


if __name__ == "__main__":
    data = get_input(use_sample_data=True)
    disk = parse_input(data)
    if DEBUG:
        print(data)
        print(disk)

    print("Part 1")
    print(part1(disk))

    print("Part 2")
    print(find_free(disk, 4))
