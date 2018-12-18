'''
    Team 4 - Ben Duggan & Connor Altic
    12/4/18
    Class that contains all of the AIs used
'''

import heapq, time
from Cube import *
from Heuristic import *

'''
First AI tested.  Not an efficient AI as no heuristic is used and there is a large branching factor ~3*n
'''
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

class Better_BFS:
    # cube = Cube object to run BBFS on
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
        seen[self.cube.__hash__()] = (self.cube, None, None, -1) #Current cube, parent cube, forbiden moves, move from parent to current
        # The nodes that need to be expanded (the deepest lay)
        fringe = {}
        fringe[self.cube.__hash__()] = (self.cube, None, None, -1) 

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

                for j in fringe[i][0].children('2x'):
                    if j[1].__hash__() == goal_state:
                        print('Found goal at depth ' + str(depth))
                        return self.find_path(seen, (j[1], fringe[i][0], j[0], -1))
                    if j[0][0] == fringe[i][3]:
                        continue
                    if j[1].__hash__() not in fringe and j[1].__hash__() not in seen:
                        new_fringe[j[1].__hash__()] = (j[1], fringe[i][0], j[0], j[0][0])
                        seen[j[1].__hash__()] = (j[1], fringe[i][0], j[0], j[0][0])
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

# Not used
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

# Object used by A* and to keep track of state, previous state and other items
class State:
    # current_state = current cube state
    # parent_state = the parent cube state
    # fValue = the fValue of the current state
    # depth = the number of moves from the initial state to current_state
    # move = the move to get from parent_state to current_state
    def __init__(self, current_state, parent_state, fValue, depth, move):
        self.current_state = current_state
        self.parent_state = parent_state
        self.fValue = fValue
        self.depth = depth
        self.move = move

    # checks if two States are the same
    def __eq__(self, other):
        if self.current_state == other:
            return True
        return False

    # checks if the fValue of this board is less than the fValue of another board
    def __lt__(self, other):
        return self.fValue < other.fValue

    def __bool__(self):
        return True

    def __hash__(self):
        return self.current_state.__hash__()

    def __str__(self):
        return "depth:" + str(self.depth) + "; fValue:" + str(self.fValue) + "; current_state:" + str(self.current_state.__hash__()) + '; move:' + str(self.move) + '; solved:' + str(self.current_state.isSolved())