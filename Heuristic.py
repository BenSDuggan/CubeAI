'''
    Team 4 - Ben Duggan & Connor Altic
    11/26/18
    Class containing heuristics that can be used
'''

from Cube import *
from ManhattanCube import *

class Heuristic:
    # Simple heuristic that gives a higher score for the more similar colors on a face
    # state = a Cube object
    # return the heuristic value
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
        return 1200 - score

    # Heuristic that calculates the hamming distance of the cube in comparison to the goal state
    # cube = a Cube object
    # return the heuristic value
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

    # Heuristic that calculates the 3D Manhattan Distance of the cube by calling myHeuristic.scoreCube(cube)
    # cube = a Cube object
    # return the heuristic value
    @staticmethod
    def manhattanDistance(cube):
        return myHeuristic.scoreCube(cube)

# Class used to calculate the 3d Manhattan Distance of the cube
class myHeuristic:
    def __init__(self):
        pass

    @staticmethod
    def scoreCube(this):
        cube = ManhattanCube(this)
        simple = Heuristic.simpleHeuristic(this)
        score = 0
        for i in range(6):
            score = score + myHeuristic.scorePiece(cube, i)
        return (float(score) / 4) + simple/1200

    @staticmethod
    def scorePiece(c, p):
        index = c.findPiece(p)
        if p == 0:
            if index == 0:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 1:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 2:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 3:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
            if index == 4:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
            if index == 5:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 6:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
        if p == 1:
            if index == 0:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 1:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 2:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
            if index == 3:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
            if index == 6:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
        if p == 2:
            if index == 0:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 1:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
            if index == 2:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 3:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 6:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
        if p == 3:
            if index == 0:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
            if index == 1:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 2:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 3:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 6:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
        if p == 4:
            if index == 0:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
            if index == 1:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 2:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 3:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 6:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
        if p == 5:
            if index == 0:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 1:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
            if index == 2:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 3:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 6:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
        if p == 6:
            if index == 0:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 1:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 2:
                if c.ore[index] == 0:
                    return 2
                if c.ore[index] == 1:
                    return 1
                if c.ore[index] == 2:
                    return 1
            if index == 3:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 4:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2
            if index == 5:
                if c.ore[index] == 0:
                    return 1
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 1
            if index == 6:
                if c.ore[index] == 0:
                    return 0
                if c.ore[index] == 1:
                    return 2
                if c.ore[index] == 2:
                    return 2



# Run python Heuristic.py
if __name__ == '__main__':
    cube = Cube(2)
    print(cube.trueScramble(6))