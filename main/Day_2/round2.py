class Round2:
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

    def __init__(self, guideline):
        c1, c2 = guideline.split(' ')
        self.choice_opponent = c1
        self.choice_ending = c2

    def my_choice(self):
        if self.choice_ending == Round2.DRAW:
            return self.choice_opponent
        if self.choice_ending == Round2.LOSE:
            if self.choice_opponent == Round2.ROCK:
                return Round2.SCISSORS
            elif self.choice_opponent == Round2.PAPER:
                return Round2.ROCK
            elif self.choice_opponent == Round2.SCISSORS:
                return Round2.PAPER
        else:
            if self.choice_opponent == Round2.ROCK:
                return Round2.PAPER
            elif self.choice_opponent == Round2.PAPER:
                return Round2.SCISSORS
            elif self.choice_opponent == Round2.SCISSORS:
                return Round2.ROCK

    def total_score(self):
        return score_ending(self.choice_ending) + score_choice(self.my_choice())


def score_choice(choice):
    if choice == Round2.ROCK:
        return 1
    elif choice == Round2.PAPER:
        return 2
    elif choice == Round2.SCISSORS:
        return 3


def score_ending(ending):
    if ending == Round2.LOSE:
        return 0
    elif ending == Round2.DRAW:
        return 3
    elif ending == Round2.WIN:
        return 6
