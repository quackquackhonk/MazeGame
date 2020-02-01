from .mazecreator import MazeCreator
import random


class GrowingTree(MazeCreator):
    # takes in a board as well as a weight for picking by random over picking the newest.
    def __init__(self, board, weight):
        self.weight = weight
        self.selectedCells = None
        self.visitedCells = None
        super(GrowingTree, self).__init__(board)

    def prepareGen(self, seed=None):
        random.seed(seed)
        genBegin = self.startNode
        self.selectedCells = []
        self.selectedCells.append(genBegin)
        self.visitedCells = []

    def complete(self):
        return len(self.selectedCells) == 0

    def step(self):
        # choose a cell
        cell = self.chooseCell(self.selectedCells)
        # add the selected cell to the visited cells
        if (cell not in self.visitedCells):
            self.visitedCells.append(cell)
        dirs = [MazeCreator.N, MazeCreator.E, MazeCreator.S, MazeCreator.W]
        # edge testing
        # test x borders
        if (cell[0] == 0):
            dirs.remove(MazeCreator.W)
        elif (cell[0] == self.width - 1):
            dirs.remove(MazeCreator.E)
        # test y borders
        if (cell[1] == 0):
            dirs.remove(MazeCreator.N)
        elif (cell[1] == self.height - 1):
            dirs.remove(MazeCreator.S)

        # loop through all possible directons. add the direction to the current cell, and see
        # that new cell has been visited. If it has been visited, repeat with the next direction.
        # If it hasn't been visited, break and use it as the new cell
        random.shuffle(dirs)
        newCell = None
        direction = None
        for d in dirs:
            nc = (cell[0] + d[0], cell[1] + d[1])
            if (nc not in self.visitedCells):
                direction = d
                newCell = nc
                break
        if (newCell is None):
            self.selectedCells.remove(cell)

        # Carve path to the new cell
        if (direction == MazeCreator.N):
            self.grid[cell[1]][cell[0]].setAbove(
                self.grid[newCell[1]][newCell[0]])
        elif (direction == MazeCreator.E):
            self.grid[cell[1]][cell[0]].setRight(
                self.grid[newCell[1]][newCell[0]])
        elif (direction == MazeCreator.S):
            self.grid[cell[1]][cell[0]].setBelow(
                self.grid[newCell[1]][newCell[0]])
        elif (direction == MazeCreator.W):
            self.grid[cell[1]][cell[0]].setLeft(
                self.grid[newCell[1]][newCell[0]])

        # add the new cell to the list of cells to choose from
        if (newCell is not None):
            self.selectedCells.append(newCell)
            self.visitedCells.append(newCell)

    def chooseCell(self, cells):
        r = random.randint(0, 100)
        # pick random
        if (r < self.weight):
            return cells[random.randrange(0, len(cells))]
        else:
            return cells[len(cells) - 1]

    def getNeighbors(self, cell):
        neighborlist = []
        if (cell[0] != 0):
            neighborlist.append((cell[0] - 1, cell[1]))
        if (cell[0] != self.width - 1):
            neighborlist.append((cell[0] + 1, cell[1]))
        # test y borders
        if (cell[1] != 0):
            neighborlist.append((cell[0], cell[1] - 1))
        if (cell[1] != self.height - 1):
            neighborlist.append((cell[0], cell[1] + 1))
        return neighborlist
