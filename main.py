'''
    Team 4 - Ben Duggan & Connor Altic
    8/17/19
    Class with main gui class
'''

import time, argparse
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

    parser = argparse.ArgumentParser(description='CubeAI\nCSCI-B 351 final project with the goal of making an AI to solve a 2x2 cube and possibly scaling up to higher order cubes.\nThe AI algorithms used are BFS, Better BFS (limit moves), A*, IDA*, and Mini (a minimizing version of MiniMax)\nThere are 3 heuristics implimented: simpleHeuristic, hammingDistance and manhattanDistance.', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--m', metavar='False', default=False, type=bool, action='store', help='Run manually (start gui) or run the AI first')
    parser.add_argument('--n', metavar='2', default=2, type=int, action='store', help='The dimension of the cube (nxn)')
    parser.add_argument('--s', metavar='5', default=5, type=int, action='store', help='How many times to scramble the cube')
    parser.add_argument('--a', metavar='ida*', default='ida*', type=str, action='store', help='Which AI algorithm to use: (bfs), (bbfs), (a*), (ida*), (mini)')
    parser.add_argument('--h', metavar='m', default='m', type=str, action='store', help='Which heuristic to use: (s)impleHeuristic, (h)ammingDistance, (m)anhattanDistance.')

    args = parser.parse_args()

    if args.h == 's':
        heuristic = Heuristic.simpleHeuristic
    elif args.h == 'h':
        heuristic = Heuristic.hammingDistance
    else:
        heuristic = Heuristic.manhattanDistance

    if args.m:
        gui(args.n, args.s)
    else:
        ai(args.a, args.n, args.s, heuristic)
