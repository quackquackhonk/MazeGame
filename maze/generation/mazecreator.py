
class MazeCreator():
    N = (0, -1)
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)

    def __init__(self, board):
        self.board = board
        self.grid = board.grid
        self.startNode = board.startNode
        self.endNode = board.endNode
        self.height = board.height
        self.width = board.width

    def generate(self, seed=None):
        pass
