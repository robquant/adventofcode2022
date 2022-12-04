import sys
import pathlib
from itertools import islice
from more_itertools import split_at

from tools import runtime


def part1(elves):
    return max(sum(elve) for elve in elves)


def part2(elves):
    top3 = islice(sorted((sum(elve) for elve in elves), reverse=True), 3)
    return sum(top3)


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]

    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    elves = [[int(item.rstrip("\n")) for item in elve]
             for elve in split_at(lines, lambda line: line == "\n")]

    print(part1(elves))
    print(part2(elves))


if __name__ == "__main__":
    main()
