'''
    Team 4 - Ben Duggan & Connor Altic
    11/3/18
    Class with main gui class
'''

from beginnersmethod import *
from map import *

if __name__ == "__main__":
    print('Testing GUI')

    m = Map()
    m.scramble(10)
    b = beginnersmethod(m)
    b.firstPiece()

    b.secondPiece()
    b.thirdPiece()
    b.fourthPiece()
    print("")
    print(b.log)
    print(len(b.log))
    print(Cube(b.cube).cube[4].id)
    print(Cube(b.cube).cube[4].ore)
    print(Cube(b.cube).cube[5].id)
    print(Cube(b.cube).cube[5].ore)
    print(Cube(b.cube).cube[6].id)
    print(Cube(b.cube).cube[6].ore)
    print(Cube(b.cube).cube[7].id)
    print(Cube(b.cube).cube[7].ore)
    m.printMap()