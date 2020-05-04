from maze.generation.growingtree import GrowingTree
from maze.mazedata.board import Board
from maze.mazedata.constants import *


class GeneticSolver():
    """
    Solves the maze using a genetic algorithm

    self.board: (Board) takes in a pre-made board
    """

    def __init__(self, board):
        self.board = board

    def run():
        mc = GrowingTree(Board(10,10), 50)
        mc.generate(1)
        b = mc.board
        gs = GrowingTree(b, 50)
        gs.board.move_player(SOUTH)
        # gs.board.move_player(SOUTH)
        # gs.board.move_player(WEST)
        # gs.board.move_player(EAST)
        print(gs.board)
