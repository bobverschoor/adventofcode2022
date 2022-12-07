import re


class File:
    def __init__(self, line):
        size, name = parse_line(line)
        self._name = name
        self._size = size

    def size(self):
        return self._size


def parse_line(line):
    match = re.match(r"(\d+) (.+)", line)
    return int(match.group(1)), match.group(2)

