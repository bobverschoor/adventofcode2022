class Rucksack:
    def __init__(self, items):
        half = int(len(items)/2)
        self.compartment_1 = items[:half]
        self.compartment_2 = items[half:]
        self.unique_items = set()
        for item in items:
            self.unique_items.add(item)

    def common_items(self):
        common = ""
        for item in self.compartment_1:
            if item in self.compartment_2:
                if item not in common:
                    common += item
        if len(common) != 1:
            print("Multiple items" + common)
        return common

