
class Cublet:

    def __init__(self, a):
        cublets = [{1,4,5}, {1,2,5}, {1,0,2}, {1,0,4}, {0,4,3}, {3,0,2}, {3,2,5}, {3,4,5}]
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
