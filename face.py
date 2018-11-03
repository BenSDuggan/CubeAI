class Face:

    def __init__(self, l):
        self.layout = l

    def printFace(self):
        for i in self.asRows(self.layout):
            print(i)

    def asCollums(self, l):
        return [[l[0],l[3]],[l[1],l[2]]]

    def asRows(self, l):
        return [[l[0],l[1]],[l[3],l[2]]]

    def colToFace(self,l):
        self.layout = [l[0][0], l[1][0], l[1][1], l[0][1]]

    def rowToFace(self, l):
        self.layout = [l[0][0],l[0][1],l[1][1],l[1][0]]

    def swap(self, l):
        temp = l[0]
        l[0] = l[1]
        l[1] = temp
        return l

    def rotateClockwise(self):
        temp = self.layout[0]
        self.layout[0] = self.layout[3]
        self.layout[3] = self.layout[2]
        self.layout[2] = self.layout[1]
        self.layout[1] = temp
        return self.layout

    def rotateCounterClockwise(self):
        temp = self.layout[0]
        self.layout[0] = self.layout[1]
        self.layout[1] = self.layout[2]
        self.layout[2] = self.layout[3]
        self.layout[3] = temp

if __name__ == '__main__':
    pass


