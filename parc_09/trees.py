
import random

TREE_LEAVES_PER_ROW = 3


class Tree:


    def __init__(self):

        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):

        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):

        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for _ in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):

        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):

        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):


    def grow(self, sunlight, water):

        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):


    def __str__(self):

        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):

    pass


class QuickTree(Tree):

    pass


class FruitTree(Tree):

    pass


class PineTree(Tree):

    pass
