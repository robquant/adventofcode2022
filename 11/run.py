import sys

from copy import deepcopy
from dataclasses import dataclass
from tools import runtime
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    if_true: int
    if_false: int
    counter: int = 0


def run_round(monkeys, divide_by_three):
    for i in range(len(monkeys)):
        turn(monkeys, i, divide_by_three)


def turn(monkeys, index, divide_by_three):
    monkey = monkeys[index]
    remainder_by = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    while monkey.items:
        monkey.counter += 1
        item = monkey.items.pop(0)
        item = monkey.operation(item)
        if divide_by_three:
            item //= 3
        else:
            item %= remainder_by

        if monkey.test(item):
            monkeys[monkey.if_true].items.append(item)
        else:
            monkeys[monkey.if_false].items.append(item)


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    monkeys = [
        Monkey(
            items=[50, 70, 54, 83, 52, 78],
            operation=lambda x: x * 3,
            test=lambda x: x % 11 == 0,
            if_true=2,
            if_false=7,
        ),
        Monkey(
            items=[71, 52, 58, 60, 71],
            operation=lambda x: x * x,
            test=lambda x: x % 7 == 0,
            if_true=0,
            if_false=2,
        ),
        Monkey(
            items=[66, 56, 56, 94, 60, 86, 73],
            operation=lambda x: x + 1,
            test=lambda x: x % 3 == 0,
            if_true=7,
            if_false=5,
        ),
        Monkey(
            items=[83, 99],
            operation=lambda x: x + 8,
            test=lambda x: x % 5 == 0,
            if_true=6,
            if_false=4,
        ),
        Monkey(
            items=[98, 98, 79],
            operation=lambda x: x + 3,
            test=lambda x: x % 17 == 0,
            if_true=1,
            if_false=0,
        ),
        Monkey(
            items=[76],
            operation=lambda x: x + 4,
            test=lambda x: x % 13 == 0,
            if_true=6,
            if_false=3,
        ),
        Monkey(
            items=[52, 51, 84, 54],
            operation=lambda x: x * 17,
            test=lambda x: x % 19 == 0,
            if_true=4,
            if_false=1,
        ),
        Monkey(
            items=[82, 86, 91, 79, 94, 92, 59, 94],
            operation=lambda x: x + 7,
            test=lambda x: x % 2 == 0,
            if_true=5,
            if_false=3,
        ),
    ]

    # Part 1
    monkeys_part1 = deepcopy(monkeys)
    for round_number in range(20):
        run_round(monkeys_part1, divide_by_three=True)

    monkeys_part1.sort(key=lambda x: x.counter, reverse=True)
    print(monkeys_part1[0].counter * monkeys_part1[1].counter)

    # Part 2
    monkeys_part2 = deepcopy(monkeys)
    for round_number in range(10000):
        run_round(monkeys_part2, divide_by_three=False)

    monkeys_part2.sort(key=lambda x: x.counter, reverse=True)
    print(monkeys_part2[0].counter * monkeys_part2[1].counter)


if __name__ == "__main__":
    main()
