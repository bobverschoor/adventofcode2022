class Elf:
    def __init__(self, elf_id):
        self._id = elf_id
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, waarde):
        self._items.append(waarde)

    def total_calories(self):
        calory= 0
        for item in self.items:
            calory += int(item)
        return calory