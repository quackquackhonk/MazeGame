from maze.mazedata.board import Board, BoardSizeException
from maze.generation.growingtree import GrowingTree
from maze.view.app import MazeApp


def main():
    try:
        test = Board(25, 25)
        generate = GrowingTree(test, 25)
        generate.generate()
        run = MazeApp(test)
        run.on_execute()
        # print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
