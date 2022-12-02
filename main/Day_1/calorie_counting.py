from Day_1.elf import Elf


class CalorieCounting:
    def __init__(self):
        self.input = []
        self._elves = []

    def setup(self):
        with open("input.txt") as f:
            self.input = [line.rstrip() for line in f]

    def divide_among_elves(self):
        elf_nr = 1
        elf = Elf(elf_nr)
        for item in self.input:
            if item == "":
                self._elves.append(elf)
                elf_nr += 1
                elf = Elf(elf_nr)
            else:
                elf.items = item
        self._elves.append(elf)

    def nr_of_elves(self):
        return len(self._elves)

    def get_elf(self, elf_nr):
        return self._elves[elf_nr - 1]

    def get_elf_with_most_calories(self):
        highest_calories = 0
        elf_with_highest_calories = None
        for elf in self._elves:
            if elf.total_calories() > highest_calories:
                elf_with_highest_calories = elf
                highest_calories = elf.total_calories()
        return elf_with_highest_calories

    def get_top3_elves(self):
        sorted_elves = sorted(self._elves, key=lambda elf: elf.total_calories(), reverse=True)
        return sorted_elves[0], sorted_elves[1], sorted_elves[2]


if __name__ == '__main__':
    cc = CalorieCounting()
    cc.setup()
    cc.divide_among_elves()
    print(cc.get_elf_with_most_calories().total_calories())
    elf1, elf2, elf3 = cc.get_top3_elves()
    print(elf1.total_calories() + elf2.total_calories() + elf3.total_calories())
