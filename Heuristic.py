'''
    Team 4 - Ben Duggan & Connor Altic
    11/26/18
    Class containing heuristics that can be used
'''

from Cube import *
from ManhattanCube import *

class Heuristic:

    @staticmethod
    def simpleHeuristic(state):
        current_state = state.state
        if state.isSolved():
            return 0
        score = 0
        for i in range(6):
            colors = [0,0,0,0,0,0]
            for j in current_state[i]:
                colors[j] += 1
            for l in colors:
                if l == 4:
                    score += 100
                elif l == 3:
                    score += 50
                elif l == 2:
                    score += 25
        return 100*6 - score

    @staticmethod
    def hammingDistance(cube):
        current_state = cube.state
        goal_state = Cube(cube.size).state
        score = 6 * cube.size**2
        for i in range(6):
            for j in range(len(current_state[i])):
                if current_state[i] == goal_state[i]:
                    score -= 1
        return score

    # https://stackoverflow.com/questions/36490073/heuristic-for-rubiks-cube
    @staticmethod
    def manhattanDistance(cube):
        return myHeuristic.scoreCube(cube)

class myHeuristic:
    def __init__(self):
        pass

    @staticmethod
    def scoreCube(this):
        c = ManhattanCube(this)
        score = myHeuristic.scorePiece(c, 0)
        print("~~")
        print(c.cube)
        this.makeMove((1,1))
        this.makeMove((3,3))
        c = ManhattanCube(this)
        score = score + myHeuristic.scorePiece(c, 1)
        this.makeMove((1,1))
        this.makeMove((3,3))
        c = ManhattanCube(this)
        score = score + myHeuristic.scorePiece(c, 2)
        this.makeMove((1,1))
        this.makeMove((3,3))
        score = score + myHeuristic.scorePiece(c, 3)
        this.makeMove((1,1))
        this.makeMove((3,3))
        this.makeMove((4,2))
        this.makeMove((2,2))
        this.makeMove((1,3))
        this.makeMove((3,1))
        c = ManhattanCube(this)
        score = score + myHeuristic.scorePiece(c, 4)
        this.makeMove((1,3))
        this.makeMove((3,1))
        cube = ManhattanCube(this)
        score = score + myHeuristic.scorePiece(c, 5)
        this.makeMove((1,3))
        this.makeMove((3,1))
        c = ManhattanCube(this)
        score = score + myHeuristic.scorePiece(c, 6)
        this.makeMove((1,3))
        this.makeMove((3,1))
        c = ManhattanCube(this)
        return score + myHeuristic.scorePiece(cube,7)

    @staticmethod
    def scorePiece(c, p):
        index = c.findPiece(p)
        case = c.cube[index]
        if case[0] == 0:
            if case[1] == 0:
                return 0
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 2
        if case[0] == 1:
            if case[1] == 0:
                return 1
            if case[1] == 1:
                return 1
            if case[1] == 2:
                return 2
        if case[0] == 2:
            if case[1] == 0:
                return 1
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 2
        if case[0] == 3:
            if case[1] == 0:
                return 1
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 1
        if case[0] == 4:
            if case[1] == 0:
                return 2
            if case[1] == 1:
                return 1
            if case[1] == 2:
                return 1
        if case[0] == 5:
            if case[1] == 0:
                return 2
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 2
        if case[0] == 6:
            if case[1] == 0:
                return 2
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 2
        if case[0] == 7:
            if case[1] == 0:
                return 1
            if case[1] == 1:
                return 2
            if case[1] == 2:
                return 2


# Run python Heuristic.py
if __name__ == '__main__':
    #print(Heuristic.simpleHeuristic())
    cube = Cube(2)
    cube.makeMove((0,1))
    # cube.makeMove((1,1))
    # cube.makeMove((3,3))
    print("Manhattan distance: " + str(Heuristic.manhattanDistance(cube)))
