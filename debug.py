from map import*

class debug:

    def __init__(self):
        pass
if __name__ == '__main__':
    m = Map()
    while(True):
        m.printCube()
        move = input('make a move')
        d = (int(move[0]), int(move[1]))
        d = (0,1)
        print(d)
        m.makeMove(d)
