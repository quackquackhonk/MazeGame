import pygame
from pygame.locals import *
from .gamecolors import *
from .player import Player


class MazeApp:

    BORDER_WIDTH = 2

    def __init__(self, board):
        self._running = True
        self._screen = None
        self._generated = False
        self._slowgen = False
        self._mazeAlg = None
        self.board = board
        self.startNode = board.startNode
        self.player = None
        self.endNode = board.endNode
        self.size = (self.sw, self.sh) = (700, 700)
        self.cellSize = 10

    @property
    def mazeAlg(self):
        return self._mazeAlg

    @mazeAlg.setter
    def mazeAlg(self, a):
        self._mazeAlg = a

    # do all setup work here
    def on_init(self):
        pygame.init()
        # commenting out for now, may need later
        # screenW = pygame.display.Info().current_w
        screenH = pygame.display.Info().current_h
        # screen is a square two-thirds the size of the height of the screen resolution
        # TODO: make screen size a function of the board size AND the screen resolution
        #       Need support for non-square game boards
        screenSize = int(screenH * (2 / 5))
        self.size = (self.sw, self.sh) = (screenSize, screenSize)
        self.cellSize = screenSize / self.board.height
        self._screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        # create clock
        self.clock = pygame.time.Clock()

        # set initial screen color
        self._screen.fill(white)
        pygame.display.update()

        # create player class
        self.player = Player(self.endNode)

        # start the game
        self._running = True

    # control flow
    def on_event(self, event):
        loc = self.player.loc
        if (event.type == pygame.QUIT):
            self._running = False

        # key presses
        if (event.type == pygame.KEYDOWN):
            k = event.key
            # move player only if maze gen is complete
            if (self._generated):
                if (k == pygame.K_UP and self.board.grid[loc[1]][loc[0]].up is not False):
                    self.player.move((0, -1))
                if (k == pygame.K_DOWN and self.board.grid[loc[1]][loc[0]].down is not False):
                    self.player.move((0, 1))
                if (k == pygame.K_LEFT and self.board.grid[loc[1]][loc[0]].left is not False):
                    self.player.move((-1, 0))
                if (k == pygame.K_RIGHT and self.board.grid[loc[1]][loc[0]].right is not False):
                    self.player.move((1, 0))
            # reset board
            if (k == pygame.K_r and self._generated):
                self.player.loc = self.startNode
                self.board.resetBoard()
                self.mazeAlg.board = self.board
                self._generated = False
            # generate board
            if (k == pygame.K_SPACE):
                if (self.mazeAlg is not None and self._generated is False):
                    self.mazeAlg.generate()
                    self._generated = True
            # stub for slow generation
            if (k == pygame.K_g):
                if (self.mazeAlg is not None and self._generated is False):
                    self.mazeAlg.prepareGen()
                    self._slowgen = True

    # run every game tick
    def on_loop(self):
        self._running = not self.player.reachedGoal()
        self.clock.tick(20)
        # step through
        if (self._slowgen):
            if (not self.mazeAlg.complete()):
                self.mazeAlg.step()
            # stop slow gen and finish generation
            if (self.mazeAlg.complete()):
                self._slowgen = False
                self._generated = True

    # draw the game
    def on_render(self):
        self._screen.fill(white)
        # right = +x, down = +y
        # draw entire game border:
        pygame.draw.line(self._screen, black, (0, 0),
                         (self.sw, 0), MazeApp.BORDER_WIDTH)  # top border
        pygame.draw.line(self._screen, black, (0, 0),
                         (0, self.sh), MazeApp.BORDER_WIDTH)  # left border
        pygame.draw.line(self._screen, black, (0, self.sh - 1),
                         (self.sw - 1, self.sh - 1), MazeApp.BORDER_WIDTH)  # right border
        pygame.draw.line(self._screen, black, (self.sw - 1, 0),
                         (self.sw - 1, self.sh - 1), MazeApp.BORDER_WIDTH)  # bottom border
        # draw cells
        for y in range(len(self.board.grid)):
            for x in range(len(self.board.grid[y])):
                topLeft = (x * self.cellSize, y * self.cellSize)
                topRight = ((x + 1) * self.cellSize, y * self.cellSize)
                bottomRight = ((x + 1) * self.cellSize,
                               (y + 1) * self.cellSize)
                bottomLeft = (x * self.cellSize, (y + 1) * self.cellSize)

                if ((x, y) == self.startNode or (x, y) == self.endNode):
                    node = self.board.grid[y][x]
                    # choose color
                    drawColor = green if ((x, y) == self.startNode) else red

                    # fill region
                    region = pygame.Rect(
                        topLeft, (self.cellSize, self.cellSize))
                    pygame.draw.rect(self._screen, drawColor, region)

                    # re-draw borders
                    if (node.up is False):
                        pygame.draw.line(self._screen, black, topLeft,
                                         topRight, MazeApp.BORDER_WIDTH)
                    if (node.left is False):
                        pygame.draw.line(self._screen, black, topLeft,
                                         bottomLeft, MazeApp.BORDER_WIDTH)
                    if (node.right is False):
                        pygame.draw.line(self._screen, black, topRight,
                                         bottomRight, MazeApp.BORDER_WIDTH)
                    if (node.down is False):
                        pygame.draw.line(self._screen, black, bottomLeft,
                                         bottomRight, MazeApp.BORDER_WIDTH)

                # draw the player
                if ((x, y) == self.player.loc):
                    loc = (int((x + 1 / 2) * self.cellSize),
                           int((y + 1 / 2) * self.cellSize))
                    pygame.draw.circle(self._screen, blue,
                                       loc, int(self.cellSize / 3))
                # draw right wall
                if (self.board.grid[y][x].right is False):
                    pygame.draw.line(self._screen, black,
                                     topRight, bottomRight, MazeApp.BORDER_WIDTH)

                if (self.board.grid[y][x].down is False):
                    pygame.draw.line(self._screen, black, bottomLeft,
                                     bottomRight, MazeApp.BORDER_WIDTH)
                pass

        pygame.display.update()

    # runs last, do whatever you need to do to reset the game
    def on_cleanup(self):
        if self.player.reachedGoal():
            print("You did it!")
        pygame.quit()

    # call this function to start the game
    def on_execute(self):
        if (self.on_init() is False):
            self._running = False

        while(self._running):
            self.on_loop()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
