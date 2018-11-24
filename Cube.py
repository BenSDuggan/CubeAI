'''
    Team 4 - Ben Duggan & Connor Altic
    11/3/18
    Class with main gui class
'''

import base64, math, random

class Cube:
    # constructor takes n for size of cube
    def __init__(self, n=2, hash=None):
        self.num_moves = 0
        self.size = n
        self.state = [[],[],[],[],[],[]]
        for i in range(6):
            for j in range(n*n):
                self.state[i].append(i)
        if n % 2 == 0:
            self.moves = (3 * n) - 1
        elif n % 2 == 1:
            self.moves = (3 * (n - 1)) - 1

    # isSolved returns bool value of if state
    # is a solved state or not
    def isSolved(self):
        for i in range(6):
            for j in range((self.size * self.size) - 1):
                if self.state[i][j] != self.state[i][j + 1]:
                    return False
        return True

    # scramble takes a length and returns list of moves
    # in the scramble, scramble won't turn the same layer
    # or opposite layers sequentially
    def scramble(self, length):
        moves = []
        for i in range(length):
            move = (random.randint(0, 5), random.randint(1, 3))
            while i >= 1 and (moves[i - 1][0] == move[0] or move[0] == self.opposite(moves[i - 1][0])):
                move = (random.randint(0, 5), random.randint(1, 3))
            moves.append(move)
            self.makeMove(move)

    @staticmethod
    def opposite(i):
        if i == 0:
            return 5
        if i == 1:
            return 3
        if i == 2:
            return 4
        if i == 3:
            return 1
        if i == 4:
            return 2
        if i == 5:
            return 0

    # turnFront rotates the front layer of the cube
    # pi/2 clockwise, it takes n which is which
    # front layer to rotate, 0 being the face
    # and 1, etc for higher order cubes
    def turnFront(self, n):
        assert n <= self.size/2
        rotation = [self.asRows(1)[self.size - n - 1], self.asColumns(2)[n], self.asRows(3)[n], self.asColumns(4)[self.size - 1 - n]]
        self.rotateLayers(rotation)
        # repair Up
        temp = self.asRows(1)
        temp[self.size - 1 - n] = self.reverse(rotation[0])
        self.state[1] = self.rowToFace(temp)
        # repair Right
        temp = self.asColumns(2)
        temp[n] = rotation[1]
        self.state[2] = self.colToFace(temp)
        # repair Down
        temp = self.asRows(3)
        temp[n] = self.reverse(rotation[2])
        self.state[3] = self.rowToFace(temp)
        # repair Left
        temp = self.asColumns(4)
        temp[self.size - 1 - n] = rotation[3]
        self.state[4] = self.colToFace(temp)

        # if the outer layer is turned, rotate the face
        if n == 0:
            self.rotate(0)

    # turns top layer
    def turnUp(self, n):
        assert n <= self.size/2
        rotation = [self.asRows(0)[n], self.asRows(4)[n], self.asRows(5)[self.size - n - 1], self.asRows(2)[n]]
        self.rotateLayers(rotation)
        # repair front
        temp = self.asRows(0)
        temp[n] = rotation[0]
        self.state[0] = self.rowToFace(temp)
        # repair left
        temp = self.asRows(4)
        temp[n] = rotation[1]
        self.state[4] = self.rowToFace(temp)
        # repair back
        temp = self.asRows(5)
        temp[self.size - 1 - n] = self.reverse(rotation[2])
        self.state[5] = self.rowToFace(temp)
        # repair right
        temp = self.asRows(2)
        temp[n] = self.reverse(rotation[3])
        self.state[2] = self.rowToFace(temp)

        # rotate outer layer
        if n == 0:
            self.rotate(1)
    # turns right layer
    def turnRight(self, n):
        assert n <= self.size/2
        rotation = [self.asColumns(0)[self.size - 1 - n], self.asColumns(1)[self.size - n - 1], self.asColumns(5)[self.size - n - 1], self.asColumns(3)[self.size - n - 1]]
        self.rotateLayers(rotation)
        # repair front
        temp = self.asColumns(0)
        temp[self.size - 1 - n] = rotation[0]
        self.state[0] = self.colToFace(temp)
        # repair up
        temp = self.asColumns(1)
        temp[self.size - 1 - n] = rotation[1]
        self.state[1] = self.colToFace(temp)
        # repair back
        temp = self.asColumns(5)
        temp[self.size - 1 - n] = rotation[2]
        self.state[5] = self.colToFace(temp)
        # repair down
        temp = self.asColumns(3)
        temp[self.size - 1 - n] = rotation[3]
        self.state[3] = self.colToFace(temp)

        # rotate outer layer
        if n == 0:
            self.rotate(2)

    # turns down layer
    def turnDown(self, n):
        assert n <= self.size/2
        rotation = [self.asRows(0)[self.size - n - 1], self.asRows(2)[self.size - n - 1], self.asRows(5)[n], self.asRows(4)[self.size - n - 1]]
        self.rotateLayers(rotation)
        # repair front
        temp = self.asRows(0)
        temp[self.size - 1 - n] = rotation[0]
        self.state[0] = self.rowToFace(temp)
        # repair right
        temp = self.asRows(2)
        temp[self.size - 1 - n] = rotation[1]
        self.state[2] = self.rowToFace(temp)
        # repair back
        temp = self.asRows(5)
        temp[n] = self.reverse(rotation[2])
        self.state[5] = self.rowToFace(temp)
        # repair left
        temp = self.asRows(4)
        temp[self.size - 1 - n] = self.reverse(rotation[3])
        self.state[4] = self.rowToFace(temp)

        # rotate face
        if n == 0:
            self.rotate(3)

    # turns left layer
    def turnLeft(self, n):
        assert n <= self.size/2
        rotation = [self.asColumns(0)[n], self.asColumns(3)[n], self.asColumns(5)[n], self.asColumns(1)[n]]
        self.rotateLayers(rotation)
        # repair front
        temp = self.asColumns(0)
        temp[n] = rotation[0]
        self.state[0] = self.colToFace(temp)
        # repair down
        temp = self.asColumns(3)
        temp[n] = rotation[1]
        self.state[3] = self.colToFace(temp)
        # repair back
        temp = self.asColumns(5)
        temp[n] = rotation[2]
        self.state[5] = self.colToFace(temp)
        # repair up
        temp = self.asColumns(1)
        temp[n] = rotation[3]
        self.state[1] = self.colToFace(temp)
        # rotate face
        if n == 0:
            self.rotate(4)

    # turns back layer
    def turnBack(self, n):
        assert n <= self.size/2
        rotation = [self.asRows(1)[n], self.asColumns(4)[n], self.asRows(3)[self.size - n - 1], self.asColumns(2)[self.size - n - 1]]
        self.rotateLayers(rotation)
        # repair up
        temp = self.asRows(1)
        temp[n] = self.reverse(rotation[0])
        self.state[1] = self.rowToFace(temp)
        # repair left
        temp = self.asColumns(4)
        temp[n] = rotation[1]
        self.state[4] = self.colToFace(temp)
        # repair down
        temp = self.asRows(3)
        temp[self.size - 1 - n] = self.reverse(rotation[2])
        self.state[3] = self.rowToFace(temp)
        # repair right
        temp = self.asColumns(2)
        temp[self.size - 1 - n] = rotation[3]
        self.state[2] = self.colToFace(temp)
        # rotate face
        if n == 0:
            self.rotate(5)

    # makeMove takes a move which is a tuple of the slice
    # to turn and how many times to turn it
    def makeMove(self, move):
        self.num_moves += 1
        for i in range(move[1]):
            if move[0] % 6 == 0:
                self.turnFront(int(move[0]/6))
            if move[0] % 6 == 1:
                self.turnUp(int((move[0] - 1)/6))
            if move[0] % 6 == 2:
                self.turnRight(int((move[0] - 2)/6))
            if move[0] % 6 == 3:
                self.turnDown(int((move[0] - 3)/6))
            if move[0] % 6 == 4:
                self.turnLeft(int((move[0] - 4) / 6))
            if move[0] % 6 == 5:
                self.turnBack(int((move[0] - 5) / 6))
        return self


    # asRows takes int of which face to transform
    # and returns the face (in self.state) indexed
    # but as a 2d array representing the n rows
    # from left to right
    def asRows(self, i):
        rows = []
        for j in range(self.size):
            row = []
            for f in range((self.size * j),(self.size * (j + 1))):
                row.append(self.state[i][f])
            rows.append(row)
        return rows

    # asColumns takes int of which face to transform
    # and returns the face (in self.state) indexed
    # but as a 2d array representing the n columns
    # from left to right.  This is done in a similar
    # fashion to asRows
    def asColumns(self, i):
        cols = []
        for j in range(self.size):
            col = []
            for f in range(self.size):
                col.append(self.state[i][(f * self.size) + j])
            cols.append(col)
        return cols

    # colToFace takes a 2d array of collums and turns it into a face
    # as to easily be put back into state
    def colToFace(self,cols):
        l = []
        for i in range(self.size):
            for j in range(self.size):
                l.append(cols[j][i])
        return l

    # rowToFace takes a 2d array of rows and turns it into a face
    # as to easily be put back into state
    def rowToFace(self, rows):
        l = []
        for i in range(self.size):
            for j in range(self.size):
                l.append(rows[i][j])
        return l

    # reverse is a simple function that takes a list
    # and returns it in reverse order
    @staticmethod
    def reverse(l):
        j = []
        for i in range(len(l)):
            j.append(l[len(l) - i - 1])
        return j
    # this uses the row and column methods with reverse to
    # rotate the face pi/2 clockwise at index i
    def rotate(self, i):
        self.state[i] = self.colToFace(self.reverse(self.asRows(i)))

    # rotate layers rotates a list in a circular way
    # this will be used to rotate the rows/cols around
    # the cube
    @staticmethod
    def rotateLayers(l):
        temp = l[0]
        l[0] = l[3]
        l[3] = l[2]
        l[2] = l[1]
        l[1] = temp
        return l

    # printMap prints the self.state to console
    def printMap(self):
        for i in range(6):
            if i == 0:
                print("0 ~ Front")
            if i == 1:
                print("1 ~ Up")
            if i == 2:
                print("2 ~ Right")
            if i == 3:
                print("3 ~ Down")
            if i == 4:
                print("4 ~ Left")
            if i == 5:
                print("5 ~ Back")
            rows = self.asRows(i)
            for j in rows:
                print(j)

    def children(self,depth=None):
        children = []
        for i in range(self.moves):
            children.append(self.__copy__().makeMove((i,1)))
            if depth == 'all' or depth == 'prime':
                children.append(self.__copy__().makeMove((i,3)))
            if depth == 'all' or depth == 'double':
                children.append(self.__copy__().makeMove((i,2)))
        return children

    def __copy__(self):
        m = Cube(self.size)
        m.num_moves = self.num_moves
        m.state = self.state.copy()
        return m

    def __hash__(self):
        hash = 0
        count = 0
        for i in self.state:
            for j in i:
                hash += j*(6**count)
                count += 1
        #return BaseSixEncoding().encode(hash)
        return hash

    def decode(self, hash):
        #hash_10 = BaseSixEncoding().decode(hash)
        hash_10 = hash
        state = [[],[],[],[],[],[]]
        num_face_cublets = math.ceil(math.log(hash_10, 6))//6

        for i in range(6):
            for j in range(num_face_cublets):
                state[i].append(int(hash_10%6))
                hash_10 = int(hash_10//6)
        return state

class BaseSixEncoding:
    def __init__(self):
        self.start_index = 32
        self.encoding_length = 94

    def encode(self, num):
        num = int(num)
        encoded = ""
        while num > 0:
            encoded = chr(self.start_index + int(num%self.encoding_length)) + encoded
            num = int(num//self.encoding_length)
        return encoded

    def decode(self, encoding):
        decoded = int(0)
        count = 0
        while len(encoding) > 0:
            decoded += (ord(encoding[-1])-self.start_index)*int((self.encoding_length**count))
            encoding = encoding[:-1]
            count += 1
        return decoded

if __name__ == '__main__':
    m = Cube(2)
    #m.printMap()

    print(m.children())

    hash = m.__hash__()
    print(hash)
    print(m.decode(hash))

    for i in range(0):
        if i != BaseSixEncoding().decode(BaseSixEncoding().encode(i)):
            print("Error: " + str(i))

'''

Map key:
0 -> Front
1 -> Up
2 -> Right
3 -> Down
4 -> Left
5 -> Back
'''