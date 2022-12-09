import sys
from dataclasses import dataclass
from typing import Self, Optional
from textwrap import indent
from tools import runtime


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    name: str
    subdirs: dict[str, Self]
    files: dict[str, File]
    parent: Optional[Self] = None

    def add_file(self, _file: File):
        self.files[_file.name] = _file

    def add_subdir(self, subdir: Self):
        self.subdirs[subdir.name] = subdir
        subdir.parent = self

    def __str__(self):
        res = f"{self.name} Size: {self.size()}\n"
        res += indent("\n".join(str(file) for file in self.files.values()), "  ")
        res += indent("\n".join(str(subdir) for subdir in self.subdirs.values()), "  ")
        return res

    def size(self):
        return sum(file.size for file in self.files.values()) + sum(
            subdir.size() for subdir in self.subdirs.values()
        )

    def walk(self, predicate, callback):
        if predicate(self):
            callback(self)
        for subdir in self.subdirs.values():
            subdir.walk(predicate, callback)


@runtime
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    root = Dir("/", {}, {})
    cur_dir = root
    for line in open("input"):
        line = line.rstrip("\n")
        if line.startswith("dir"):
            name = line.split(" ")[1]
            cur_dir.add_subdir(Dir(name, {}, {}))
        elif line[0].isnumeric():
            size, name = line.split(" ")
            cur_dir.add_file(File(name, int(size)))
        elif line.startswith("$ cd"):
            target = line.split(" ")[2]
            if target == "..":
                cur_dir = cur_dir.parent
            elif target == "/":
                cur_dir = root
            else:
                cur_dir = cur_dir.subdirs[target]

    sum = 0

    def smaller_than_100k(dir):
        return dir.size() < 100000

    def callback(dir):
        nonlocal sum
        sum += dir.size()

    root.walk(smaller_than_100k, callback)
    print("Part 1", sum)

    total = 70000000
    need = 30000000
    currently_unused = total - root.size()
    need_to_free = need - currently_unused

    smallest_so_far = total

    def bigger_than_needed(dir):
        return dir.size() > need_to_free

    def smallest(dir):
        nonlocal smallest_so_far
        smallest_so_far = min(smallest_so_far, dir.size())

    root.walk(bigger_than_needed, smallest)
    print("Part 2", smallest_so_far)


if __name__ == "__main__":
    main()
