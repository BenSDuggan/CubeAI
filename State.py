'''
    Team 4 - Ben Duggan & Connor Altic
    11/26/18
    Creates a state object of a cube
'''

from Cube import *

class State:
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