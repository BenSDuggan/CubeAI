'''
    Team 4 - Ben Duggan & Connor Altic
    11/4/18
    Class with main gui class
'''

import time
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
    elif type == 'ida*':
        m = Cube(n)
        #m.scramble(3)
        m.makeMove((0,3))
        #m.makeMove((2,1))
        ai = IDA_Star(m)
        path = ai.solve()[0]
        for i in path:
            print(i.state)
        '''
        g = GUI(cube=m, width=800, height=600, threeD=False)
        move_list = []
        for i in path:
            move_list.append((i.move, i.current_state.__hash__()))
        g.moveList(move_list)
        while True:
            g.update()
        '''
        #print(ai.solve())
    elif type == 'maxi':
        m = Cube(n)
        print('scramble: ' + str(m.scramble(4)))
        #m.makeMove((0,3))
        #m.makeMove((4,3))
        ai = Maxi(m)
        print('Starting ai:')
        start_time = time.time()
        result = ai.solve(4)
        print('AI took: ' + str(time.time()-start_time) + ' seconds')
        print(result)
    else:
        print("Not sure what you want")

if __name__ == '__main__':
    x,n = 'ida*',2
    if len(sys.argv) > 2:
        x = sys.argv[1]
        n = sys.argv[2]
        print("using argv")
    elif x == None or n == None:
        print("(h)uman | (bfs)")
        x = input()
        print("what n?")
        n = int(input())

    m = Cube(2)
    m.state = m.decode(238544208514371525)
    print('hash: ' + str(Heuristic.hammingDistance(m)))

    assert type(x) == type('a') and type(n) == type(1)

    if x == 'h':
        gui(n)
    else:
        ai(x, n)
