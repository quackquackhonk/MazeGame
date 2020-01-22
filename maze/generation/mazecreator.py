
class MazeCreator():

    def __init__(self, grid, height, width):
        self.grid = grid
        self.height = height
        self.width = width
        self.realHeight = len(grid)
        self.realWidth = len(grid[0])
        self.startNode = (0, 1)
        self.endNode = (self.realHeight - 1, self.width)

    def generate(self):
        pass
