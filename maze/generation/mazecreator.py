
class MazeCreator():

    def __init__(self, height, width):
        self._grid = None
        self.startNode = None
        self.endNode = None
        self.height = height
        self.width = width
        self.realHeight = -1
        self.realWidth = -1

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, grid):
        try:
            x = len(grid)
            y = len(grid[0])
        except IndexError as e:
            raise e
        else:
            self._grid = grid
            self.realHeight = len(grid)
            self.realWidth = len(grid[0])
            self.startNode = (0, 1)
            self.endNode = (self.realHeight - 1, self.width)

    def generate(self):
        pass
