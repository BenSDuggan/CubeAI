from Cube import*
from gui.main_gui import *

class Debug:
    cube = Cube(2)
    move_list = []
    def __init__(self):
        pass

    @staticmethod
    def view(hash):
        if hash == None:
            return
        m = Cube(2)
        m.state = Cube.decode(hash)
        g = GUI(cube=m, player=True, width=800, height=600)

        while True:
            g.update()

    @staticmethod
    def reset(cube=Cube(2)):
        Debug.cube = cube
        Debug.move_list = [((None,None),cube.__hash__())]

    @staticmethod
    def addMove(move):
        Debug.move_list.append(move)

    @staticmethod
    def viewMoves():
        g = GUI(cube=Debug.cube, width=800, height=600)
        g.moveList(Debug.move_list)

        while True:
            g.update()

if __name__ == '__main__':
    hash = None
    print("Enter the hash: ")
    Debug.view(int(input()))

    pass

    # Initial setup debug
    c = Cube(2)
    c.makeMove((1,1))
    c.makeMove((2,1))
    Debug.reset(c)

    # Add moves
    c.makeMove((2,3))
    Debug.addMove(((2,3), c.__hash__()))
    c.makeMove((1,3))
    Debug.addMove(((1,3), c.__hash__()))

    Debug.viewMoves()

