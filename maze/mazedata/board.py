from .node import Node
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
    def __init__(self, h=15, w=15):
        if (h < MIN_SIZE or w < MIN_SIZE):
            raise BoardSizeException(h, w)
        self.height = h
        self.width = w
        self.grid = Board.createGrid(self.height, self.width)
        self.startNode = (0, 0)
        self.endNode = (self.height - 1, self.width - 1)

    def __str__(self):
        toPrint = '+'
        # Print top row boundaries
        for i in range(self.width):
            # checking if the top border is intact
            # SHOULD NEVER HAPPEN. If the top doesn't have a complete boundary, something
            # went wrong with the maze gen algorithm
            add = '  ' if (self.grid[0][i].up is not False) else '--'
            toPrint += add + '+'
        toPrint += '\n'
        # if the node has None to the left or below, print a boundary, otherwise leave it open
        for y in range(len(self.grid)):
            leftBorders = '|' if (self.grid[y][0].right is False) else ' '
            bottomBorders = "+"
            for x in range(len(self.grid[y])):
                # uncomment if you want to make each cell display it's name.
                # will require some changes to other code
                # middle = str(self.grid[y][x].name).center(5)
                middle = '  '
                if ((y, x) == self.startNode):
                    middle = 'St'
                elif ((y, x) == self.endNode):
                    middle = 'En'

                leftBorders += middle
                # check the left
                if (self.grid[y][x].left is False):
                    leftBorders += '|'
                else:
                    leftBorders += ' '

                # check the down
                if (self.grid[y][x].down is False):
                    bottomBorders += '--+'
                else:
                    bottomBorders += middle + '+'
            toPrint += leftBorders + '\n'
            toPrint += bottomBorders + '\n'
        return toPrint.strip()

    def createGrid(height, width):
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(Node(x, y))
        return grid

    def makeMaze(self, creator):
        self.grid = creator.generate()


if __name__ == '__main__':
    b = Board()
    print(b)
