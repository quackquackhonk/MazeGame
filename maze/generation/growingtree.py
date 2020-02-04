from .mazecreator import MazeCreator
import random


class GrowingTree(MazeCreator):
    # takes in a board as well as a weight for picking by random over picking the newest.
    def __init__(self, board, weight):
        self.weight = weight
        super(GrowingTree, self).__init__(board)

    def prepare_gen(self, seed=None):
        random.seed(seed)
        gen_begin = self.start_node
        self.selected_cells = []
        self.selected_cells.append(gen_begin)
        self.visited_cells = []

    def complete(self):
        return len(self.selected_cells) == 0

    def step(self):
        # choose a cell
        cell = self.choose_cell(self.selected_cells)
        # add the selected cell to the visited cells
        if (cell not in self.visited_cells):
            self.visited_cells.append(cell)

        dirs = [MazeCreator.NORTH, MazeCreator.EAST, MazeCreator.SOUTH, MazeCreator.WEST]
        # edge testing
        # test x borders
        if (cell[0] == 0):
            dirs.remove(MazeCreator.WEST)
        elif (cell[0] == self.width - 1):
            dirs.remove(MazeCreator.EAST)
        # test y borders
        if (cell[1] == 0):
            dirs.remove(MazeCreator.NORTH)
        elif (cell[1] == self.height - 1):
            dirs.remove(MazeCreator.SOUTH)
        # loop through all possible directons. add the direction to the current cell, and see
        # that new cell has been visited. If it has been visited, repeat with the next direction.
        # If it hasn't been visited, break and use it as the new cell
        random.shuffle(dirs)
        new_cell = None
        direction = None
        for d in dirs:
            nc = (cell[0] + d[0], cell[1] + d[1])
            if (nc not in self.visited_cells):
                direction = d
                new_cell = nc
                break
        if (new_cell is None):
            self.selected_cells.remove(cell)

        # Carve path to the new cell
        if (direction == MazeCreator.NORTH):
            self.grid[cell[1]][cell[0]].setAbove(
                self.grid[new_cell[1]][new_cell[0]])
        elif (direction == MazeCreator.EAST):
            self.grid[cell[1]][cell[0]].setRight(
                self.grid[new_cell[1]][new_cell[0]])
        elif (direction == MazeCreator.SOUTH):
            self.grid[cell[1]][cell[0]].setBelow(
                self.grid[new_cell[1]][new_cell[0]])
        elif (direction == MazeCreator.WEST):
            self.grid[cell[1]][cell[0]].setLeft(
                self.grid[new_cell[1]][new_cell[0]])

        # add the new cell to the list of cells to choose from
        if (new_cell is not None):
            self.selected_cells.append(new_cell)
            self.visited_cells.append(new_cell)

    def choose_cell(self, cells):
        rand = random.randint(0, 100)
        # pick random
        if (rand < self.weight):
            return cells[random.randrange(0, len(cells))]
        return cells[len(cells) - 1]

    def get_neighbors(self, cell):
        neighbor_list = []
        if (cell[0] != 0):
            neighbor_list.append((cell[0] - 1, cell[1]))
        if (cell[0] != self.width - 1):
            neighbor_list.append((cell[0] + 1, cell[1]))
        # test y borders
        if (cell[1] != 0):
            neighbor_list.append((cell[0], cell[1] - 1))
        if (cell[1] != self.height - 1):
            neighbor_list.append((cell[0], cell[1] + 1))
        return neighbor_list
