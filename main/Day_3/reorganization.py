from Day_3.group import Group, GroupSizeException
from Day_3.rucksack import Rucksack


class Reorganization:
    def __init__(self):
        self.rucksacks = []
        self.groups = []

    def setup(self):
        with open("input.txt") as f:
            self.rucksacks = [Rucksack(line.rstrip()) for line in f]

    def rucksacks_sum(self):
        return priority_sum(self.rucksacks)

    def groups_sum(self):
        return priority_sum(self.groups)

    def form_groups(self):
        group = Group()
        for rucksack in self.rucksacks:
            try:
                group.rucksacks = rucksack
            except GroupSizeException:
                self.groups.append(group)
                group = Group()
                group.rucksacks = rucksack
        if group.size() > 0:
            self.groups.append(group)


def priority_sum(alist):
    prio = 0
    for item in alist:
        prio += priorityscore(item.common_items())
    return prio


def priorityscore(character):
    priority = 0
    if character.islower():
        priority = ord(character) - 96
    elif character.isupper():
        priority = ord(character) - 38
    return priority


if __name__ == '__main__':
    reor = Reorganization()
    reor.setup()
    print(reor.rucksacks_sum())
    reor.form_groups()
    print(reor.groups_sum())