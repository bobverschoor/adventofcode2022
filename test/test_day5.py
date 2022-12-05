import unittest

from Day_5.ship import Ship


class TestDay5(unittest.TestCase):
    def setUp(self) -> None:
        self.ship = Ship()
        self.ship._setup = CRATE_SETUP.splitlines()
        self.ship.setup_crates()
        self.ship._orders = ORDERS_SETUP.splitlines()

    def test_setup_cradles(self):
        ship = self.ship
        self.assertEqual(2, ship._stacks[0].size())
        self.assertEqual("[N]", ship._stacks[0].show_top_item())
        self.assertEqual(3, ship._stacks[1].size())
        self.assertEqual("[D]", ship._stacks[1].show_top_item())
        self.assertEqual(1, ship._stacks[2].size())
        self.assertEqual("[P]", ship._stacks[2].show_top_item())

    def test_exectte_orders(self):
        ship = self.ship
        ship.execute_orders()
        self.assertEqual(1, ship._stacks[0].size())
        self.assertEqual("[C]", ship._stacks[0].show_top_item())
        self.assertEqual(1, ship._stacks[1].size())
        self.assertEqual("[M]", ship._stacks[1].show_top_item())
        self.assertEqual(4, ship._stacks[2].size())
        self.assertEqual("[Z]", ship._stacks[2].show_top_item())
        self.assertEqual("CMZ", ship.show_top_stack())

    def test_execute_orders_for_cratemover_9001(self):
        ship = self.ship
        ship.execute_orders(cratemachine=9001)
        self.assertEqual(1, ship._stacks[0].size())
        self.assertEqual("[M]", ship._stacks[0].show_top_item())
        self.assertEqual(1, ship._stacks[1].size())
        self.assertEqual("[C]", ship._stacks[1].show_top_item())
        self.assertEqual(4, ship._stacks[2].size())
        self.assertEqual("[D]", ship._stacks[2].show_top_item())
        self.assertEqual("MCD", ship.show_top_stack())


if __name__ == '__main__':
    unittest.main()

CRATE_SETUP = """    [D]    
[N] [C]    
[Z] [M] [P]
"""

ORDER_SETUP = """move 1 from 2 to 1"""

ORDERS_SETUP = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""