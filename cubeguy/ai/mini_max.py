import time

from .. import Cube
from ..Heuristic import *

# Run Mini (MiniMax but mini)
class Mini:
    # cube = Cube object to run Mini on
    # heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
    def __init__(self, cube, heuristic=Heuristic.manhattanDistance):
        self.cube = cube
        self.heuristic = heuristic

    # depth = 2 = How deep to look before making a move
    # timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
    # return path from initial cube state to solved state
    def solve(self, depth=2, timeout=float('inf')):
        start_time = time.time()
        path = []
        while True:
            # Check to see if AI is timed out
            if time.time() - start_time >= timeout:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            move = self.mini(self.cube, depth, (timeout, start_time))
            print('Making move: ' + str(move[0]) + ' with score of ' + str(move[1]))
            self.cube.makeMove(move[0])
            path.append((move[0], self.cube))
            if self.cube.isSolved():
                return path

    # Runs the mini alg on the current cube
    # cube = the cube to run the alg on
    # depth = how dep to look
    # times=(float('inf'),0) = a tuple with first index equal to the timeout and second index equal to the duration of the test
    # retrun a tuple of the best_move and best_score
    def mini(self, cube, depth, times=(float('inf'),0)):
        if cube.isSolved():
            return None, -100 * (depth+1)

        if depth == 0:
            return None, self.heuristic(cube)

        # Check to see if AI is timed out
        if time.time() - times[1] >= times[0]:
            print('time: ' + str(time.time()))
            raise Exception('Code timed out')

        best_move = None
        best_score = None

        for move in cube.children('2x'):
            score = self.mini(move[1], depth-1)[1]

            print("depth:", str(depth), "; score:", score, '; move:', str(move[0]), '; cube: ', str(move[1].__hash__()), '; heuristic: ', str(self.heuristic(move[1])))

            if best_move is None or score < best_score:
                best_score = score
                best_move = move[0]

        return best_move, best_score