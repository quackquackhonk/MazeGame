from maze.mazedata.board import Board, BoardSizeException


def main():
    try:
        test = Board()
        print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
