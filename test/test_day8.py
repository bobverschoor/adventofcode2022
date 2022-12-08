import unittest

from Day_8.forest import Forest


class TestDay8(unittest.TestCase):
    def test_forest(self):
        forest = Forest()
        forest.input = TEST_INPUT.splitlines()
        forest.plant_trees()
        self.assertFalse(forest.is_visible_from_outside(3, 3))
        self.assertTrue(forest.is_visible_from_outside(0, 0))
        self.assertTrue(forest.is_visible_from_outside(4, 4))
        self.assertTrue(forest.is_visible_from_outside(1, 1))
        self.assertTrue(forest.is_visible_from_outside(2, 1))
        self.assertFalse(forest.is_visible_from_outside(3, 1))
        self.assertTrue(forest.is_visible_from_outside(1, 2))
        self.assertFalse(forest.is_visible_from_outside(2, 2))
        self.assertTrue(forest.is_visible_from_outside(3, 2))
        self.assertFalse(forest.is_visible_from_outside(1, 3))
        self.assertTrue(forest.is_visible_from_outside(2, 3))
        self.assertFalse(forest.is_visible_from_outside(1, 3))
        self.assertTrue(forest.is_visible_from_outside(2, 3))

        self.assertTrue(forest.is_visible_horizontal(1, 2))
        self.assertTrue(forest.is_visible_horizontal(3, 2))
        self.assertFalse(forest.is_visible_horizontal(3, 1))
        self.assertFalse(forest.is_visible_horizontal(1, 3))
        self.assertFalse(forest.is_visible_vertical(1, 2))
        self.assertFalse(forest.is_visible_vertical(3, 1))
        self.assertTrue(forest.is_visible_vertical(2, 3))
        self.assertEqual(21, forest.total_visible())

    def test_scenic(self):
        forest = Forest()
        forest.input = TEST_INPUT.splitlines()
        forest.plant_trees()
        self.assertEqual(1, forest.scenic_up(2, 1))
        self.assertEqual(1, forest.scenic_left(2, 1))
        self.assertEqual(2, forest.scenic_right(2, 1))
        self.assertEqual(2, forest.scenic_down(2, 1))
        self.assertEqual(2, forest.scenic_up(2, 3))
        self.assertEqual(2, forest.scenic_left(2, 3))
        self.assertEqual(2, forest.scenic_right(2, 3))
        self.assertEqual(1, forest.scenic_down(2, 3))
        self.assertEqual(8, forest.maximum_scenic_score())




if __name__ == '__main__':
    unittest.main()


TEST_INPUT = """30373
25512
65332
33549
35390
"""
