from Day_4.assignment_pair import AssignmentPair


class CleanupAssignments:
    def __init__(self):
        self.pairs = []

    def setup(self):
        with open("input.txt") as f:
            self.pairs = [AssignmentPair(line.rstrip()) for line in f]

    def nr_of_pairs_fully_contains(self):
        nr = 0
        for pair in self.pairs:
            if pair.fully_contains():
                nr += 1
        return nr

    def nr_of_pairs_partly_contains(self):
        nr = 0
        for pair in self.pairs:
            if pair.partly_contains():
                nr += 1
        return nr


if __name__ == '__main__':
    ca = CleanupAssignments()
    ca.setup()
    print(ca.nr_of_pairs_fully_contains())
    print(ca.nr_of_pairs_partly_contains())
