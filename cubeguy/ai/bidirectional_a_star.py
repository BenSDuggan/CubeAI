import heapq
import time

from .. import Cube
from ..State import State
from ..Heuristic import *

class Bidirectional_A_star:
    def __init__(self, cube, heuristic=Heuristic.manhattanDistance):
        self.cube = cube
        self.heuristic = heuristic

    def solve(self, timeout=float('inf')):
        start_time = time.time()
        start_state = State(self.cube, None, 0, 0, None)
        goal_state = State(Cube(self.cube.size), None, 0, 0, None)
        explored = set()
        fringe_i = [start_state]
        heapq.heapify(fringe_i)
        fringe_g = [goal_state]
        heapq.heapify(fringe_g)

        print("starting solve")
        while len(fringe_i) > 0 or len(fringe_g) > 0:
            # Check to see if AI is timed out
            if time.time() - start_time >= timeout:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            # Can we explore fringe_i?
            if len(fringe_i) > 0:
                current_state = heapq.heappop(fringe_i)
                print(current_state)
                if current_state.current_state.isSolved():
                    return self.find_path(start_state, current_state)
                if current_state.__hash__() in explored:
                    continue
                for i in current_state.current_state.children('2x'):
                    if i.__hash__() not in explored:
                        new_addition = State(i[1], current_state, current_state.depth+1+self.heuristic(i[1]), current_state.depth+1, i[0])
                        heapq.heappush(fringe_i, new_addition)
                        explored.add(current_state.__hash__())

            # Can we explore fringe_g
            if len(fringe_g) > 0:
                current_state = heapq.heappop(fringe_g)
                print(current_state)
                if current_state.current_state.isSolved():
                    print('in g')
                    return self.find_path(start_state, current_state)
                if current_state.__hash__() in explored:
                    continue
                for i in current_state.current_state.children('2x'):
                    if i.__hash__() not in explored:
                        new_addition = State(i[1], current_state, current_state.depth+1+self.heuristic(i[1]), current_state.depth+1, i[0])
                        heapq.heappush(fringe_g, new_addition)
                        explored.add(current_state.__hash__())


    def find_path(self, start_state, end_state):
        last_state = end_state
        path = [ [last_state.move, last_state.current_state] ]
        last_state = last_state.parent_state

        while last_state != None and start_state.current_state.__hash__() != path[0][1].__hash__():
            path = [ [last_state.move, last_state.current_state] ] + path
            last_state = last_state.parent_state

        return path
