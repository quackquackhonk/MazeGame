from .mazecreator import MazeCreator
import random


class GrowingTree(MazeCreator):
    # takes in a board as well as a weight for picking by random over picking the newest.
    def __init__(self, board, weight):
        self.weight = weight
        super(GrowingTree, self).__init__(board)

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

    def generate(self, seed=None):
        # seed the random gen
        random.seed(seed)
        # maze generation starts here, and is automatically connected to the startNode
        generationBegin = self.startNode
        # list of coordinates to use as the cells that have been selected
        selectedCells = []
        selectedCells.append(generationBegin)
        visitedCells = []
        while (len(selectedCells) != 0):
            # choose a cell
            cell = self.chooseCell(selectedCells)
            # add the selected cell to the visited cells
            if (cell not in visitedCells):
                visitedCells.append(cell)
            dirs = [MazeCreator.N, MazeCreator.E, MazeCreator.S, MazeCreator.W]
            # edge testing
            # test x borders
            if (cell[0] == 0):
                dirs.remove((-1, 0))
            elif (cell[0] == self.width - 1):
                dirs.remove((1, 0))
            # test y borders
            if (cell[1] == 0):
                dirs.remove((0, -1))
            elif (cell[1] == self.height - 1):
                dirs.remove((0, 1))

            # loop through all possible directons. add the direction to the current cell, and see
            # that new cell has been visited. If it has been visited, repeat with the next direction.
            # If it hasn't been visited, break and use it as the new cell
            random.shuffle(dirs)
            newCell = None
            direction = None
            for d in dirs:
                nc = (cell[0] + d[0], cell[1] + d[1])
                if (nc not in visitedCells):
                    direction = d
                    newCell = nc
                    break
            if (newCell is None):
                selectedCells.remove(cell)

            # Carve path to the new cell
            if (direction == MazeCreator.N):
                self.grid[cell[1]][cell[0]].up = True
                self.grid[newCell[1]][newCell[0]].down = True
            elif (direction == MazeCreator.E):
                self.grid[cell[1]][cell[0]].left = True
                self.grid[newCell[1]][newCell[0]].right = True
            elif (direction == MazeCreator.S):
                self.grid[cell[1]][cell[0]].down = True
                self.grid[newCell[1]][newCell[0]].up = True
            elif (direction == MazeCreator.W):
                self.grid[cell[1]][cell[0]].right = True
                self.grid[newCell[1]][newCell[0]].left = True

            # add the new cell to the list of cells to choose from
            if (newCell is not None):
                selectedCells.append(newCell)
                visitedCells.append(newCell)
        # this should be it
