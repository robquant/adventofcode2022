import sys
import pathlib
from itertools import count

from tools import runtime


def part1(field):
    nrows = len(field)
    ncols = len(field[0])
    visible = [[False] * ncols for _ in range(nrows)]

    # Top to bottom, left to right
    for row in range(nrows):
        max_in_row = -1
        for col in range(ncols):
            if field[row][col] > max_in_row:
                max_in_row = field[row][col]
                visible[row][col] = True

    # Top to bottom, right to left
    for row in range(nrows):
        max_in_row = -1
        for col in range(ncols):
            if field[row][ncols - col - 1] > max_in_row:
                max_in_row = field[row][ncols - col - 1]
                visible[row][ncols - col - 1] = True

    # Left to right, top to bottom
    for col in range(ncols):
        max_in_col = -1
        for row in range(nrows):
            if field[row][col] > max_in_col:
                max_in_col = field[row][col]
                visible[row][col] = True

    # Left to right, bottom to top
    for col in range(ncols):
        max_in_col = -1
        for row in range(nrows):
            if field[nrows - row - 1][col] > max_in_col:
                max_in_col = field[nrows - row - 1][col]
                visible[nrows - row - 1][col] = True

    count_visible = 0
    for row in range(nrows):
        for col in range(ncols):
            if visible[row][col]:
                count_visible += 1
    return count_visible


def part2(field):
    nrows = len(field)
    ncols = len(field[0])

    best_scenic_score = 0

    for row in range(nrows):
        for col in range(ncols):
            tree = field[row][col]

            score_left = 0
            for n in range(col - 1, -1, -1):
                score_left += 1
                if tree <= field[row][n]:
                    break

            score_right = 0
            for n in range(col + 1, ncols):
                score_right += 1
                if tree <= field[row][n]:
                    break

            score_up = 0
            for n in range(row - 1, -1, -1):
                score_up += 1
                if tree <= field[n][col]:
                    break

            score_down = 0
            for n in range(row + 1, nrows):
                score_down += 1
                if tree <= field[n][col]:
                    break

            score = score_left * score_right * score_up * score_down
            if score > best_scenic_score:
                best_scenic_score = score
    return best_scenic_score


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]

    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    # lines = ["30373", "25512", "65332", "33549", "35390"]
    field = []
    for line in lines:
        field.append([int(item) for item in line.rstrip("\n")])

    print("Part 1:", part1(field))
    print("Part 2:", part2(field))


if __name__ == "__main__":
    main()
