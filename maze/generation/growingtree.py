from mazecreator import MazeCreator


class GrowingTree(MazeCreator):
    def __init__(self, grid, height, width, weight):
        self.weight = weight
        super(GrowingTree, self).__init__(grid, height, width)

    def generate(self):
        print(self.startNode, ", ", self.weight)


if __name__ == '__main__':
    mc = GrowingTree([[]], 10, 10, 10)
    mc.generate()
