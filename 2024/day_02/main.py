#! /usr/bin/env python
# https://adventofcode.com/2024/day/2

test_input = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines: list[str]) -> list[list[int]]:
    data = []
    for line in lines:
        data.append([int(d) for d in line.split()])
    return data


def is_increasing(report: list[int]) -> bool:
    return True if report == sorted(report) else False


def is_decreasing(report: list[int]) -> bool:
    return True if report == sorted(report, reverse=True) else False


def is_small_steps(report: list[int]) -> bool:
    for idx, level in enumerate(report):
        if idx >= 0 and idx < len(report) - 1:
            diff = abs(level - report[idx + 1])
            if (diff < 1) or (diff > 3):
                return False
    return True


def safe_report(report: list[int]) -> bool:
    return any([is_increasing(report), is_decreasing(report)]) and is_small_steps(
        report
    )


def part1(reports: list[list[int]]) -> tuple[list[int]]:
    safe_reports = []
    unsafe_reports = []
    for report in reports:
        safe = safe_report(report)
        if safe:
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)
    return safe_reports, unsafe_reports


def part2(reports: list[list[int]]) -> tuple[list[int]]:
    safe_reports = []
    unsafe_reports = []
    for report in reports:
        safe = safe_report(report)
        if safe:
            safe_reports.append(report)
        else:
            for idx in range(len(report)):
                if safe_report(report[0:idx] + report[idx + 1 :]):
                    safe = True
            if safe:
                safe_reports.append(report)
            else:
                unsafe_reports.append(report)
    return safe_reports, unsafe_reports


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    reports = parse_input(data)

    print("Part 1")
    safe, unsafe = part1(reports)
    print("safe: {}, unsafe: {}".format(len(safe), len(unsafe)))

    print("Part 2")
    safe, unsafe = part2(reports)
    print("safe: {}, unsafe: {}".format(len(safe), len(unsafe)))
