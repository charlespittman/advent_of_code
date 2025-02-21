#! /usr/bin/env python
# https://adventofcode.com/2015/day/15

import re
from collections import namedtuple

MAX_CAPACITY = 100

Ingredient = namedtuple(
    "Ingredient",
    ["name", "capacity", "durability", "flavor", "texture", "calories"],
)


def get_input(use_sample_data=False):
    if use_sample_data:
        result = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]
    else:
        with open("input") as f:
            result = [line.strip() for line in f.readlines()]
    return result


def parse_input(data):

    result = []
    for line in data:
        name, capacity, durability, flavor, texture, calories = re.match(
            r"(\w*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)",
            line,
        ).groups()

        result.append(
            Ingredient(
                name,
                int(capacity),
                int(durability),
                int(flavor),
                int(texture),
                int(calories),
            )
        )
    return result


def score_cookie(ingredients: list[Ingredient], composition: tuple[int], part: int = 1):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for idx, ingredient in enumerate(ingredients):
        capacity += ingredient.capacity * composition[idx]
        durability += ingredient.durability * composition[idx]
        flavor += ingredient.flavor * composition[idx]
        texture += ingredient.texture * composition[idx]
        calories += ingredient.calories * composition[idx]

    total = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

    if part == 2:
        if calories == 500:
            return total
        else:
            return 0
    else:
        return total


def best_cookie(
    ingredients: list[Ingredient], amounts: list[tuple[int]], part: int = 1
):
    best = 0
    for recipe in amounts:
        score = score_cookie(ingredients, recipe, part)
        if score > best:
            best = score
    return best


if __name__ == "__main__":
    use_sample_data = False
    data = get_input(use_sample_data)
    ingredients = parse_input(data)
    # [print(i) for i in ingredients]

    # TODO: precompute and save, or find a better way to generate totals
    if use_sample_data:
        ingredient_amounts = [
            (x, y)
            for x in range(MAX_CAPACITY + 1)
            for y in range(MAX_CAPACITY + 1)
            if x + y == MAX_CAPACITY
        ]
    else:
        ingredient_amounts = [
            (w, x, y, z)
            for w in range(MAX_CAPACITY + 1)
            for x in range(MAX_CAPACITY + 1)
            for y in range(MAX_CAPACITY + 1)
            for z in range(MAX_CAPACITY + 1)
            if w + x + y + z == MAX_CAPACITY
        ]

    print("Part 1")
    print(best_cookie(ingredients, ingredient_amounts))

    print("Part 2")
    print(best_cookie(ingredients, ingredient_amounts, part=2))
