class GroupSizeException(Exception):
    pass


class Group:
    def __init__(self):
        self._rucksacks = []

    @property
    def rucksacks(self):
        return self._rucksacks

    @rucksacks.setter
    def rucksacks(self, new_rucksack):
        if len(self._rucksacks) <= 2:
            self._rucksacks.append(new_rucksack)
        else:
            raise GroupSizeException()

    def size(self):
        return len(self._rucksacks)

    def common_items(self):
        common = self._rucksacks[0].unique_items.intersection(self._rucksacks[1].unique_items,
                                                              self._rucksacks[2].unique_items)
        return ''.join(common)
