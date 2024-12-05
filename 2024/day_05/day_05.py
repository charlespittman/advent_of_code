#! /usr/bin/env python
# https://adventofcode.com/2024/day/5

test_input = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


def get_input(use_sample_data=False):
    result = None
    if use_sample_data:
        result = test_input
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(lines: list[str]):
    page_ordering_rules = []
    updates_to_print = []
    for line in lines:
        if "|" in line:
            left, right = line.split("|")
            page_ordering_rules.append((int(left), int(right)))
        if "," in line:
            updates_to_print.append([int(page) for page in line.split(",")])
    return page_ordering_rules, updates_to_print


def part1(page_order_rules: list[tuple[int]], updates_to_print: list[list[int]]):
    correctly_ordered = []
    middle_pages = []
    for update in updates_to_print:
        order_applies = []
        for order in page_order_rules:
            left, right = order
            if left in update and right in update:
                if update.index(left) < update.index(right):
                    order_applies.append(True)
                else:
                    order_applies.append(False)
        if all(order_applies):
            correctly_ordered.append(update)

    for order in correctly_ordered:
        middle_pages.append(order[int(len(order) / 2)])
    return sum(middle_pages)


def part2(page_order_rules: list[tuple[int]], updates_to_print: list[list[int]]):
    correctly_ordered = []
    incorrectly_ordered = []
    middle_pages = []
    for update in updates_to_print:
        order_applies = []
        for order in page_order_rules:
            left, right = order
            if left in update and right in update:
                if update.index(left) < update.index(right):
                    order_applies.append(True)
                else:
                    order_applies.append(False)
        if not all(order_applies):
            incorrectly_ordered.append(update)

    # TODO: I know this is a dumb way to do it, but wanted a quick answer. Next step would be to break into a function and run as long as the print order is incorrect. Might also be a way to sort the rules.
    for _ in range(10):
        for update in incorrectly_ordered:
            for order in page_order_rules:
                left, right = order
                if left in update and right in update:
                    left_index = update.index(left)
                    right_index = update.index(right)
                    if left_index > right_index:
                        update[left_index] = right
                        update[right_index] = left

    for order in incorrectly_ordered:
        middle_pages.append(order[int(len(order) / 2)])
    return sum(middle_pages)


if __name__ == "__main__":
    data = get_input(use_sample_data=False)
    page_ordering_rules, updates_to_print = parse_input(data)

    print("Part 1")
    print(part1(page_ordering_rules, updates_to_print))

    print("Part 2")
    print(part2(page_ordering_rules, updates_to_print))
