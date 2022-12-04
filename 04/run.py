import sys
import pathlib

from tools import runtime


def fully_contained(pair_1, pair_2):
    start_contained = pair_2[0] <= pair_1[0] <= pair_2[1]
    end_contained = pair_2[0] <= pair_1[1] <= pair_2[1]
    return start_contained and end_contained


def overlap(pair_1, pair_2):
    start_contained_1 = pair_2[0] <= pair_1[0] <= pair_2[1]
    end_contained_1 = pair_2[0] <= pair_1[1] <= pair_2[1]
    start_contained_2 = pair_1[0] <= pair_2[0] <= pair_1[1]
    end_contained_2 = pair_1[0] <= pair_2[1] <= pair_1[1]
    return start_contained_1 or end_contained_1 or start_contained_2 or end_contained_2


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]

    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    contained_count = 0
    overlap_count = 0
    for line in lines:
        line = line.rstrip('\n')
        sections = line.split(",")
        if len(sections) != 2:
            continue
        pair_1 = sections[0].split("-")
        pair_2 = sections[1].split("-")
        pair_1 = (int(pair_1[0]), int(pair_1[1]))
        pair_2 = (int(pair_2[0]), int(pair_2[1]))
        if fully_contained(pair_1, pair_2) or fully_contained(pair_2, pair_1):
            contained_count += 1
        if overlap(pair_1, pair_2):
            overlap_count += 1
    print("Part 1: ", contained_count)
    print("Part 2: ", overlap_count)


if __name__ == "__main__":
    main()
