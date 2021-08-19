'''
First AI tested.  Not an efficient AI as no heuristic is used and there is a large branching factor ~3*n
'''

import time

from ..Cube import Cube

class BFS:
    # cube = Cube object to run BFS on
    def __init__(self, cube):
        self.cube = cube

    # timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
    # return path from initial cube state to solved state
    def solve(self, timeout=float('inf')):
        start_time = time.time()
        goal_state = Cube(self.cube.size).__hash__()
        depth = 0
        if self.cube.__hash__() == goal_state:
            print('Found goal at depth ' + str(depth))
            return [(None, self.cube)]

        # Remembers every state seen and allows us to find the parent state of a cube so we can output the path
        seen = {}
        seen[self.cube.__hash__()] = (self.cube, None, None) #Current cube, parent cube, forbiden moves, move from parent to current
        # The nodes that need to be expanded (the deepest lay)
        fringe = {}
        fringe[self.cube.__hash__()] = (self.cube, None, None) 

        while True:
            # Check to see if AI is timed out
            if time.time() - start_time >= timeout:
                print('time: ' + str(time.time()))
                raise Exception('Code timed out')

            depth += 1
            print('Depth: ' + str(depth) + ', length of fringe: ' + str(len(fringe)) + '; len seen: ' + str(len(seen)))
            print('time: ' + str(time.time()) + '; overlaped time: ' + str(time.time()-start_time))

            new_fringe = {}
            for i in fringe:
                # Check to see if AI is timed out
                if time.time() - start_time >= timeout:
                    print('time: ' + str(time.time()))
                    raise Exception('Code timed out')
                
                for j in fringe[i][0].children('all'):
                    if j[1].__hash__() == goal_state:
                        print('Found goal at depth ' + str(depth))
                        return self.find_path(seen, (j[1], fringe[i][0], j[0], -1))
                    if j[1].__hash__() not in fringe and j[1].__hash__() not in seen:
                        new_fringe[j[1].__hash__()] = (j[1], fringe[i][0], j[0])
                        seen[j[1].__hash__()] = (j[1], fringe[i][0], j[0])
            fringe = new_fringe

    def find_path(self, seen, goal_state):
        last_state = goal_state
        path = [ (last_state[2], last_state[0]) ]
        last_state = seen[last_state[1].__hash__()]

        while last_state != None:
            path = [ (last_state[2], last_state[0]) ] + path
            if last_state[1] == None:
                return path
            last_state = seen[last_state[1].__hash__()]

        return path