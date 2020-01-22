from mazecreator import MazeCreator
import random


class GrowingTree(MazeCreator):
    def __init__(self, height, width, weight):
        self.weight = weight
        self._DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        super(GrowingTree, self).__init__(height, width)

    def generate(self, grid, seed=None):
        if (self.grid is None):
            raise TypeError("MazeCreator doesn't contain a grid yet.")

        rand = None
        if (seed is None):
            rand = random.seed()
        else:
            rand = random.seed(seed)

        # maze generation starts here, and is automatically connected to the startNode
        generationBegin = (1, 1)
        # list of coordinates to use as the cells that have been selected
        selectedCells = []
        visitedCells = []
        pass


if __name__ == '__main__':
    mc = GrowingTree(10, 10, 10)
    mc.generate([[]])
