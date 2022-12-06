import unittest

from Day_6.signal import Signal, is_marker_start


class TestDay6(unittest.TestCase):
    def test_signal(self):
        signal = Signal()
        signal.stream = TEST_1
        self.assertFalse(is_marker_start("mjqj"))
        self.assertTrue(is_marker_start("jpqm"))
        self.assertEqual(7, signal.position_start_marker())
        self.assertEqual(19, signal.position_start_message())
        signal.stream = TEST_2
        self.assertEqual(5, signal.position_start_marker())
        self.assertEqual(23, signal.position_start_message())
        signal.stream = TEST_3
        self.assertEqual(6, signal.position_start_marker())
        self.assertEqual(23, signal.position_start_message())
        signal.stream = TEST_4
        self.assertEqual(10, signal.position_start_marker())
        self.assertEqual(29, signal.position_start_message())
        signal.stream = TEST_5
        self.assertEqual(11, signal.position_start_marker())
        self.assertEqual(26, signal.position_start_message())


if __name__ == '__main__':
    unittest.main()


TEST_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
TEST_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
TEST_3 = "nppdvjthqldpwncqszvftbrmjlhg"
TEST_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
TEST_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
