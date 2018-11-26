# CubeAI
CSCI-B 351 final project with the goal of making an AI to solve a 2x2 cube and possibly scaling up to higher order cubes.

# Documentation:
## Project structure
```
├── gui                     # Folder conaining GUI files
    ├── cubeSpin.py         # Template script to demonstrate how to draw and rotate a cube in 3D
    ├── main_gui.py         # Main file that creates the gui
    └── ThreeD_Cube.py      # 3D nxn cube model that moves
├── AIs.py                  # Python script with different AI algorithms for solving the cube
├── beginnersmethod.py      # ''unfinished'' simple solving method
├── Cube.py                 # The class which models the cube
├── debug.py                # Tools to debug unsuccessful solves
├── Heuristic.py            # Heuristics for solving the cube
├── main.py                 # The main python script which runs all others and serves as the entry point
├── project files           # Files needed to submit this project such as proposals and formal documentation
└── unused                  # Contains currently unused files
```

## Cube.py
This file contains the Cube class which is used to represent and manipulate the Rubik's cube in software.  The class is written to create a cube for any ordered cube n.  The cube is represented by a 2-dimensional matrix of size 6x(nxn).  The first index is the face of the cube with the following mapping: 0->front, 1->up, 2->right, 3->down, 4->left, 5->back.  The script also contains a base 94 encoding for the hash method but it is not currently used.

```
Dependencies: math, random
```

**class Cube**: class to represent the cube
```
    num_moves
    size
    state
    moves

    # constructor takes n for size of cube
    __init__(n=2, hash=None)

    # isSolved returns bool value of if state
    # is a solved state or not
    isSolved()

    # scramble takes a length and returns list of moves
    # in the scramble, scramble won't turn the same layer
    # or opposite layers sequentially
    scramble(length)

    @staticmethod
    opposite(i)

    # turnFront rotates the front layer of the cube
    # pi/2 clockwise, it takes n which is which
    # front layer to rotate, 0 being the face
    # and 1, etc for higher order cubes
    turnFront(n)

    # turns top layer
    turnUp(n)

    # turns right layer
    turnRight(n)

    # turns down layer
    turnDown(n)

    # turns left layer
    turnLeft(n)

    # turns back layer
    turnBack(n)

    # makeMove takes a move which is a tuple of the slice
    # to turn and how many times to turn it
    makeMove(move)

    # asRows takes int of which face to transform
    # and returns the face (in self.state) indexed
    # but as a 2d array representing the n rows
    # from left to right
    asRows(i)

    # asColumns takes int of which face to transform
    # and returns the face (in self.state) indexed
    # but as a 2d array representing the n columns
    # from left to right.  This is done in a similar
    # fashion to asRows
    asColumns(i)

    # colToFace takes a 2d array of collums and turns it into a face
    # as to easily be put back into state
    colToFace(cols)

    # rowToFace takes a 2d array of rows and turns it into a face
    # as to easily be put back into state
    rowToFace(rows)

    # reverse is a simple function that takes a list
    # and returns it in reverse order
    @staticmethod
    reverse(l)

    # this uses the row and column methods with reverse to
    # rotate the face pi/2 clockwise at index i
    rotate(i)

    # rotate layers rotates a list in a circular way
    # this will be used to rotate the rows/cols around
    # the cube
    @staticmethod
    rotateLayers(l)

    # printMap prints the self.state to console
    printMap(self)

    children(self,depth=None)

    __copy__()

    __hash__()

    decode(hash)
```

**class Base94Encoding**: encode an integer as a string that saves space
```
    start_index: the ascii starting character to use for the string
    encoding_length: the length of the encoding used

    Just creates class
    __init__()

    Given an integer this method returns a base96 (encoding_length) representation of that number in ascii form
        num = the base 10  integer to be encoded (changed base)
        returns: the encoded (base 96) number as a string
    encode(num)

    Given an encoded string in base96 ascii this method returns the base10 integer
            encoding = the base96 encoded number
            returns: the decoded base10 integer
    decode(encoding)
```

