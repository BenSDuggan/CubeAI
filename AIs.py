'''
    Team 4 - Ben Duggan & Connor Altic
    12/4/18
    Class that contains all of the AIs used
'''

import heapq
from Cube import *
from Heuristic import *
from State import *

'''
First AI tested.  Not an efficient AI as no heuristic is used and there is a large branching factor ~3*n
'''
class BFS:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        goal_state = Cube(self.cube.size).__hash__()
        depth = 0
        if self.cube.__hash__() == goal_state:
            print('Found goal at depth ' + str(depth))
            return 'yes'

        seen = set()
        seen.add(self.cube.__hash__())
        fringe = {}
        fringe[self.cube.__hash__()] = self.cube

        while True:
            depth += 1
            print(depth)
            new_fringe = {}
            for i in fringe:
                children = fringe[i].children('prime')
                for j in children:
                    if j[1].__hash__() == goal_state:
                        print('Found goal at depth ' + str(depth))
                        return 'yes'
                    if j[1].__hash__() not in fringe and j[1].__hash__() not in seen:
                        new_fringe[j[1].__hash__()] = j[1]
                        seen.add(j[1].__hash__())
            fringe = new_fringe
            print(len(fringe))

class A_star:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        start_state = State(self.cube, None, 0, 0, None)
        goal_state = State(Cube(self.cube.size), None, 0, 0, None)
        explored = set()
        fringe = [start_state]
        heapq.heapify(fringe)

        print("starting solve")
        while len(fringe) > 0:
            current_state = heapq.heappop(fringe)
            print(current_state)
            if current_state.current_state.isSolved():
                return self.find_path(start_state, current_state)
            if current_state.__hash__() in explored:
                continue
            for i in current_state.current_state.children('2x'):
                if i.__hash__() not in explored:
                    new_addition = State(i[1], current_state, current_state.depth+1+Heuristic.simpleHeuristic(i[1]), current_state.depth+1, i[0])
                    heapq.heappush(fringe, new_addition)
                    explored.add(current_state.__hash__())

    def find_path(self, start_state, end_state):
        last_state = end_state
        path = [ [last_state.move, last_state.current_state] ]
        last_state = last_state.parent_state

        while last_state != None and start_state.current_state.__hash__() != path[0][1].__hash__():
            path = [ [last_state.move, last_state.current_state] ] + path
            last_state = last_state.parent_state

        return path

class Bidirectional_A_star:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        pass

class IDA_Star:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        bound = Heuristic.hammingDistance(self.cube)
        path = [(None, self.cube)] #(move, cube)
        while True:
            print('Path len: ' + str(len(path)) + '; bound: ' + str(bound) + '; path head: (' + str(path[-1][0]) + ', ' + str(path[-1][1].state) + ')')

            t = self.search(path, 0, bound)
            if t[0]:
                return (path, bound)
            if t[2] == float('inf'):
                return [], None
            path.append(t[1][len(path)])
            bound = t[2]
            print(path)

    def search(self, path, g, bound):
        node = path[-1][1]
        f = g + Heuristic.hammingDistance(node)
        if f > bound:
            return False, path, f
        print('')
        if node.isSolved():
            return True, path, f
        min = False, path, float('inf')
        for succ in node.children('all'):
            if succ[1] not in path:
                path.append(succ)
                t = self.search(path, g+1, bound)
                if t[0]:
                    return t
                if t[2] < min[2]:
                    min = t[0], path, t[2]
                del path[-1]
        return min

class Maxi:
    def __init__(self, cube):
        self.cube = cube

    def solve(self, depth=2):
        path = []
        while True:
            move = self.maxi(self.cube, depth)
            print('Making move: ' + str(move[0]) + ' with score of ' + str(move[1]))
            self.cube.makeMove(move[0])
            path.append(move)
            if self.cube.isSolved():
                return path

    def maxi(self, cube, depth):
        if cube.isSolved():
            return None, -100 * (depth+1)

        if depth == 0:
            return None, Heuristic.hammingDistance(cube)

        best_move = None
        best_score = None

        for move in cube.children('all'):
            score = self.maxi(move[1], depth-1)[1]

            print("depth:", str(depth), "; score:", score, '; move:', str(move[0]), '; cube: ', str(move[1].__hash__()), '; heuristic: ', str(Heuristic.hammingDistance(move[1])))

            if best_move is None or score < best_score:
                best_score = score
                best_move = move[0]

        return best_move, best_score
