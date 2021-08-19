import heapq
import time

from .. import Cube
from ..State import State
from ..Heuristic import *

class A_Star:
    # cube = Cube object to run A* on
    # heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
    def __init__(self, cube, heuristic=Heuristic.manhattanDistance):
        self.cube = cube
        self.heuristic = heuristic

    # timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
    # return path from initial cube state to solved state
    def solve(self, timeout=float('inf')):
        start_time = time.time()
        start_state = State(self.cube, None, 0, 0, None)
        goal_state = State(Cube(self.cube.size), None, 0, 0, None)
        explored = set()
        fringe = [start_state]
        heapq.heapify(fringe)

        print("starting solve")
        while len(fringe) > 0:
            # Check to see if AI is timed out
            if time.time() - start_time >= timeout:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            current_state = heapq.heappop(fringe)
            print(current_state)
            if current_state.current_state.isSolved():
                return self.find_path(start_state, current_state)
            if current_state.__hash__() in explored:
                continue
            for i in current_state.current_state.children('2x'):
                if i.__hash__() not in explored:
                    new_addition = State(i[1], current_state, current_state.depth+1+self.heuristic(i[1]), current_state.depth+1, i[0])
                    heapq.heappush(fringe, new_addition)
                    explored.add(current_state.__hash__())

    # Find the path using State() given that A* has found the goal_state
    # start_state = the initial State()
    # end_state = the State() that contains the goal cube
    # return the standard path output
    def find_path(self, start_state, end_state):
        last_state = end_state
        path = [ [last_state.move, last_state.current_state] ]
        last_state = last_state.parent_state

        while last_state != None and start_state.current_state.__hash__() != path[0][1].__hash__():
            path = [ [last_state.move, last_state.current_state] ] + path
            last_state = last_state.parent_state

        return path