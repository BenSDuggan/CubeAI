'''
    Team 4 - Ben Duggan & Connor Altic
    12/10/18
    Class with main gui class
'''

import sys, math, pygame, time
from operator import itemgetter
from Cube import *
from copy import copy, deepcopy # Needed to copy cube state for 3D cube

# The main class used to render the data to the screen and handels user inputs and switching between 3D and 2D objects
class GUI():
    # Creates a gui instance given a cube.  The width, height and wheather or not to use threeD can also be specified
    # cube = cube instance to make a gui of
    # width = 800 = the width of the screen
    # height = 600 = the height of the screen
    # threeD = True = a boolean indeicating if the GUI should open in 3D mode
    def __init__(self, cube, width=800, height=600, threeD=True):
        self.cube = cube
        self.color_bank = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 255, 0), (255, 165, 0)] #Color of each cube: red, yellow, blue, white, green, orange
        self.background_color = (0,35,0)

        self.state_list = None # Stores path list AI took
        self.move_history = [] # Stores the history of moves made by the user
        self.info_box_text = [[('State list: ', (0,0,0))], [('Move history: ',(0,0,0))], [('Key: ',(0,0,0))]] # Array that holds text rendered at bottom of the screen
        self.info_box_text[2].append(('(F)ront, (U)p, (R)ight, (D)own, (L)eft, (B)ack | (1)+move=prime/reverse, (2)+move=2/180      (V)iew=2D/3D | 3D settings: (A)uto rotation, (M)anual rotation | Left arrow=previous state, Right arrow=next state', (0,0,0))) # Add gui key text

        pygame.init() # start pygame
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        pygame.display.set_caption('CubeAI')

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 15)

        self.frame_rate = 50 # Frame rate of the game
        pygame.time.Clock().tick(self.frame_rate) # Limit frame rate

        # 3D settings
        self.autoRotate = False # Should the cube auto rotate
        self.threeD = threeD # 3D or 2D
        self.threeDCube = ThreeD_Cube()
        self.mouse_center = None
        self.speed = 140 # Limits the influence that the mouse has on the cube movement (higher is slower)
        self.autorotate_speed = 0.8 # speed that the cube will auto rotate (higher is faster)
        self.theta = (0,0)

    # Update and render the GUI using user input, must be called continuously
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            # Key board controls
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                # 3D controls
                # Automatic rotation
                if keys[pygame.K_a]:
                    if self.threeD != None:
                        self.autoRotate = True
                # Manual rotation with mouse
                if keys[pygame.K_m]:
                    if self.threeD != None:
                        self.autoRotate = False
                # Toggle view between 2d and 3d
                if keys[pygame.K_v]:
                    if self.threeD:
                        self.threeD = False
                    else:
                        self.threeD = True

                # Arrow keys
                if keys[pygame.K_RIGHT]:
                    if self.state_list != None and self.state_num < len(self.state_list)-1:
                        self.state_num += 1
                        self.cube.state = self.state_list[self.state_num][1]
                        # Change the info text for state if it's a valid move
                        del self.info_box_text[0][1:]
                        path_str = ''
                        for i in range(1,self.state_num):
                            path_str += str(Cube.translateMove(self.state_list[i][0])) + ', '
                        self.info_box_text[0].append((path_str, (0,0,0)))
                        self.info_box_text[0].append((str(Cube.translateMove(self.state_list[self.state_num][0])), (0,0,255)))
                        path_str = ', '
                        for i in range(self.state_num+1,len(self.state_list)):
                            path_str += str(Cube.translateMove(self.state_list[i][0])) + ', '
                        self.info_box_text[0].append((path_str[:-2], (0,0,0)))
                if keys[pygame.K_LEFT]:
                    if self.state_list != None and self.state_num > 0:
                        self.state_num -= 1
                        self.cube.state = self.state_list[self.state_num][1]
                        # Change the info text for state if it's a valid move
                        del self.info_box_text[0][1:]
                        path_str = ''
                        for i in range(1,self.state_num):
                            path_str += str(Cube.translateMove(self.state_list[i][0])) + ', '
                        self.info_box_text[0].append((path_str, (0,0,0)))
                        path_str = ''
                        if self.state_num > 0:
                            self.info_box_text[0].append((str(Cube.translateMove(self.state_list[self.state_num][0])), (0,0,255)))
                            path_str = ', '
                        for i in range(self.state_num+1,len(self.state_list)):
                            path_str += str(Cube.translateMove(self.state_list[i][0])) + ', '
                        self.info_box_text[0].append((path_str[:-2], (0,0,0)))

                # Prime
                if keys[pygame.K_1]:
                    if keys[pygame.K_f]:
                        self.makeMove((0,3))
                    if keys[pygame.K_u]:
                        self.makeMove((1,3))
                    if keys[pygame.K_r]:
                        self.makeMove((2,3))
                    if keys[pygame.K_d]:
                        self.makeMove((3,3))
                    if keys[pygame.K_l]:
                        self.makeMove((4,3))
                    if keys[pygame.K_b]:
                        self.makeMove((5,3))
                    if keys[pygame.K_x]:
                        self.makeMove((6,3))
                    if keys[pygame.K_y]:
                        self.makeMove((7,3))
                    if keys[pygame.K_z]:
                        self.makeMove((8,3))
                # Move twice
                elif keys[pygame.K_2]:
                    if keys[pygame.K_f]:
                        self.makeMove((0,2))
                    if keys[pygame.K_u]:
                        self.makeMove((1,2))
                    if keys[pygame.K_r]:
                        self.makeMove((2,2))
                    if keys[pygame.K_d]:
                        self.makeMove((3,2))
                    if keys[pygame.K_l]:
                        self.makeMove((4,2))
                    if keys[pygame.K_b]:
                        self.makeMove((5,2))
                    if keys[pygame.K_x]:
                        self.makeMove((6,2))
                    if keys[pygame.K_y]:
                        self.makeMove((7,2))
                    if keys[pygame.K_z]:
                        self.makeMove((8,2))
                else:
                    if keys[pygame.K_f]:
                        self.makeMove((0,1))
                    if keys[pygame.K_u]:
                        self.makeMove((1,1))
                    if keys[pygame.K_r]:
                        self.makeMove((2,1))
                    if keys[pygame.K_d]:
                        self.makeMove((3,1))
                    if keys[pygame.K_l]:
                        self.makeMove((4,1))
                    if keys[pygame.K_b]:
                        self.makeMove((5,1))
                    if keys[pygame.K_x]:
                        self.makeMove((6,1))
                    if keys[pygame.K_y]:
                        self.makeMove((7,1))
                    if keys[pygame.K_z]:
                        self.makeMove((8,1))

        # Check to see if the mouse is clicked to rotate the 3D cube
        if pygame.mouse.get_pressed()[0] and not self.autoRotate:
                if self.mouse_center == None:
                    self.mouse_center = pygame.mouse.get_pos()
                self.theta = (self.theta[0] + (pygame.mouse.get_pos()[0]-self.mouse_center[0])/(self.speed), self.theta[1] + (pygame.mouse.get_pos()[1]-self.mouse_center[1])/(self.speed))

        self.screen.fill(self.background_color) # clear screen
        # Render 3D
        if self.threeD:
            self.threeDCube.update(self.cube.state, self.color_bank)
            self.draw3DCube(self.threeDCube.vertices, self.threeDCube.faces, self.threeDCube.colors)
            self.renderText()
            pygame.display.update()
        # Render 2D
        else:
            self.draw2DCube()
            self.renderText()
            pygame.display.update()

        pygame.time.Clock().tick(self.frame_rate) # Limit frame rate

    # Draws the 2D cube to the screen
    def draw2DCube(self):
        cube = self.cube.state
        #print(cube)
        # Cube size param
        color_bank = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 255, 0), (255, 165, 0)] #Color of each cube: red, yellow, blue, white, green, orange
        offset = (200, 25)
        cubeletSize = 30
        gap = 2
        size = int(math.log(len(cube[0]), 2)) #What demention is used
        faces = [(size*(cubeletSize+gap)+gap, size*(cubeletSize+gap)+gap),
                 (size*(cubeletSize+gap)+gap, 0),
                 (2*(size*(cubeletSize+gap)+gap), size*(cubeletSize+gap)+gap),
                 (size*(cubeletSize+gap)+gap, 2*(size*(cubeletSize+gap)+gap)),
                 (0, size*(cubeletSize+gap)+gap),
                 (size*(cubeletSize+gap)+gap, 3*(size*(cubeletSize+gap)+gap))] #[Color, offset] for each face; indexing is [front, up, right, down, left, back]

        for c in range(len(cube)):
            count = 0
            for i in range(1, size+1):
                for j in range(1, size+1):
                    f = faces[c]
                    pygame.draw.rect(self.screen, color_bank[cube[c][count]], [offset[0]+f[0]+j*(cubeletSize+gap), offset[1]+f[1]+i*(cubeletSize+gap), cubeletSize, cubeletSize])
                    count += 1

    """
     Simulation of a rotating 3D Cube
     Developed by Leonel Machava <leonelmachava@gmail.com>
     
    http://codeNtronix.com
     
    """
    # Draws 3D cube to the screen
    # vertices = verticies that result from the ThreeD_Cube
    # faces = faces that result from the ThreeD_Cube
    # colors = colors that result from the ThreeD_Cube
    def draw3DCube(self, vertices, faces, colors):
        # It will hold transformed vertices.
        t = []

        for v in vertices:
            # Rotate the point around X axis, then around Y axis, and finally around Z axis.
            #r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
            r = v.rotateX(self.theta[1]).rotateY(self.theta[0])
            # Transform the point from 3D to 2D
            p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
            # Put the point in the list of transformed vertices
            t.append(p)

        # Calculate the average Z values of each face.
        avg_z = []
        i = 0
        for f in faces:
            z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
            avg_z.append([i,z])
            i = i + 1

        # Draw the faces using the Painter's algorithm:
        # Distant faces are drawn before the closer ones.
        for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
            face_index = tmp[0]
            f = faces[face_index]
            pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                         (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                         (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                         (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
            try:
                pygame.draw.polygon(self.screen, colors[face_index],pointlist)
            except:
                print(self.colors)
                print(face_index)
                print(faces)
                exit()
            #print(pointlist)

        if self.autoRotate:
            self.theta = (self.theta[0]+self.autorotate_speed, self.theta[1]+self.autorotate_speed)

    # Renderes the text box to the screen and all text.  Also handels word wrapping
    def renderText(self):
        rect = pygame.Rect(0,pygame.display.get_surface().get_size()[1]-100,pygame.display.get_surface().get_size()[0],100)
        pygame.draw.rect(self.screen, (255,255,255), rect)

        lineSpacing = -2
        # get the height of the font
        fontHeight = self.font.size("Tg")[1]

        y = rect.top - fontHeight - lineSpacing

        for i in self.info_box_text:
            x = 0
            y += fontHeight + lineSpacing
            for j in i:
                text = j[0]
                color = j[1]
                while text:
                    i = 1
                    # determine if the row of text will be outside our area
                    if y + fontHeight > rect.bottom:
                        break
                    # determine maximum width of line
                    while self.font.size(text[:i])[0] + x < rect.width and i < len(text):
                        i += 1

                    # if we've wrapped the text, then adjust the wrap to the last word
                    if i < len(text):
                        i = text.rfind(" ", 0, i) + 1

                    image = self.font.render(text[:i], False, color)

                    self.screen.blit(image, (rect.left+x, y))

                    x += self.font.size(text[:i])[0]

                    if x >= rect.width or i < len(text):
                        x = 0
                        y += fontHeight + lineSpacing

                    # remove the text we just blitted
                    text = text[i:]

    # Makes a requested move to the cube and adds the move to the screen
    # move = a touple containing the desired move (face, type)
    def makeMove(self, move):
        self.move_history.append(move)

        self.cube.makeMove(move)
        print('Made move: ' + str(move))

        # Add to move history
        if len(self.info_box_text[1]) >= 3:
            # There is at least 2 moves present
            if len(self.info_box_text[1][1][0]) == 0:
                self.info_box_text[1][1] = (self.info_box_text[1][2][0] + ', ', (0,0,0))
            else:
                self.info_box_text[1][1] = (self.info_box_text[1][1][0] + self.info_box_text[1][2][0] + ', ', (0,0,0))
            self.info_box_text[1][2] = (str(Cube.translateMove(move)), (0,0,255))
        else:
            # This is the first move
            self.info_box_text[1].append(('', (0,0,0)))
            self.info_box_text[1].append((str(Cube.translateMove(move)), (0,0,255)))

    # Takes an AI path and lets users easily travers over this path
    # path = the path returned from the AI algorithms
    def moveList(self, path):
        self.cube.state = path[0][1]
        self.state_list = path
        self.state_num = 0
        path_str = ''
        for i in range(1, len(path)):
            path_str += str(Cube.translateMove(path[i][0])) + ', '

        self.info_box_text[0].append((path_str[:-2], (0,0,0)))

"""
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>
 
http://codeNtronix.com
 
"""
# Makes a point in 3 dimentions.  Used to draw the 3D cube
class Point3D:
    # Creates a point
    # x = 0 = x cord
    # y = 0 = y cord
    # z = 0 = z cord
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    # Rotates the point around the X axis by the given angle in degrees. 
    # angle = the angle the point should be rotated
    def rotateX(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    # Rotates the point around the Y axis by the given angle in degrees. 
    # angle = the angle the point should be rotated
    def rotateY(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    # Rotates the point around the Z axis by the given angle in degrees. 
    # angle = the angle the point should be rotated
    def rotateZ(self, angle):
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    # Transforms this 3D point to 2D using a perspective projection. 
    # win_width = window width
    # win_height = window height
    # fow = field of view
    # viewer_distance = how far away is the viewer
    def project(self, win_width, win_height, fov, viewer_distance):
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

    def __hash__(self):
        return self.x + 10*self.y + 100*self.z

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

# Class that create rectangles and moves the 3D cube
class ThreeD_Cube:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.colors = []

    # Methhod that takes in a cube state and colors and generates all of the 3DPoints needed to draw them to the screen
    # cube = cube.state to be rendered
    # color_bank = the color bank desired for each face
    def update(self, cube, color_bank):
        # clear old cube
        self.vertices = []
        self.faces = []
        self.colors = []
        face_transformations = [[('n',0)],[('x',90)],[('y',270)],[('x',270)],[('y',90)],[('y',180)]] #Front,up,right,down,left,back
        # Need to translate the back state so that it is oriented correctly
        cube = deepcopy(cube)
        back = deepcopy(cube[5])
        for i in range(len(back)):
            cube[5][i] = back[len(back)-i-1]

        size = int(math.log(len(cube[0]), 2)) #What demention is used
        offset = 2/(size)/25 # Distance between cubes
        cube_size = (2 - offset*(size+1))/size

        # Add each square to faces and colors
        for c in range(len(cube)):
            tmp_vertices = []
            p = (-1,1+cube_size,-1) # The original point where we start drawing each square from
            count = 0
            for i in range(0, size):
                p = (-1, p[1]-offset-cube_size, p[2])

                for j in range(0, size):
                    start_index = len(self.vertices) + len(tmp_vertices)
                    tmp_vertices.append(Point3D(p[0],p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+cube_size,p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+cube_size,p[1]-cube_size,p[2]))
                    tmp_vertices.append(Point3D(p[0],p[1]-cube_size,p[2]))
                    self.faces.append((start_index,start_index+1,start_index+2,start_index+3)) # Hold all of the rectangles

                    self.colors.append(color_bank[cube[c][count]]) # Holds the color of the rectangle at the same index in faces

                    p = (p[0]+cube_size+offset, p[1], p[2]) # Update p
                    count += 1

                # Add in a gap between squares (not used)
                if i != size-1 and False:
                    start_index = len(self.vertices) + len(tmp_vertices)
                    tmp_vertices.append(Point3D(p[0],p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+offset,p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+offset,p[1]-offset,p[2]))
                    tmp_vertices.append(Point3D(p[0],p[1]-offset,p[2]))
                    self.faces.append((start_index,start_index+1,start_index+2,start_index+3))
                    self.colors.append((165,165,165))

                    p = (p[0]+offset, p[1], p[2])

            # Transform to correct position
            for i in range(len(tmp_vertices)):
                for j in range(len(face_transformations[c])):
                    if face_transformations[c][j][0]== 'x':
                        self.vertices.append(tmp_vertices[i].rotateX(face_transformations[c][j][1]))
                    elif face_transformations[c][j][0] == 'y':
                        self.vertices.append(tmp_vertices[i].rotateY(face_transformations[c][j][1]))
                    elif face_transformations[c][j][0] == 'z':
                        self.vertices.append(tmp_vertices[i].rotateZ(face_transformations[c][j][1]))
                    else:
                        self.vertices.append(tmp_vertices[i])


if __name__ == "__main__":
    print('Testing GUI')
    m = Cube(2)
    g = GUI(cube=m, width=800, height=600, threeD=True)
    m.makeMove((1,1))

    #g.moveList([(None,[[1, 1, 4, 0], [1, 5, 0, 0], [4, 2, 3, 2], [5, 4, 3, 0], [5, 2, 4, 1], [5, 3, 2, 3]]),((0, 1),[[4, 1, 0, 1], [1, 5, 1, 2], [0, 2, 0, 2], [3, 4, 3, 0], [5, 5, 4, 4], [5, 3, 2, 3]]),((2, 1),[[4, 4, 0, 0], [1, 1, 1, 1], [0, 0, 2, 2], [3, 3, 3, 3], [5, 5, 4, 4], [5, 5, 2, 2]]),((1, 1),[[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]])])

    m.printMap()

    while True:
        g.update()




