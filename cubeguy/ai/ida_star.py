import time

from .. import Cube
from .. import ManhattanCube
from ..State import State
from ..Heuristic import *

class IDA_Star:
    # cube = Cube object to run IDA* on
    # heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
    def __init__(self, cube, heuristic=Heuristic.manhattanDistance):
        self.cube = cube
        self.heuristic = heuristic

    # timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
    # return path from initial cube state to solved state
    def solve(self, timeout=float('inf')):
        start_time = time.time()
        bound = self.heuristic(self.cube)
        path = [(None, self.cube)] #(move, cube)
        while True:
            # Check to see if AI is timed out
            if time.time() - start_time >= timeout:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            print('Path len: ' + str(len(path)) + '; bound: ' + str(bound) + '; path head: (' + str(path[-1][0]) + ', ' + str(path[-1][1].state) + ')')

            t = self.search(path, 0, bound)
            if t[0]:
                return path
            if t[2] == float('inf'):
                return []

            if t[0]:
                path.append(t[1][len(path)])
            bound = t[2]

    # Perform iterative deepening operation
    # path = Current path
    # g = current depth
    # bound = what the fValue can't exced
    # times=(float('inf'),0) = a tuple with first index equal to the timeout and second index equal to the duration of the test
    # return the minium value which is a tuple of solved, path, and fValue
    def search(self, path, g, bound, times=(float('inf'),0)):
        node = path[-1][1]
        f = g + self.heuristic(node)
        if f > bound:
            return False, path, f
        if node.isSolved():
            return True, path, f
        min_val = False, path, float('inf')
        for succ in node.children('2x'):
            # Check to see if AI is timed out
            if time.time() - times[1] >= times[0]:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            if succ[1] not in path:
                path.append(succ)
                t = self.search(path, g+1, bound)
                if t[0]:
                    return t
                if t[2] < min_val[2]:
                    min_val = t[0], path, t[2]
                del path[-1]
        return min_val
