import re

from Day_7.directory import Directory


class DirectoryStructure:
    def __init__(self):
        self.input = []
        self.topdir = None

    def setup(self):
        with open("input.txt") as f:
            self.input = [line.rstrip() for line in f]

    def execute(self):
        current_dir = None
        dirlist = False
        for line in self.input:
            line = line.strip()
            if line != "":
                if line.startswith('$'):
                    dirlist = False
                    command, parameter = parse_command(line)
                    if command == 'cd':
                        if parameter == '..':
                            current_dir = current_dir.parentdir
                        else:
                            if current_dir is not None and parameter in current_dir.subdirs.keys():
                                current_dir = current_dir.subdirs[parameter]
                            else:
                                current_dir = Directory(parameter, current_dir)
                        if not self.topdir:
                            self.topdir = current_dir
                        continue
                    elif command == 'ls':
                        dirlist = True
                        continue
                elif dirlist:
                    current_dir.add_item(line)

    def total_size(self):
        return self.topdir.total_size()

    def calculate_size(self, maximum):
        totalsize = 0
        dirsize = self.topdir.calculate_size({})
        for size in dirsize.values():
            if size <= maximum:
                totalsize += size
        return totalsize

    def calculate_smallest(self):
        dirsize = self.topdir.calculate_size({})
        topdirsize = self.topdir.total_size()
        unused_space = 70000000 - topdirsize
        needed_space = 30000000 - unused_space
        dirsizes = sorted(dirsize.values())
        for dirsize in dirsizes:
            if dirsize > needed_space:
                return dirsize


def parse_command(line):
    cmd = par = ""
    if 'cd' in line:
        match = re.search(r"\$\s(\w+?)\s(/|\.+|\w*)", line)
        cmd = match.group(1)
        par = match.group(2)
    elif 'ls' in line:
        cmd = 'ls'
    return cmd, par


if __name__ == '__main__':
    ds = DirectoryStructure()
    ds.setup()
    ds.execute()
    print(ds.calculate_size(100000))
    print(ds.calculate_smallest())
