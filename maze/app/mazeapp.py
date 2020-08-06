from tkinter import Frame, Tk, Canvas

from maze.generation.mazecreator import MazeCreator
from maze.mazedata.board import Board
from maze.mazedata.constants import EAST, NORTH, SOUTH, WEST
from maze.solve.genetic import GeneticSolver
import random

CELL_SIZE = 50  # Cells are rendered as 50x50 squares
BORDER_SIZE = 15


"""Module for rendering and controlling the maze application.

This class will handle the main application class that allows the
user to run the maze game.
"""


def launch(board=Board()):
    """Launch the application.

    Method used to launch the maze application. Handles construction
    of the master for the MazeApp class, as well as dimensions for the
    window and etc.
    """
    root = Tk()
    app = MazeApp(board, master=root)

    b_w = board.width
    b_h = board.height

    ds = []
    ds.append(str(b_w * CELL_SIZE + b_w * BORDER_SIZE))
    ds.append("x")
    ds.append(str(b_h * CELL_SIZE + b_h * BORDER_SIZE))
    dimension_string = ''.join(ds)
    root.geometry(dimension_string)

    app.pack()
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

    def __init__(self, board, master=None):
        Frame.__init__(self, master)
        b_w = board.width
        b_h = board.height
        f_height = b_h * CELL_SIZE + b_h * BORDER_SIZE
        f_width = b_w * CELL_SIZE + b_w * BORDER_SIZE
        self.master = master
        self.board = board
        self._generated = False
        self._slow_gen = False
        self._gen_alg = MazeCreator(self.board)
        # TODO: Make this a more sane default
        self._solve_alg = GeneticSolver(self.board, 100)
        self.canvas = Canvas(self, width=f_width,
                             height=f_height)

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
        # self.master.bind('q', lambda e: None)  # Quit
        # self.master.bind('g', lambda e: None)  # Slow generate
        # self.master.bind('<Space>', lambda e: None)  # Quick generate
        # self.master.bind('s', lambda e: None)  # Solve

        self.render_maze()


    def render_maze(self):
        """Render the maze

        Draws the maze onto the application canvas based one whatever
        board the game is using right now.
        """
        # pass
        (h, w) = (self.board.height * CELL_SIZE + self.board.height * BORDER_SIZE,
                  self.board.width * CELL_SIZE + self.board.width * BORDER_SIZE)

        def choose_color():
            colors = ["red", "black", "blue"]
            return random.choice(colors)

        # Create borders
        self.canvas.create_rectangle(0, 0, w, h, width=BORDER_SIZE)

        # rendering for if the board has not been generated
        if (self._generated is False and self._slow_gen is False):
            for y, row in enumerate(self.board.grid):
                for x, cell in enumerate(row):
                    y_c = y * CELL_SIZE
                    x_c = x * CELL_SIZE
                    border_offset_x = x * BORDER_SIZE + BORDER_SIZE
                    border_offset_y = y * BORDER_SIZE + BORDER_SIZE
                    self.canvas.create_rectangle(x_c + border_offset_x,
                                                 y_c + border_offset_y,
                                                 x_c + border_offset_x + CELL_SIZE,
                                                 y_c + border_offset_y + CELL_SIZE,
                                                 fill=choose_color())

        self.canvas.pack()


    def move_event(self, direction):
        """Moves the player a given direction.

        Args:
            direction (Tuple[Int, Int]): the direction to move
        """
        print(direction)
        pass
