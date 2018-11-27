'''
    Team 4 - Ben Duggan & Connor Altic
    11/26/18
    Class containing heuristics that can be used
'''

from Cube import *

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
    def hammingDistance(state):
        current_state = state.state
        goal_state = Cube(state.size).state
        score = 6 * state.size**2
        for i in range(6):
            for j in range(len(current_state[i])):
                if current_state[i] == goal_state[i]:
                    score -= 1
        return score



if __name__ == '__main__':
    print(Heuristic.simpleHeuristic([]))
