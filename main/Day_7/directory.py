import re

from Day_7.file import File


class Directory:
    def __init__(self, name, parentdir):
        self._name = name
        self.parentdir = parentdir
        self.subdirs = {}
        self.files = []

    def total_size(self):
        size = 0
        for subdir in self.subdirs.values():
            size += subdir.total_size()
        for file in self.files:
            size += file.size()
        return size

    def calculate_size(self, dirsize):
        for subdir in self.subdirs.values():
            size = subdir.total_size()
            dirsize[subdir.name + str(size)] = size
            subdir.calculate_size(dirsize)
        return dirsize

    @property
    def name(self):
        return self._name

    def add_item(self, item):
        if item.startswith('dir'):
            name = parse_line(item)
            if name not in self.subdirs.keys():
                self.subdirs[name] = Directory(name, self)
        else:
            file = File(item)
            self.files.append(file)


def parse_line(line):
    match = re.match(r"dir (.+)", line)
    if match:
        return match.group(1)
    else:
        return line
