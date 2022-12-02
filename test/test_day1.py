import unittest

from Day_1.calorie_counting import CalorieCounting


class TestDay1(unittest.TestCase):
    def setUp(self):
        cc = CalorieCounting()
        cc.input = TEST_INPUT
        cc.divide_among_elves()
        self.cc = cc

    def test_splitsing_items_by_elves(self):
        self.assertEqual(5, self.cc.nr_of_elves())
        self.assertEqual(6000, self.cc.get_elf(1).total_calories())
        self.assertEqual(24000, self.cc.get_elf_with_most_calories().total_calories())

    def test_top3_calories(self):
        elf1, elf2, elf3 = self.cc.get_top3_elves()
        self.assertEqual(45000, elf1.total_calories() + elf2.total_calories() + elf3.total_calories())


if __name__ == '__main__':
    unittest.main()

TEST_INPUT = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
