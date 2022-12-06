from more_itertools import windowed

def find_marker(text, length):
    for index, packet in enumerate(windowed(text, length)):
        if len(set(packet)) == length:
            return index + length


text = open("input").readline().rstrip('\n')
print("Part 1: ", find_marker(text, 4))
print("Part 2: ", find_marker(text, 14))
