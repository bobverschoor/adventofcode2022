import unittest

from Day_2.round import Round
from Day_2.round2 import score_choice, Round2, score_ending
from Day_2.strategy_guide import StrategyGuide


class TestDay2(unittest.TestCase):
    def test_round(self):
        ronde = Round("A Y")
        self.assertEqual(2, ronde.score_mine_choice())
        self.assertEqual(6, ronde.score_game())
        self.assertEqual(8, ronde.total_score())
        ronde = Round("B X")
        self.assertEqual(1, ronde.score_mine_choice())
        self.assertEqual(0, ronde.score_game())
        self.assertEqual(1, ronde.total_score())
        ronde = Round("C Z")
        self.assertEqual(3, ronde.score_mine_choice())
        self.assertEqual(3, ronde.score_game())
        self.assertEqual(6, ronde.total_score())

    def test_rounds(self):
        strategy = StrategyGuide()
        strategy.rounds = [Round("A Y"), Round("B X"), Round("C Z")]
        self.assertEqual(15, strategy.total_score())

    def test_round_pt2(self):
        ronde = Round2("A Y")
        self.assertEqual(1, score_choice(ronde.my_choice()))
        self.assertEqual(3, score_ending(ronde.choice_ending))
        self.assertEqual(4, ronde.total_score())
        ronde = Round2("B X")
        self.assertEqual(1, score_choice(ronde.my_choice()))
        self.assertEqual(0, score_ending(ronde.choice_ending))
        self.assertEqual(1, ronde.total_score())
        ronde = Round2("C Z")
        self.assertEqual(1, score_choice(ronde.my_choice()))
        self.assertEqual(6, score_ending(ronde.choice_ending))
        self.assertEqual(7, ronde.total_score())

    def test_rounds2(self):
        strategy = StrategyGuide()
        strategy.rounds = [Round2("A Y"), Round2("B X"), Round2("C Z")]
        self.assertEqual(12, strategy.total_score())


if __name__ == '__main__':
    unittest.main()
