class MazeCreator():
    def __init__(self, board):
        self.selected_cells = []
        self.visited_cells = []
        self._board = None
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board
        self.grid = board.grid
        self.start_node = board.start_node
        self.end_node = board.end_node
        self.height = board.height
        self.width = board.width

    def prepare_gen(self, seed=None):
        pass

    def complete(self):
        pass

    def step(self):
        pass

    def generate(self, seed=None):
        self.prepare_gen(seed)
        while(not self.complete()):
            self.step()
