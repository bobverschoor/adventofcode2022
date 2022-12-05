import re

from Day_5.stack import Stack


class Ship:
    def __init__(self):
        self._stacks = []
        self._setup = []
        self._orders = []

    def read_input(self):
        setup = []
        orders = []
        setupsection = True
        with open("input.txt") as f:
            lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip()
            if line == "":
                setupsection = False
            if setupsection:
                if "[" in line:
                    setup.append(line)
            else:
                if line:
                    orders.append(line)
        self._setup = setup
        self._orders = orders

    def setup_crates(self):
        for line in self._setup:
            crate = ""
            position = 0
            stack_nr = 1
            for char in line:
                position += 1
                if position % 4 == 0 or position == len(line):
                    if char:
                        crate += char
                    if stack_nr > len(self._stacks):
                        self._stacks.append(Stack())
                    if crate.strip() != "":
                        self._stacks[stack_nr - 1].add_crate(crate)
                    crate = ""
                    stack_nr += 1
                else:
                    crate += char
        for stack in self._stacks:
            stack.reverse_order()

    def execute_orders(self):
        prog = re.compile(r"move (\d+) from (\d+) to (\d+)")
        for order in self._orders:
            execute = prog.match(order)
            if execute is not None:
                self.move_nr_of_crates_from_stack_to_stack(int(execute.group(1)), int(execute.group(2)),
                                                           int(execute.group(3)))

    def execute_orders_9001(self):
        prog = re.compile(r"move (\d+) from (\d+) to (\d+)")
        for order in self._orders:
            execute = prog.match(order)
            if execute is not None:
                self.move_simultaneous_nr_of_crates_from_stack_to_stack(int(execute.group(1)), int(execute.group(2)),
                                                                        int(execute.group(3)))

    def move_nr_of_crates_from_stack_to_stack(self, crates_nr, from_stack_nr, to_stack_nr):
        for nr in range(0, crates_nr):
            crate = self._stacks[from_stack_nr - 1].grab_crate()
            self._stacks[to_stack_nr - 1].add_crate(crate)

    def move_simultaneous_nr_of_crates_from_stack_to_stack(self, crates_nr, from_stack_nr, to_stack_nr):
        crates = self._stacks[from_stack_nr - 1].grab_top_crates(crates_nr)
        self._stacks[to_stack_nr - 1].add_crates(crates)

    def show_top_stack(self):
        top = ""
        for stack in self._stacks:
            top += stack.show_top_item()
        top = top.replace(']', '')
        top = top.replace('[', '')
        return top


if __name__ == '__main__':
    ship = Ship()
    ship.read_input()
    ship.setup_crates()
    print(ship.show_top_stack())
    # ship.execute_orders()
    ship.execute_orders_9001()
    print(ship.show_top_stack())
