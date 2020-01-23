# Constants
MIN_SIZE = 3


class BoardSizeException(Exception):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def _getMessage(self):
        message = "Nothing's wrong..."
        if (self.height < MIN_SIZE and self.width < MIN_SIZE):
            message = "Board height and width are both less than 1."
        elif (self.height < MIN_SIZE):
            message = "Board height is less than 1"
        elif (self.width < MIN_SIZE):
            message = "Board width is less than 1."
        return message

    @property
    def message(self):
        return self._getMessage()


class Board:

    def __init__(self, n, h=15, w=15):
        if (h < MIN_SIZE or w < MIN_SIZE):
            raise BoardSizeException(h, w)
        self.height = h
        self.width = w
        self.realHeight = h + 2
        self.realWidth = w + 2
        self.grid = Board.createGrid(self.height, self.width, n)
        self.startNode = (0, 1)
        self.endNode = (self.realHeight - 1, self.width)

    def __str__(self):
        toPrint = ""
        for i in range(self.realHeight):
            for j in range(self.realWidth):
                app = ''
                if ((i, j) == self.startNode):
                    app = '[S]'
                elif ((i, j) == self.endNode):
                    app = '[E]'
                else:
                    app = str(self.grid[i][j])
                toPrint = toPrint + app
            toPrint = toPrint + '\n'
        return toPrint

    def createGrid(height, width, n):
        grid = []
        for y in range(height + 2):
            grid.append([])
            for x in range(width + 2):
                if (x == 0 or y == 0 or x == (width + 1) or y == (height + 1)):
                    grid[y].append(n(True))
                else:
                    grid[y].append(n())
                if (not y == 0):
                    grid[y][x].setAbove(grid[y - 1][x])
                if (not x == 0):
                    grid[y][x].setLeft(grid[y][x - 1])
        return grid

    def makeMaze(self, creator):
        creator.grid = self.grid
        self.grid = creator.generate()
