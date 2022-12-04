import sys
from tools import runtime
import pathlib
from more_itertools import chunked


def priority(letter):
    if 'A' <= letter <= 'Z':
        return 27 + ord(letter) - ord('A')
    return 1 + ord(letter) - ord('a')


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]
    lines = [
        line.rstrip('\n')
        for line in open(pathlib.Path(__file__).parent / "input")
    ]
    total = 0
    for line in lines:
        compartment_1, compartment_2 = line[:len(line) // 2], line[len(line) //
                                                                   2:]
        both = set(compartment_1) & set(compartment_2)
        assert len(both) == 1
        total += priority(both.pop())
    print(total)

    total = 0
    for group in chunked(lines, 3):
        badge = set(group[0]) & set(group[1]) & set(group[2])
        assert len(badge) == 1
        total += priority(badge.pop())
    print(total)


if __name__ == "__main__":
    main()