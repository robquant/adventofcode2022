import sys
import pathlib

from tools import runtime


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[:]

    lines = open(pathlib.Path(__file__).parent / "input").readlines()
    x = [1]
    for line in lines:
        if line.startswith("noop"):
            x.append(x[-1])
        else:
            val = int(line.split(" ")[1])
            x.append(x[-1])
            x.append(x[-1] + val)

    # Part 1
    cycles = [20, 60, 100, 140, 180, 220]
    total = 0
    for cycle in cycles:
        total += cycle * x[cycle - 1]

    # Part 2
    screen = []
    for cycle in range(1, 241):
        sprite_center = x[cycle - 1]
        crt_pos = (cycle - 1) % 40
        print("Cycle: ", cycle, "Center: ", sprite_center, "Pos: ", crt_pos)
        if abs(sprite_center - crt_pos) <= 1:
            screen.append("#")
            print("#")
        else:
            screen.append(".")
            print(".")

    for line in range(6):
        print("".join(screen[line * 40 : line * 40 + 40]))


if __name__ == "__main__":
    main()
