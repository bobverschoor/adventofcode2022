import unittest

from Day_7.directorystructure import DirectoryStructure
from Day_7.directory import Directory


class TestDay7(unittest.TestCase):
    def test_directory(self):
        direct = Directory("a", ".")
        self.assertEqual("a", direct.name)
        direct.add_item("dir e")
        direct.add_item("14848514 b.txt")
        direct.add_item("8504156 c.dat")
        size = direct.total_size()
        self.assertEqual(23352670, size)

    def test_directorystructure(self):
        topdir = DirectoryStructure()
        topdir.input = TEST_INPUT.splitlines()
        topdir.execute()
        self.assertEqual(48381165, topdir.total_size())
        self.assertEqual(95437, topdir.calculate_size(100000))
        self.assertEqual(24933642, topdir.calculate_smallest())


if __name__ == '__main__':
    unittest.main()


TEST_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
