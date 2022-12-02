class Round:
    ROCK = "AX"
    PAPER = "BY"
    SCISSORS = "CZ"

    def __init__(self, guideline):
        c1, c2 = guideline.split(' ')
        self.choice_opponent = shape(c1)
        self.choice_mine = shape(c2)

    def score_mine_choice(self):
        if self.choice_mine == self.ROCK:
            return 1
        elif self.choice_mine == self.PAPER:
            return 2
        elif self.choice_mine == self.SCISSORS:
            return 3

    def score_game(self):
        if self.choice_mine == self.choice_opponent:
            return 3
        if self.choice_mine == self.ROCK:
            if self.choice_opponent == self.PAPER:
                return 0
            elif self.choice_opponent == self.SCISSORS:
                return 6
        elif self.choice_mine == self.PAPER:
            if self.choice_opponent == self.ROCK:
                return 6
            elif self.choice_opponent == self.SCISSORS:
                return 0
        elif self.choice_mine == self.SCISSORS:
            if self.choice_opponent == self.ROCK:
                return 0
            elif self.choice_opponent == self.PAPER:
                return 6

    def total_score(self):
        return self.score_mine_choice() + self.score_game()


def shape(character):
    if character in Round.ROCK:
        return Round.ROCK
    elif character in Round.PAPER:
        return Round.PAPER
    elif character in Round.SCISSORS:
        return Round.SCISSORS
