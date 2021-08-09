from unused.cube import *

class myHeuristic:
    def __init__(self, c):
        self.state = c

    def scoreCube(self, this):
        cube = cube(this)
        score = self.scorePiece(cube, 0)
        this.makeMove((1,1))
        this.makeMove((3,3))
        cube = cube(this)
        score = score + self.scorePiece(cube, 1)
        this.makeMove((1,1))
        this.makeMove((3,3))
        cube = cube(this)
        score = score + self.scorePiece(cube, 2)
        this.makeMove((1,1))
        this.makeMove((3,3))
        score = score + self.scorePiece(cube, 3)
        this.makeMove((1,1))
        this.makeMove((3,3))
        this.makeMove((4,2))
        this.makeMove((2,2))
        this.makeMove((1,3))
        this.makeMove((3,1))
        cube = cube(this)
        score = score + self.scorePiece(cube, 4)
        this.makeMove((1,3))
        this.makeMove((3,1))
        cube = cube(this)
        score = score + self.scorePiece(cube, 5)
        this.makeMove((1,3))
        this.makeMove((3,1))
        cube = cube(this)
        score = score + self.scorePiece(cube, 6)
        this.makeMove((1,3))
        this.makeMove((3,1))
        cube = cube(this)
        return score + self.scorePiece(cube,7)

    def scorePiece(self, c, p):
        index = c.findPiece(p)
        case = c.cube[index]
        if case.id == 0:
            if case.orr == 0:
                return 0
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 2
        if case.id == 1:
            if case.orr == 0:
                return 1
            if case.orr == 1:
                return 1
            if case.orr == 2:
                return 2
        if case.id == 2:
            if case.orr == 0:
                return 1
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 2
        if case.id == 3:
            if case.orr == 0:
                return 1
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 1
        if case.id == 4:
            if case.orr == 0:
                return 2
            if case.orr == 1:
                return 1
            if case.orr == 2:
                return 1
        if case.id == 5:
            if case.orr == 0:
                return 2
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 2
        if case.id == 6:
            if case.orr == 0:
                return 2
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 2
        if case.id == 7:
            if case.orr == 0:
                return 1
            if case.orr == 1:
                return 2
            if case.orr == 2:
                return 2
