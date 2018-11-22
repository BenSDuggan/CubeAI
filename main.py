'''
    Team 4 - Ben Duggan & Connor Altic
    11/4/18
    Class with main gui class
'''

from gui import *

def gui():
    m = Map(2)
    g = GUI(map=m, player=True, width=800, height=600)

    g.scramble(10, 0.3)

    while True:
        g.update()

def ai():
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("using argv")
        if sys.argv[0] == 'gui':
            print("using GUI")
            gui()
        else:
            print("using AI")
            ai()
    else:
        gui()