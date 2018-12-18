'''
    Team 4 - Ben Duggan & Connor Altic
    12/10/18
    Class with main gui class
'''

import time
from main_gui import *
from AIs import *
from Heuristic import *

# Start the gui
# n = the size of the cube
# scramble_length = how many scrambles should be made
def gui(n, scramble_length):
    print('Using manual GUI')

    m = Cube(n)
    g = GUI(cube=m, width=800, height=600, threeD=True)

    scramble_pattern = m.trueScramble(scramble_length)
    print('Scramble: ' + str(scramble_pattern))
    while True:
        g.update()

# Run the specified AI algorithm and start the GUI to show the results
# type = a string specifying which AI algorithm to run
# n = size of the cube
# scramble_length = how many scrambles should be made
# heuristic = The Heuristic object reference that should be used by an applicable AI
def ai(type, n, scramble_length, heuristic):
    if type == 'bfs':
        m = Cube(n)
        ai = BFS(m)
    elif type == 'bbfs':
        m = Cube(n)
        ai = Better_BFS(m)
    elif type == 'a*':
        m = Cube(n)
        ai = A_Star(m, heuristic)
    elif type == 'ba*':
        print('Not working')
        exit()
        m = Cube(n)
        ai = Bidirectional_A_star(m, heuristic)
    elif type == 'ida*':
        m = Cube(n)
        ai = IDA_Star(m, heuristic)
    elif type == 'mini':
        m = Cube(n)
        ai = Mini(m, heuristic)
    else:
        print("Not sure what you want")

    # Procedures before AI starts to solve cube
    scramble = m.trueScramble(scramble_length)
    print('Scramble moves: ' + str(scramble))
    print('Scramble hash: ' + str(m.__hash__()))
    input('Type enter to continue.')

    # Solve cube
    start_time = time.time() # Start time of algorithm
    path = ai.solve()
    gui_path = [] # Used to store move,state touples
    print('AI took: ' + str(time.time()-start_time) + ' seconds')
    print('Original scramble: ' + str(scramble))
    for i in range(len(path)):
        print('Move #' + str(i+1) + '[ ' + str(Cube.translateMove(path[i][0])) + ', ' + str(path[i][1].state))
        gui_path.append((path[i][0], path[i][1].state))

    # Start GUI showing results
    new_cube = Cube(n)
    g = GUI(cube=new_cube, width=800, height=600, threeD=True)
    g.moveList(gui_path)
    while True:
        g.update()


if __name__ == '__main__':
    # Ask the user what they want to run and run it for them

    #x,n,scramble,heuristic = 'ida*',2,12,Heuristic.manhattanDistance
    x,n,scramble,heuristic = None,None,None,None
    if len(sys.argv) >= 2:
        x = sys.argv[1]
    if len(sys.argv) >= 3:
        n = int(sys.argv[2])
    if len(sys.argv) >= 4:
        scramble = int(sys.argv[3])
    if len(sys.argv) >= 5:
        if sys.argv[4] == 's':
            heuristic = Heuristic.simpleHeuristic
        elif sys.argv[4] == 'h':
            heuristic = Heuristic.hammingDistance
        else:
            heuristic = Heuristic.manhattanDistance
    elif x == None or n == None:
        print("(h)uman (gui) | (bfs), (bbfs), (a*), (ida*), (mini)")
        x = input()
        print("what nxn (just n)?")
        n = int(input())
        print("what scramble length?")
        scramble = int(input())
        print("What heuristic? (s)impleHeuristic, (h)ammingDistance, (m)anhattanDistance")
        h = input()
        if h == 's':
            heuristic = Heuristic.simpleHeuristic
        elif h == 'h':
            heuristic = Heuristic.hammingDistance
        else:
            heuristic = Heuristic.manhattanDistance

    assert type(x) == type('a') and type(n) == type(1) and type(scramble) == type(1)

    if x == 'h':
        gui(n, scramble)
    else:
        ai(x, n, scramble, heuristic)
