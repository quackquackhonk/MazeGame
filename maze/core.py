from Board import *


def run():
    try:
        test = Board()
        print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)
    except Exception as e:
        print(e)
