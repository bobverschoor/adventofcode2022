import unittest

from Day_4.assignment_pair import AssignmentPair
from Day_4.cleanup_assignments import CleanupAssignments


class TestDay4(unittest.TestCase):
    def test_assignments(self):
        ap = AssignmentPair("2-4,6-8")
        self.assertEqual([2, 3, 4], ap.section_1)
        self.assertEqual([6, 7, 8], ap.section_2)
        self.assertFalse(ap.fully_contains())
        self.assertFalse(ap.partly_contains())
        ap = AssignmentPair("2-3,4-5")
        self.assertEqual([2, 3], ap.section_1)
        self.assertEqual([4, 5], ap.section_2)
        self.assertFalse(ap.fully_contains())
        self.assertFalse(ap.partly_contains())
        ap = AssignmentPair("5-7,7-9")
        self.assertEqual([5, 6, 7], ap.section_1)
        self.assertEqual([7, 8, 9], ap.section_2)
        self.assertFalse(ap.fully_contains())
        self.assertTrue(ap.partly_contains())
        ap = AssignmentPair("2-8,3-7")
        self.assertEqual([2, 3, 4, 5, 6, 7, 8], ap.section_1)
        self.assertEqual([3, 4, 5, 6, 7], ap.section_2)
        self.assertTrue(ap.fully_contains())
        self.assertTrue(ap.partly_contains())
        ap = AssignmentPair("6-6,4-6")
        self.assertEqual([6], ap.section_1)
        self.assertEqual([4, 5, 6], ap.section_2)
        self.assertTrue(ap.fully_contains())
        self.assertTrue(ap.partly_contains())
        ap = AssignmentPair("2-6,4-8")
        self.assertEqual([2, 3, 4, 5, 6], ap.section_1)
        self.assertEqual([4, 5, 6, 7, 8], ap.section_2)
        self.assertFalse(ap.fully_contains())
        self.assertTrue(ap.partly_contains())

    def test_cleanup_assignments(self):
        ca = CleanupAssignments()
        ca.pairs = [AssignmentPair("2-4,6-8"), AssignmentPair("2-3,4-5"), AssignmentPair("5-7,7-9"),
                    AssignmentPair("2-8,3-7"), AssignmentPair("6-6,4-6"), AssignmentPair("2-6,4-8")]
        self.assertEqual(2, ca.nr_of_pairs_fully_contains())
        self.assertEqual(4, ca.nr_of_pairs_partly_contains())


if __name__ == '__main__':
    unittest.main()
