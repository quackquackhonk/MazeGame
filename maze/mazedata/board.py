from .node import Node

"""
TODO: Improve documentation
"""
# Constants
MIN_SIZE = 3


class BoardSizeException(Exception):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        super(BoardSizeException, self).__init__()

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
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    def __init__(self, h=15, w=15):
        if (h < MIN_SIZE or w < MIN_SIZE):
            raise BoardSizeException(h, w)
        self.height = h
        self.width = w
        self.grid = Board.create_grid(self.height, self.width)
        self.start_node = (0, 0)
        self.end_node = (self.height - 1, self.width - 1)
        self.player = self.start_node

    def __str__(self):
        to_print = '+'
        # Print top row boundaries
        for i in range(self.width):
            # checking if the top border is intact
            # SHOULD NEVER HAPPEN. If the top doesn't have a complete boundary, something
            # went wrong with the maze gen algorithm
            add = '  ' if (self.grid[0][i].up is not False) else '--'
            to_print += add + '+'
        to_print += '\n'
        # if the node has None to the right or below, print a boundary, otherwise leave it open
        for y in range(len(self.grid)):
            right_borders = '|' if (self.grid[y][0].left is False) else ' '
            bottom_borders = "+"
            for x in range(len(self.grid[y])):
                # uncomment if you want to make each cell display it's name.
                # will require some changes to other code
                # middle = str(self.grid[y][x].loc).center(5)
                middle = '  '
                if ((y, x) == self.start_node):
                    middle = 'St'
                elif ((y,x) == self.player.loc):
                    middle = 'Pl'
                elif ((y, x) == self.end_node):
                    middle = 'En'

                right_borders += middle
                # check the right
                if (self.grid[y][x].right is False):
                    right_borders += '|'
                else:
                    right_borders += ' '

                # check the down
                if (self.grid[y][x].down is False):
                    bottom_borders += '--+'
                else:
                    bottom_borders += '  +'
            to_print += right_borders + '\n'
            to_print += bottom_borders + '\n'
        return to_print.strip()

    @staticmethod
    def create_grid(height, width):
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(Node(x, y))
        return grid

    def reset_board(self):
        self.player = self.start_node
        self.grid = Board.create_grid(self.height, self.width)

    def move_player(self, direction):
        move_to_x = self.player[0] + direction[0]
        move_to_y = self.player[1] + direction[1]
        if (self.can_move(direction)):
            self.player = (move_to_x, move_to_y)

    def can_move(self, direction):
        can_move = {
            Board.NORTH: self.grid[self.player[1]][self.player[0]].up,
            Board.SOUTH: self.grid[self.player[1]][self.player[0]].down,
            Board.EAST: self.grid[self.player[1]][self.player[0]].right,
            Board.WEST: self.grid[self.player[1]][self.player[0]].left,
        }
        return can_move.get(direction, False)

    def player_reached_goal(self):
        return self.player == self.end_node



if __name__ == '__main__':
    b = Board()
    print(b)
