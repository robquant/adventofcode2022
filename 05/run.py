import sys
import pathlib
from copy import deepcopy

from parse import compile, findall

from tools import runtime


def move(towers, moves, reverse=True):
    for (n, start, end) in moves:
        taken = towers[start - 1][-n:]
        towers[start - 1] = towers[start - 1][:-n]
        if reverse: taken.reverse()
        towers[end - 1] += taken
    return ''.join(tower[-1] for tower in towers)


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]

    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    tower_lines = []
    for line in lines:
        if line == "\n":
            break
        tower_lines.append(line.rstrip('\n'))
    tower_lines.reverse()

    tower_columns = [
        result.spans[0] for result in findall("{:>d}", tower_lines[0])
    ]
    towers = [[] for _ in range(len(tower_columns))]
    for line in tower_lines[1:]:
        for i, span in enumerate(tower_columns):
            if len(line) >= span[0] and line[span[0]:span[1]] != ' ':
                towers[i].append(line[span[0]:span[1]])

    move_pattern = compile("move {:d} from {:d} to {:d}")
    moves = []
    for line in lines:
        if res := move_pattern.parse(line.rstrip('\n')):
            moves.append(tuple(res))

    after = move(deepcopy(towers), moves)
    print(after)
    after = move(deepcopy(towers), moves, reverse=False)
    print(after)


if __name__ == "__main__":
    main()
