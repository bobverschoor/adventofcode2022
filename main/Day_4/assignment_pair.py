class AssignmentPair:
    def __init__(self, assignment):
        self.section_1, self.section_2 = section2list(assignment)

    def fully_contains(self):
        biggest, smallest = self.determine_biggest_smallest()
        for item in smallest:
            if item not in biggest:
                return False
        return True

    def partly_contains(self):
        biggest, smallest = self.determine_biggest_smallest()
        for item in smallest:
            if item in biggest:
                return True
        return False

    def determine_biggest_smallest(self):
        biggest = self.section_2
        smallest = self.section_1
        if len(self.section_1) > len(self.section_2):
            biggest = self.section_1
            smallest = self.section_2
        return biggest, smallest


def section2list(assignment):
    sections = assignment.split(',')
    return expand_section(sections[0]), expand_section(sections[1])


def expand_section(section):
    range_start, range_end = section.split('-')
    return list(range(int(range_start), int(range_end) + 1))
