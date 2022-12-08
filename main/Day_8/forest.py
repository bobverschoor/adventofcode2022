class Forest:
    def __init__(self):
        self.input = []
        self.trees = []

    def setup(self):
        with open("input.txt") as f:
            self.input = [line.rstrip() for line in f]

    def plant_trees(self):
        for line in self.input:
            line = line.strip()
            tree_line = []
            if line != "":
                for tree in line:
                    tree_line.append(tree)
                self.trees.append(tree_line)

    def is_visible_from_outside(self, x, y):
        if x == 0 or x == len(self.trees[x]) - 1:
            return True
        if y == 0 or y == len(self.trees):
            return True
        if self.is_visible_horizontal(x, y):
            return True
        if self.is_visible_vertical(x, y):
            return True
        return False

    def is_visible_horizontal(self, x, y):
        height = self.trees[y][x]
        left_visible = True
        right_visible = True
        for i in range(x - 1, -1, -1):
            if self.trees[y][i] >= height:
                left_visible = False
                break
        for i in range(x + 1, len(self.trees[y])):
            if self.trees[y][i] >= height:
                right_visible = False
                break
        return left_visible or right_visible

    def is_visible_vertical(self, x, y):
        height = self.trees[y][x]
        up_visible = True
        down_visible = True
        for i in range(y - 1, -1, -1):
            if self.trees[i][x] >= height:
                up_visible = False
                break
        for i in range(y + 1, len(self.trees)):
            if self.trees[i][x] >= height:
                down_visible = False
                break
        return up_visible or down_visible

    def total_visible(self):
        total = 0
        for y in range(0, len(self.trees)):
            for x in range(0, len(self.trees[y])):
                if self.is_visible_from_outside(x, y):
                    total += 1
        return total

    def scenic_left(self, x, y):
        non_blocked = 0
        height = self.trees[y][x]
        for i in range(x - 1, -1, -1):
            non_blocked += 1
            if self.trees[y][i] >= height:
                break
        return non_blocked

    def scenic_right(self, x, y):
        non_blocked = 0
        height = self.trees[y][x]
        for i in range(x + 1, len(self.trees[y])):
            non_blocked += 1
            if self.trees[y][i] >= height:
                break
        return non_blocked

    def scenic_up(self, x, y):
        non_blocked = 0
        height = self.trees[y][x]
        for i in range(y - 1, -1, -1):
            non_blocked += 1
            if self.trees[i][x] >= height:
                break
        return non_blocked

    def scenic_down(self, x, y):
        non_blocked = 0
        height = self.trees[y][x]
        for i in range(y + 1, len(self.trees)):
            non_blocked += 1
            if self.trees[i][x] >= height:
                break
        return non_blocked

    def scenic_score(self, x, y):
        left = self.scenic_left(x, y)
        right = self.scenic_right(x, y)
        up = self.scenic_up(x, y)
        dn = self.scenic_down(x, y)
        return left * right * up * dn

    def maximum_scenic_score(self):
        maximum = 0
        for y in range(0, len(self.trees)):
            for x in range(0, len(self.trees[y])):
                scenic_score = self.scenic_score(x, y)
                if maximum < scenic_score:
                    maximum = scenic_score
        return maximum


if __name__ == '__main__':
    forest = Forest()
    forest.setup()
    forest.plant_trees()
    print(forest.total_visible())
    print(forest.maximum_scenic_score())
