from unused.cube import*
class beginnersMethod:

    def __init__(self, map):
        self.cube = map
        self.moveCount = 0
        self.log = []

    def makeMove(self, move):
        self.log.append(move)
        self.cube.makeMove(move)
        self.moveCount = self.moveCount + 1

    def flipCorner(self,i):
        c = Cube(self.cube)
        while c.cube[4].ore != 0 and c.cube[4].id == i:
            self.makeMove((4,3))
            self.makeMove((1,3))
            self.makeMove((4,1))
            self.makeMove((1,1))
            self.makeMove((4,3))
            self.makeMove((1,3))
            self.makeMove((4,1))
            self.makeMove((1,1))
            c = Cube(self.cube)

    # find and put piece 4 into place
    def firstPiece(self):
        c = Cube(self.cube)
        # if its in the upper layer
        i = c.findPiece(4)
        if i == 4:
            self.flipCorner(4)
            return
        if i < 4:
            if c.cube[0].id == 4:
                self.makeMove((4,2))
            if c.cube[1].id == 4:
                self.makeMove((2,1))
                self.makeMove((3,2))
            if c.cube[2].id == 4:
                self.makeMove((0,2))
            if c.cube[3].id == 4:
                self.makeMove((4,1))
        else:
            if c.cube[5].id == 4:
                self.makeMove((3,3))
            if c.cube[6].id == 4:
                self.makeMove((3,2))
            if c.cube[7].id == 4:
                self.makeMove((3,1))
        self.flipCorner(4)
    def secondPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(5)
        if i > 5:
            if i == 7:
                self.makeMove((5,1))
            self.makeMove((2,1))
        if i < 4:
            while c.cube[2].id != 5:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((2,3))
        self.makeMove((3,3))
        self.flipCorner(5)
        self.makeMove((3,1))
    def thirdPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(6)
        if i == 6:
            pass
        if i == 7:
            self.makeMove((5,1))
        if i < 4:
            while c.cube[1].id != 6:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((5,3))
        self.makeMove((3,2))
        self.flipCorner(6)
        self.makeMove((3,2))
    def fourthPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(7)
        if i < 4:
            while c.cube[0].id != 7:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((4,1))
            self.makeMove((1,1))
            self.makeMove((4,3))
        self.makeMove((3,1))
        self.flipCorner(7)
        self.makeMove((3,3))


if __name__ == '__main__':
    m = Map(2)
    m.scramble(12)







