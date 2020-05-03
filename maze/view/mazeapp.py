import pygame
from pygame.locals import *
from .gamecolors import *
from .player import Player
from maze.generation.mazecreator import MazeCreator
from maze.mazedata.board import Board


class MazeApp:
    BORDER_WIDTH = 2
    CLOCK_TICK = 50

    def __init__(self, board):
        self._running = True
        self._screen = None
        self._generated = False
        self._slowgen = False
        self._maze_alg = MazeCreator(Board())
        self.board = board
        self.player = None
        self.size = (self.screen_height, self.screen_width) = (700, 700)
        self.cell_size = 10
        self.clock = pygame.time.Clock()

    @property
    def maze_alg(self):
        return self._maze_alg

    @maze_alg.setter
    def maze_alg(self, algorithm):
        self._maze_alg = algorithm
        self._maze_alg.board = self.board

    # do all setup work here
    def on_init(self):
        pygame.init()
        # commenting out for now, may need later
        # screenW = pygame.display.Info().current_w
        display_height = pygame.display.Info().current_h
        # screen is a square two-thirds the size of the height of the
        # screen resolution
        # TODO: make screen size a function of the board size
        #       AND the screen resolution
        #       Need support for non-square game boards
        screen_size = int(display_height * (2 / 5))
        self.size = (self.screen_height, self.screen_width) = (screen_size, screen_size)
        self.cell_size = screen_size / self.board.height
        self._screen = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        # initialze variables
        self._generated = False
        self._slowgen = False

        # set initial screen color
        self._screen.fill(WHITE)
        pygame.display.update()

        # create player class
        self.player = Player(self.board.end_node)

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
                if (k == pygame.K_UP):
                    self.player.move((0, -1))
                if (k == pygame.K_DOWN):
                    self.player.move((0, 1))
                if (k == pygame.K_LEFT):
                    self.player.move((-1, 0))
                if (k == pygame.K_RIGHT):
                    self.player.move((1, 0))
            # reset board
            if (k == pygame.K_r and self._generated):
                self.board.reset_board()
                self.maze_alg.board = self.board
                self._generated = False
            # generate board
            if (k == pygame.K_SPACE):
                if (self._maze_alg is not None and self._generated is False):
                    self._maze_alg.generate()
                    self._generated = True
            # stub for slow generation
            if (k == pygame.K_g):
                if (self._maze_alg is not None and self._generated is False):
                    self._maze_alg.prepare_gen()
                    self._slowgen = True

    # run every game tick
    def on_loop(self):
        self._running = not self.player.reached_goal()
        self.clock.tick(MazeApp.CLOCK_TICK)
        # step through
        if (self._slowgen):
            if (not self.maze_alg.complete()):
                self.maze_alg.step()
            # stop slow gen and finish generation
            if (self.maze_alg.complete()):
                self._slowgen = False
                self._generated = True

    # draw the game
    def on_render(self):
        # set background color
        bg = WHITE
        if (self._generated is False):
            bg = GRAY
        self._screen.fill(bg)
        # right = +x, down = +y
        # draw entire game border:
        # top border
        pygame.draw.line(self._screen, BLACK, (0, 0),
                         (self.screen_width, 0), MazeApp.BORDER_WIDTH)
        # left border
        pygame.draw.line(self._screen, BLACK, (0, 0),
                         (0, self.screen_height), MazeApp.BORDER_WIDTH)
        # right border
        pygame.draw.line(self._screen, BLACK, (0, self.screen_height - 1),
                         (self.screen_width - 1, self.screen_height - 1), MazeApp.BORDER_WIDTH)
        # bottom border
        pygame.draw.line(self._screen, BLACK, (self.screen_width - 1, 0),
                         (self.screen_width - 1, self.screen_height - 1), MazeApp.BORDER_WIDTH)

        # draw cells
        for y in range(len(self.board.grid)):
            for x in range(len(self.board.grid[y])):
                top_left = (x * self.cell_size, y * self.cell_size)
                top_right = ((x + 1) * self.cell_size, y * self.cell_size)
                bottom_right = ((x + 1) * self.cell_size,
                                (y + 1) * self.cell_size)
                bottom_left = (x * self.cell_size, (y + 1) * self.cell_size)

                # choose color
                draw_color = GRAY
                if (self._generated is False and self._slowgen is True):
                    if ((x, y) in self._maze_alg.selected_cells):
                        draw_color = LIGHT_RED
                    if ((x, y) in self._maze_alg.visited_cells
                            and not ((x, y) in self._maze_alg.selected_cells)):
                        draw_color = WHITE
                elif (self._generated is True):
                    if ((x, y) == self.board.start_node):
                        draw_color = GREEN
                    elif (((x, y)) == self.board.end_node):
                        draw_color = RED
                    else:
                        draw_color = WHITE

                # fill region
                offset = MazeApp.BORDER_WIDTH
                corner = (x * self.cell_size + offset,
                          y * self.cell_size + offset)
                hw = (self.cell_size - offset,
                      self.cell_size - offset)
                region = pygame.Rect(corner, hw)
                pygame.draw.rect(self._screen, draw_color, region)

                if ((x, y) == self.board.start_node
                        or (x, y) == self.board.end_node):
                    node = self.board.grid[y][x]

                    # re-draw borders
                    if (node.up is False):
                        pygame.draw.line(self._screen, BLACK, top_left,
                                         top_right, MazeApp.BORDER_WIDTH)
                    if (node.left is False):
                        pygame.draw.line(self._screen, BLACK, top_left,
                                         bottom_left, MazeApp.BORDER_WIDTH)
                    if (node.right is False):
                        pygame.draw.line(self._screen, BLACK, top_right,
                                         bottom_right, MazeApp.BORDER_WIDTH)
                    if (node.down is False):
                        pygame.draw.line(self._screen, BLACK, bottom_left,
                                         bottom_right, MazeApp.BORDER_WIDTH)

                # draw the player if generation is finished
                if ((x, y) == self.player.loc and self._generated is True):
                    loc = (int((x + 1 / 2) * self.cell_size),
                           int((y + 1 / 2) * self.cell_size))
                    pygame.draw.circle(self._screen, BLUE,
                                       loc, int(self.cell_size / 3))
                # draw right wall
                if (self.board.grid[y][x].right is False):
                    pygame.draw.line(self._screen, BLACK,
                                     top_right, bottom_right,
                                     MazeApp.BORDER_WIDTH)

                if (self.board.grid[y][x].down is False):
                    pygame.draw.line(self._screen, BLACK, bottom_left,
                                     bottom_right, MazeApp.BORDER_WIDTH)
        pygame.display.update()

    # runs last, do whatever you need to do to reset the game
    def on_cleanup(self):
        if self.player.reached_goal():
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
