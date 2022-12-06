import sys

from more_itertools import windowed
from tools import runtime

def find_marker(text, length):
    for index, packet in enumerate(windowed(text, length)):
        if len(set(packet)) == length:
            return index + length

@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    text = open("input").readline().rstrip('\n')
    print("Part 1: ", find_marker(text, 4))
    print("Part 2: ", find_marker(text, 14))

if __name__ == "__main__":
    main()
