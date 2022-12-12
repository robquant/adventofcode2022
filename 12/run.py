import sys
from heapq import *

from tools import runtime

# Simplified Dijkstra without weights
def dijkstra(edges, start, end):
    q = [(0, start)]
    visited = set()
    through = {}
    while q:
        dist, current = heappop(q)
        if current == end:
            break
        if current in visited:
            continue
        for neighbor in edges[current]:
            if neighbor not in visited:
                heappush(q, (dist + 1, neighbor))
                through[neighbor] = current
        visited.add(current)
    path = []
    current = end
    if current not in through:
        return []
    while current != start:
        path.append(current)
        current = through[current]
    path.append(start)
    path.reverse()
    return path


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    field = []
    for line in open("input"):
        field.append(list(line.rstrip("\n")))
    possible_starts = []
    for i, line in enumerate(field):
        if "S" in line:
            start = (i, line.index("S"))
            line[start[1]] = "a"
        if "E" in line:
            end = (i, line.index("E"))
            line[end[1]] = "z"
        for j, char in enumerate(line):
            if char == "a":
                possible_starts.append((i, j))

    def get_neighbors(pos):
        x, y = pos
        neighbors = []
        if x > 0:
            if ord(field[x - 1][y]) - ord(field[x][y]) <= 1:
                neighbors.append((x - 1, y))
        if x < len(field) - 1:
            if ord(field[x + 1][y]) - ord(field[x][y]) <= 1:
                neighbors.append((x + 1, y))
        if y > 0:
            if ord(field[x][y - 1]) - ord(field[x][y]) <= 1:
                neighbors.append((x, y - 1))
        if y < len(field[0]) - 1:
            if ord(field[x][y + 1]) - ord(field[x][y]) <= 1:
                neighbors.append((x, y + 1))
        return neighbors

    neighbours = {}
    for i, line in enumerate(field):
        for j, _ in enumerate(line):
            neighbours[(i, j)] = get_neighbors((i, j))

    print(start, end)
    path = dijkstra(neighbours, start, end)
    print("Part 1:", len(path) - 1)

    min_len = 9999
    for start in possible_starts:
        path = dijkstra(neighbours, start, end)
        if path:
            min_len = min(min_len, len(path) - 1)

    print("Part 2:", min_len)


if __name__ == "__main__":
    main()
