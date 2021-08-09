from Cube import*
class ManhattanCube:

    def __init__(self, map):
        temp = []
        temp.append([map.state[1][3], map.state[4][1], map.state[0][0]])
        temp.append([map.state[1][2], map.state[2][0], map.state[0][1]])
        temp.append([map.state[1][1], map.state[2][1], map.state[5][2]])
        temp.append([map.state[1][0], map.state[4][0], map.state[5][3]])
        temp.append([map.state[3][0], map.state[4][2], map.state[0][3]])
        temp.append([map.state[3][1], map.state[2][3], map.state[0][2]])
        temp.append([map.state[3][2], map.state[2][2], map.state[5][1]])
        temp.append([map.state[3][3], map.state[4][3], map.state[5][0]])

        self.cube = []
        for i in temp:
            self.cube.append(Cublet(i))

    # given the cublet id returns that cublet's index in cube
    def findPiece(self, id):
        for i in range(len(self.cube)):
            if self.cube[i].id == id:
                return i

class Cublet:
    def __init__(self, a):
        cublets = [{1,4,0}, {1,2,0}, {1,2,5}, {1,5,4}, {0,4,3}, {3,0,2}, {3,2,5}, {3,4,5}]
        if a[0] == 1 or a[0] == 3:
            self.ore = 0
        if a[1] == 1 or a[1] == 3:
            self.ore = 1
        if a[2] == 1 or a[2] == 3:
            self.ore = 2
        temp = {a[0], a[1], a[2]}
        for i in range(len(cublets)):
            if temp == cublets[i]:
                self.id = i
                break


if __name__ == '__main__':
    pass