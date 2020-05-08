from tkinter import Frame, Tk, Canvas

from maze.generation.mazecreator import MazeCreator
from maze.mazedata.board import Board
from maze.mazedata.constants import EAST, NORTH, SOUTH, WEST
from maze.solve.genetic import GeneticSolver

CELL_SIZE = 50  # Cells are rendered as 50x50 squares


"""Module for rendering and controlling the maze application.

This class will handle the main application class that allows the
user to run the maze game.
"""


def launch(width, height):
    """Launch the application.

    Method used to launch the maze application. Handles construction
    of the master for the MazeApp class, as well as dimensions for the
    window and etc.
    """
    root = Tk()
    app = MazeApp(master=root)
    app.pack()
    dimension_string = str(app.board.width * CELL_SIZE)
    dimension_string += "x"
    dimension_string += str(app.board.height * CELL_SIZE)
    root.geometry(dimension_string)
    root.mainloop()


class MazeApp(Frame):
    """Main class for running the Maze game.

    Tkinter Frame used for containing the maze and handling all input
    from the user.

    Attributes:
        master:
        board:
        gen_alg
        solve_alg
    """

    def __init__(self, board=Board(), master=None):
        Frame.__init__(self, master)
        self.master = master
        self.board = board
        self._generated = False
        self._slow_gen = False
        self._gen_alg = MazeCreator(self.board)
        # TODO: Make this a more sane default
        self._solve_alg = GeneticSolver(self.board, 100)
        self.canvas = Canvas(self)

        # create game
        self.initialize()

    @property
    def gen_alg(self):
        """Generation algorithm that the app is using."""
        return self._gen_alg

    @gen_alg.setter
    def gen_alg(self, ga):
        self._gen_alg = ga
        self._gen_alg.board = self.board

    @property
    def solve_alg(self):
        """Algorithm that is used to solve the maze."""
        return self._solve_alg

    @solve_alg.setter
    def solve_alg(self, sa):
        self.solve_alg = sa
        self._solve_alg.board = self.board

    def initialize(self):
        """Initialize the Application window.

        Sets up title, keybindings, board generation, generation
        algorithm and solving algorithm
        """
        self.master.title("Maze Game")

        # Bindings for keyboard control
        # Player control
        self.master.bind('<Up>', lambda e: self.move_event(NORTH))
        self.master.bind('<Down>', lambda e: self.move_event(SOUTH))
        self.master.bind('<Left>', lambda e: self.move_event(WEST))
        self.master.bind('<Right>', lambda e: self.move_event(EAST))
        # Other keybindings
        self.master.bind('r', lambda e: self.board.reset_board())  # Reset
        self.master.bind('q', lambda e: None)  # Quit
        self.master.bind('g', lambda e: None)  # Slow generate
        self.master.bind('<Space>', lambda e: None)  # Quick generate
        self.master.bind('s', lambda e: None)  # Solve

    def render_maze(self):
        """Render the maze

        Draws the maze onto the application canvas based one whatever
        board the game is using right now.
        """
        size = (h, w) = (self.board.height, self.board.width)

        # rendering for if the board has not been generated
        if (_generated is False and _slow_gen is False):
            for y in range(h):
                for x in range(w):
                    break
        pass

    def move_event(self, direction):
        """Moves the player a given direction.

        Args:
            direction (Tuple[Int, Int]): the direction to move
        """
        print(direction)
        return
