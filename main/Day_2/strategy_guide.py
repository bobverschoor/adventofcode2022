from Day_2.round import Round
from Day_2.round2 import Round2


class StrategyGuide:
    def __init__(self):
        self.rounds = []

    def setup(self):
        with open("strategy.txt") as f:
            self.rounds = [Round(line.rstrip()) for line in f]

    def setup2(self):
        with open("strategy.txt") as f:
            self.rounds = [Round2(line.rstrip()) for line in f]

    def total_score(self):
        score = 0
        for ronde in self.rounds:
            score += ronde.total_score()
        return score


if __name__ == '__main__':
    s = StrategyGuide()
    s.setup()
    print("Part1: " + str(s.total_score()))
    s = StrategyGuide()
    s.setup2()
    print("Part2: " + str(s.total_score()))
