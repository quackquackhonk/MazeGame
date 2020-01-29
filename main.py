from maze.mazedata.board import Board, BoardSizeException
from maze.generation.growingtree import GrowingTree


def main():
    try:
        test = Board(10, 10)
        generate = GrowingTree(test, 10)
        generate.generate(20)
        print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
