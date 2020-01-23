from maze.mazedata.board import Board, BoardSizeException
from maze.mazedata.node import Node


def main():
    try:
        test = Board(Node)
        print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
