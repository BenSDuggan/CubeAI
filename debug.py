from Cube import*
from gui.main_gui import *

class Debug:
    def __init__(self):
        pass

    @staticmethod
    def view(hash):
        m = Cube(2)
        m.state = Cube.decode(hash)
        g = GUI(cube=m, player=True, width=800, height=600)

        while True:
            g.update()

if __name__ == '__main__':
    hash = None
    print("Enter the hash: ")
    x = input()
    hash = int(x)
    Debug.view(hash)
