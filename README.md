# CubeAI
CSCI-B 351 final project with the goal of making an AI to solve a 2x2 cube and possibly scaling up to higher order cubes.  The AI algorithms used are BFS, Better BFS (limit moves), A\*, IDA\*, and Mini (a minimizing version of MiniMax).  There are 3 heuristics implimented: simpleHeuristic, hammingDistance and manhattanDistance.  There is a GUI which shows a 2D and 3D cube inaddition to the move states and allows for people to try to solve the cube in an easy way.

# How to run:
First make sure you have pygames installed by running `pip install pygames`.  The simplest way to run the code is by running `python main.py`.  To view the command line arguments type `python main.py -h`.  This will show the help page which is shown below:
```
CubeAI
CSCI-B 351 final project with the goal of making an AI to solve a 2x2 cube and possibly scaling up to higher order cubes.
The AI algorithms used are BFS, Better BFS (limit moves), A*, IDA*, and Mini (a minimizing version of MiniMax).
There are 3 heuristics implimented: simpleHeuristic, hammingDistance and manhattanDistance. 

optional arguments:
  -h, --help  show this help message and exit
  --m False   Run manually (start gui) or run the AI first
  --n 2       The dimension of the cube (nxn)
  --s 5       How many times to scramble the cube
  --a ida*    Which AI algorithm to use: (bfs), (bbfs), (a*), (ida*), (mini)
  --h m       Which heuristic to use: (s)impleHeuristic, (h)ammingDistance, (m)anhattanDistance.
```


# Example images:
![3D 2x2 GUI](/docs/3d_2x2.png)
3D 2X2 cube in GUI
![2D 2x2 GUI](/docs/2d_2x2.png)
2D 2x2 cube in GUI

# Documentation:
## Project structure
```
├── main.py                 # The main python script which runs all others and serves as the entry point
├── main_gui.py             # Main file that creates the gui
├── AIs.py                  # Python script with different AI algorithms for solving the cube
├── Heuristic.py            # Heuristics for solving the cube
├── Cube.py                 # The class which models the cube and methods to manipulate it
├── ManhattanCube.py        # Class used to represent the cube differently for the Manhattan Distance heuristic
├── tests.py                # Script used to generate test data CSVs found in the tests folder
├── project_files           # Files needed to submit this project such as proposals and formal documentation
├── tests                   # Folder containing the raw CSV test data for different AI algorithms and heuristics
└── unused                  # Contains currently unused and old files
```

## main.py
This is the main file that gets ran.  It can start the gui and allow humans to solve the cube or have different AIs solve the cube and show the results on the GUI.  The simplest way to run the code is by running `python main.py`.  The console will then walk you through the options.  Additionally you can use command line arguments.  The first argument is the size of the cube n (nxn), then the scramble length, next the AI algorithm (bfs, bbfs, a\*, ida\*, mini) and finally the heuristic ((s)impleHeuristic, (h)ammingDistance, (m)anhattanCube).

```
Dependencies: time, main_gui, AIs, Heuristic
```
```
# Start the gui
# n = the size of the cube
# scramble_length = how many scrambles should be made
gui(n, scramble_length)


# Run the specified AI algorithm and start the GUI to show the results
# type = a string specifying which AI algorithm to run
# n = size of the cube
# scramble_length = how many scrambles should be made
# heuristic = The Heuristic object reference that should be used by an applicable AI
ai(type, n, scramble_length, heuristic)
```

## main_gui.py
This script handels all of the GUI work.  To start a new GUI instance you must call GUI() and pass it a cube object.  GUI has both 2D and 3D models for any nxn cube and can track the moves or make it easy to see the path an AI returned.

```
Dependencies: sys, math, pygame, time, operator, copy, Cube
```
**class GUI**: The main class used to render the data to the screen and handels user inputs and switching between 3D and 2D objects
```
# Creates a gui instance given a cube.  The width, height and wheather or not to use threeD can also be specified
# cube = cube instance to make a gui of
# width = 800 = the width of the screen
# height = 600 = the height of the screen
# threeD = True = a boolean indeicating if the GUI should open in 3D mode
__init__(cube, width=8--, height=600, threeD=True)

# Update and render the GUI using user input, must be called continuously
update()

# Draws the 2D cube to the screen
draw2DCube()

# Draws 3D cube to the screen
# vertices = verticies that result from the ThreeD_Cube
# faces = faces that result from the ThreeD_Cube
# colors = colors that result from the ThreeD_Cube
draw3DCube(vertices, faces, colors)

# Renderes the text box to the screen and all text.  Also handels word wrapping
renderText(self)

# Takes an AI path and lets users easily travers over this path
# path = the path returned from the AI algorithms
moveList(path)
```
**class Point3D**: Makes a point in 3 dimentions.  Used to draw the 3D cube.  This class was taken entirely from http://codeNtronix.com and developed by Leonel Machava <leonelmachava@gmail.com>
```
# Creates a point
# x = 0 = x cord
# y = 0 = y cord
# z = 0 = z cord
__init__(x = 0, y = 0, z = 0)

# Rotates the point around the X axis by the given angle in degrees. 
# angle = the angle the point should be rotated
rotateX(angle)

# Rotates the point around the Y axis by the given angle in degrees. 
# angle = the angle the point should be rotated
rotateY(angle)

# Rotates the point around the Z axis by the given angle in degrees. 
# angle = the angle the point should be rotated
rotateZ(angle)

# Transforms this 3D point to 2D using a perspective projection. 
# win_width = window width
# win_height = window height
# fow = field of view
# viewer_distance = how far away is the viewer
project(win_width, win_height, fov, viewer_distance)

__hash__()

__str__()
```
**class ThreeD_Cube**: Class that creates rectangles and moves the 3D cube
```
vertices = []
faces = []
colors = []

__init__()

# Methhod that takes in a cube state and colors and generates all of the 3DPoints needed to draw them to the screen
# cube = cube.state to be rendered
# color_bank = the color bank desired for each face
update(cube, color_bank)
```

## AIs.py
```
Dependencies: heapq, time, Cube, Heuristic
```
All of the algorithms are classes that get initialized with cube objects and then return the path to the correct answer by running the solve method.  The path is an array of tuples with the first index being the move made to get from the previous state to the current state and the second index being the current state.  A sample path would look something like this:
```
path = [(None, cube_1), ((0,1), cube_2), ((1,3), cube_goal)]
```

**class BFS**: Runs BFS algorithm
```
# cube = Cube object to run BFS on
__init__(cube)

# timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
# return path from initial cube state to solved state
solve(timeout=float('inf'))
```

**class BBFS**: Runs Better BFS algorithm
```
# cube = Cube object to run BBFS on
__init__(cube)

# timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
# return path from initial cube state to solved state
solve(timeout=float('inf'))
```

**class A\***: Runs A* algorithm
```
# cube = Cube object to run A* on
# heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
__init__(cube, heuristic=Heuristic.manhattanDistance)

# timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
# return path from initial cube state to solved state
solve(timeout=float('inf'))

# Find the path using State() given that A* has found the goal_state
# start_state = the initial State()
# end_state = the State() that contains the goal cube
# return the standard path output
find_path(start_state, end_state)
```

**class Bidirectional_A_star**: Not implimented.  Don't grade.

**class IDA\***: Runs IDA* algorithm
```
# cube = Cube object to run IDA* on
# heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
__init__(cube, heuristic=Heuristic.manhattanDistance)

# timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
# return path from initial cube state to solved state
solve(timeout=float('inf'))

# Perform iterative deepening operation
# path = Current path
# g = current depth
# bound = what the fValue can't exced
# times=(float('inf'),0) = a tuple with first index equal to the timeout and second index equal to the duration of the test
# return the minium value which is a tuple of solved, path, and fValue
search(path, g, bound, times=(float('inf'),0))
```

**class Mini**: Runs Mini algorithm.  MiniMax but mini only
```
# cube = Cube object to run Mini on
# heuristic = Heuristic.manhattanDistance = Which Heuristic from Heuristic to run
__init__(cube, heuristic=Heuristic.manhattanDistance)

# depth = 2 = How deep to look before making a move
# timeout = float('inf') = How long the algorithm should run for before throughing a timeout error
# return path from initial cube state to solved state
solve(depth=2, timeout=float('inf'))

# Runs the mini alg on the current cube
# cube = the cube to run the alg on
# depth = how dep to look
# times=(float('inf'),0) = a tuple with first index equal to the timeout and second index equal to the duration of the test
# retrun a tuple of the best_move and best_score
mini(cube, depth, times=(float('inf'),0))
```

**class State**: Stores the state of the cube, parent cube and other information used by A*
```
# current_state = current cube state
# parent_state = the parent cube state
# fValue = the fValue of the current state
# depth = the number of moves from the initial state to current_state
# move = the move to get from parent_state to current_state
__init__(current_state, parent_state, fValue, depth, move)

# checks if two States are the same
__eq__(other)

# checks if the fValue of this board is less than the fValue of another board
__lt__(other)

__bool__()

__hash__()

__str__()
```


## Heuristic.py
```
Dependencies: Cube, ManhattanCube
```
**class Heuristic**: class used to run the 3 heuristics implimented.  All of the heuristics return a smaller value for a better state
```
# Simple heuristic that gives a higher score for the more similar colors on a face
# state = a Cube object
# return the heuristic value
@staticmethod
simpleHeuristic(state)

# Heuristic that calculates the hamming distance of the cube in comparison to the goal state
# cube = a Cube object
# return the heuristic value
@staticmethod
hammingDistance(cube)

# Heuristic that calculates the 3D Manhattand Distance of the cube by calling myHeuristic.scoreCube(cube)
# cube = a Cube object
# return the heuristic value
@staticmethod
manhattanDistance(cube)
```
**class myHeuristic**: Class used to calculate the 3d Manhattan Distance of the cube


## Cube.py
This file contains the Cube class which is used to represent and manipulate the Rubik's cube in software.  The class is written to create a cube for any ordered cube n.  The cube is represented by a 2-dimensional matrix of size 6x(nxn).  The first index is the face of the cube with the following mapping: 0->front, 1->up, 2->right, 3->down, 4->left, 5->back.  The script also contains a base 94 encoding for the hash method but it is not currently used.

```
Dependencies: math, random, copy, ManhattanCube
```

**class Cube**: class to represent the cube
```
    size = n sized cube (nxn)
    state = 6xnxn array that holds the color in each cube face
    moves = possible move indexes

    # constructor takes n for size of cube
    __init__(n=2, hash=None)

    # isSolved returns bool value of if state
    # is a solved state or not
    isSolved()

    # trueScramble is the final version of scramble, it takes an
    # int which is the length of scramble and returns a list of 
    # moves (represented as tuples) which is the scramble.
    # trueScramble only scrambles using moves right front and up,
    # and will never have two consecutive moves on the same face
    def trueScramble(length):

    # obviousSolution takes a scramble and returns the reverse of that solution
    # most of the time this is not the shortest solution, but we can be positive this
    # is a solution.  
    @staticmethod
    obviousSolution(scramble)

    # translateMove simply takes a move (tuple)
    # and returns that move's representation in standard
    # rubik's cube notation
    @staticmethod
    translateMove(move)

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

    # Generate all childrent states from the current
    # depth: a string that says how many children to explore: None=front,up,right,down,left,back; 2x=front,up,right all 1,2,prime; prime=front,up,right,down,left,back, 1,prime, all=front,up,right,down,left,back 1,2,prime
    # Return an array of tuples with the first index being the move and second being a new Cube class
    children(self,depth=None)

    # Copy current cube and return a new instance of it
    __copy__()

    # Return a hash of the cube state (base 6 encoding with 10 digits)
    __hash__()

    # base 6 encoding with 10 digits
    @staticmethod
    encode(state)

    # decode an encoded state array
    @staticmethod
    decode(hash)
```

## ManhattanCube.py
Class ManhattanCube that makes a cube of all corner pieces to be used with Manhattan Heuristic
```
Dependencies: Cube
```
**class ManhattanCube**: class to represent by pieces instead of faces
```
# Makes the Manhattan Cube given a Cube
# map = the Cube
__init__(map)

# given the cublet id returns that cublet's index in cube
# id = the cublet id
# return the cubelet
findPiece(id)

# Get the orientation of the cube
# a the cubelet
# return the cubelet orientation
cublet(a)
```

## tests.py
```
Dependencies: time, csv, Cube, AIs, Heuristic
```
This file is used to test the algorithm and generate statistical data.  Change the variable values in the main if to set the cube size, scramble length and other options.  It is ran by simply typing `python tests.py`

