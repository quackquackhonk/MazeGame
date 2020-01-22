from maze.data.board import Board
from maze.data.board import BoardSizeException
from maze.data.node import Node


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
