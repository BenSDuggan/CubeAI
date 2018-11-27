'''
    Team 4 - Ben Duggan & Connor Altic
    11/4/18
    Class with main gui class
'''

from gui.main_gui import *
from AIs import *

def gui(n):
    print('Using manual GUI')

    m = Cube(n)
    g = GUI(cube=m, player=True, width=800, height=600)

    g.scramble(10, 0.3)
    print(m.moves)
    while True:
        g.update()

def ai(type, n):
    if type == 'bfs':
        m = Cube(n)
        m.scramble(10) # Not good with heigh scrambles (>4)
        ai = BFS(m)
        print(ai.solve())
    elif type == 'a*':
        m = Cube(n)
        print(m.simple_scramble(3))
        print('Scramble hash: ' + str(m.__hash__()))
        ai = A_star(m)
        print(ai.solve())
    elif type == 'bia*':
        m = Cube(n)
        m.scramble(12)
        ai = Bidirectional_A_star(m)
        print(ai.solve())
    else:
        print("Not sure what you want")

if __name__ == '__main__':
    x,n = 'a*',2
    if len(sys.argv) > 2:
        x = sys.argv[1]
        n = sys.argv[2]
        print("using argv")
    elif x == None or n == None:
        print("(h)uman | (bfs)")
        x = input()
        print("what n?")
        n = int(input())

    assert type(x) == type('a') and type(n) == type(1)

    if x == 'h':
        gui(n)
    else:
        ai(x, n)
