import unittest

from Day_3.reorganization import Reorganization, priorityscore
from Day_3.rucksack import Rucksack


class TestDay3(unittest.TestCase):
    def test_rucksack(self):
        rs = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
        self.assertEqual("vJrwpWtwJgWr", rs.compartment_1)
        self.assertEqual("hcsFMMfFFhFp", rs.compartment_2)
        self.assertEqual("p", rs.common_items())
        self.assertEqual(16, priorityscore(rs.common_items()))
        rs = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        self.assertEqual("jqHRNqRjqzjGDLGL", rs.compartment_1)
        self.assertEqual("rsFMfFZSrLrFZsSL", rs.compartment_2)
        self.assertEqual("L", rs.common_items())
        self.assertEqual(38, priorityscore(rs.common_items()))
        rs = Rucksack("PmmdzqPrVvPwwTWBwg")
        self.assertEqual("PmmdzqPrV", rs.compartment_1)
        self.assertEqual("vPwwTWBwg", rs.compartment_2)
        self.assertEqual("P", rs.common_items())
        self.assertEqual(42, priorityscore(rs.common_items()))
        rs = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
        self.assertEqual("v", rs.common_items())
        self.assertEqual(22, priorityscore(rs.common_items()))
        rs = Rucksack("ttgJtRGJQctTZtZT")
        self.assertEqual("t", rs.common_items())
        self.assertEqual(20, priorityscore(rs.common_items()))
        rs = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
        self.assertEqual("s", rs.common_items())
        self.assertEqual(19, priorityscore(rs.common_items()))

    def test_reorganisation(self):
        r = Reorganization()
        r.rucksacks.append(Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"))
        r.rucksacks.append(Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))
        r.rucksacks.append(Rucksack("PmmdzqPrVvPwwTWBwg"))
        r.rucksacks.append(Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"))
        r.rucksacks.append(Rucksack("ttgJtRGJQctTZtZT"))
        r.rucksacks.append(Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"))
        self.assertEqual(157, r.rucksacks_sum())
        r.form_groups()
        self.assertEqual(2, len(r.groups))
        self.assertEqual(3, r.groups[0].size())
        self.assertEqual(3, r.groups[1].size())
        self.assertEqual("r", r.groups[0].common_items())
        self.assertEqual(52, priorityscore(r.groups[1].common_items()))
        self.assertEqual(70, r.groups_sum())


if __name__ == '__main__':
    unittest.main()
