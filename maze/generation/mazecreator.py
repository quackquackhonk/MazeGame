
class MazeCreator():
    N = (0, -1)
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)

    def __init__(self, board):
        self._board = None
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board
        self.grid = board.grid
        self.startNode = board.startNode
        self.endNode = board.endNode
        self.height = board.height
        self.width = board.width

    def prepareGen(self, seed=None):
        pass

    def complete(self):
        pass

    def step(self):
        pass

    def generate(self, seed=None):
        self.prepareGen(seed)
        while(not self.complete()):
            self.step()
