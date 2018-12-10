'''
    Team 4 - Ben Duggan & Connor Altic
    12/4/18
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

def ai(type, n, scramble):
    if type == 'bfs':
        m = Cube(n)
        print('Scramble moves: ' + str(m.trueScramble(scramble)))
        print('Scramble hash: ' + str(m.__hash__()))
        input('Press something to continue.')
        ai = BFS(m)
        start_time = time.time()
        path = ai.solve()
        print('AI took: ' + str(time.time()-start_time) + ' seconds')
        for i in range(len(path)):
            print('Move #' + str(i+1) + '[ ' + str(path[i][0]) + '; ' + str(path[i][1].state))
    elif type == 'bbfs':
        m = Cube(n)
        print('Scramble moves: ' + str(m.simple_scramble(scramble)))
        print('Scramble hash: ' + str(m.__hash__()))
        input('Press something to continue.')
        ai = Better_BFS(m)
        start_time = time.time()
        path = ai.solve()
        print('AI took: ' + str(time.time()-start_time) + ' seconds')
        for i in range(len(path)):
            print('Move #' + str(i+1) + '[ ' + str(path[i][0]) + '; ' + str(path[i][1].state))
    elif type == 'a*':
        m = Cube(n)
        cube_scramble = m.trueScramble(scramble)
        print('Scramble moves: ' + str(cube_scramble))
        print('Scramble hash: ' + str(m.__hash__()))
        input('Press something to continue.')
        ai = A_star(m)
        start_time = time.time()
        path = ai.solve()
        print('Scramble moves: ' + str(cube_scramble))
        print('AI took: ' + str(time.time()-start_time) + ' seconds')
        for i in range(len(path)):
            print('Move #' + str(i+1) + '[ ' + str(path[i][0]) + '; ' + str(path[i][1].state))

    elif type == 'bia*':
        m = Cube(n)
        m.scramble(scramble)
        ai = Bidirectional_A_star(m)
        print(ai.solve())
    elif type == 'ida*':
        m = Cube(n)
        print('Scramble moves: ' + str(m.simple_scramble(scramble)))
        input('Press something to continue.')
        #m.makeMove((0,3))
        #m.makeMove((2,3))
        #m.makeMove((3,3))
        ai = IDA_Star(m)
        start_time = time.time()
        path = ai.solve()[0]
        print('AI took: ' + str(time.time()-start_time) + ' seconds')
        for i in range(len(path)):
            print('Move #' + str(i+1) + '[ ' + str(path[i][0]) + '; ' + str(path[i][1].state))
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
        print('scramble: ' + str(m.scramble(scramble)))
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
    # x,n,scramble = 'ida*',2,4
    # if len(sys.argv) >= 2:
    #     x = sys.argv[1]
    # if len(sys.argv) >= 3:
    #     n = int(sys.argv[2])
    # if len(sys.argv) >= 4:
    #     scramble = int(sys.argv[3])
    # elif x == None or n == None:
    #     print("(h)uman | (bfs)")
    #     x = input()
    #     print("what n?")
    #     n = int(input())

    # assert type(x) == type('a') and type(n) == type(1)

    # if x == 'h':
    #     gui(n)
    # else:
    #     ai(x, n, scramble)
    print('Testing GUI')
    m = Cube(2)

    g = GUI(cube=m, width=800, height=600, threeD=False)

    g.update()

    time.sleep(1)

    #m.makeMove((0,2))

    #g.scramble(10, 0.3)
    m.printMap()

    while True:
        g.update()
