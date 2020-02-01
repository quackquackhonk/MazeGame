from maze.mazedata.board import Board, BoardSizeException
from maze.generation.growingtree import GrowingTree
from maze.view.mazeapp import MazeApp


def main():
    try:
        test = Board(15, 15)
        generate = GrowingTree(test, 25)
        # generate.generate(10)
        run = MazeApp(test)
        run.mazeAlg = generate
        run.on_execute()
        # while (not generate.complete()):
        #     s = input("step")
        #     generate.step()
        #     print(test)
        # print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
