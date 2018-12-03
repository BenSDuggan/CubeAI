'''
    Team 4 - Ben Duggan & Connor Altic
    11/22/18
    PyGame class to make a 3D Rubik's cube
'''

"""
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>
 
http://codeNtronix.com
 
"""
import sys, math, pygame, time
from operator import itemgetter
from Cube import *

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

    def __hash__(self):
        return self.x + 10*self.y + 100*self.z

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        self.window = (win_width, win_height)
        self.center = (self.window[0]/2, self.window[1]/2)
        self.mouse_center = None
        self.speed = 35
        self.theta = (0,0)
        self.autoRotate = False

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Simulation of a rotating 3D Cube (http://codeNtronix.com)")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1),

            Point3D(-1,-1,2),
            Point3D(0,-1,2),
            Point3D(0,1,2),
            Point3D(-1,1,2),
        ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7), (8,9,10,11),(12,13,14,15)]

        # Define colors for each face
        self.colors = [(255,0,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0), (0,255,255), (255,255,255)]

        self.angle = 0

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_m]:
                        self.autoRotate = False
                    if pygame.key.get_pressed()[pygame.K_a]:
                        self.autoRotate = True

            if pygame.mouse.get_pressed()[0] and not self.autoRotate:
                if self.mouse_center == None:
                    self.mouse_center = pygame.mouse.get_pos()
                self.theta = (self.theta[0] + (pygame.mouse.get_pos()[0]-self.mouse_center[0])/(self.speed), self.theta[1] + (pygame.mouse.get_pos()[1]-self.mouse_center[1])/(self.speed))

            self.clock.tick(50)
            self.screen.fill((0,32,0))

            self.draw()

            if __name__ != '__main__':
                break

    def draw(self):
        # It will hold transformed vertices.
        t = []

        for v in self.vertices:
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
        for f in self.faces:
            z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
            avg_z.append([i,z])
            i = i + 1

        # Draw the faces using the Painter's algorithm:
        # Distant faces are drawn before the closer ones.
        for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
            face_index = tmp[0]
            f = self.faces[face_index]
            pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                         (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                         (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                         (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
            pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)
            #print(pointlist)

        if self.autoRotate:
            self.theta = (self.theta[0]+1, self.theta[1]+1)

        #pygame.display.flip()


class ThreeD_Cube:
    def __init__(self, screen):
        self.vertices = []
        self.faces = []
        self.colors = []
        self.s = Simulation()

    def test(self, cube):
        self.update(cube,[(255, 0, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 165, 0)])
        self.s.vertices = self.vertices
        self.s.faces = self.faces
        self.s.colors = self.colors
        self.s.run()

    def draw(self):
        self.s.vertices = self.vertices
        self.s.faces = self.faces
        self.s.colors = self.colors
        self.s.run()

    '''
    Methhod that takes in a screen, map and colors and draws them on the screen given
    '''
    def update(self, cube, color_bank):
        #self.vertices = [Point3D(-1,1,-1),Point3D(1,1,-1),Point3D(1,-1,-1),Point3D(-1,-1,-1),Point3D(-1,1,1),Point3D(1,1,1),Point3D(1,-1,1),Point3D(-1,-1,1)]
        #self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)] # Define the vertices that compose each of the 6 faces. These numbers are indices to the vertices list defined above.
        #self.colors = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
        face_transformations = [('n',0),('y',90),('x',270),('y',270),('x',90),('x',180)] #Front,up,right,down,left,back

        size = int(math.log(len(cube[0]), 2)) #What demention is used
        offset = 2/(size)/25
        cube_size = (2 - offset*(size+1))/size

        for c in range(len(cube)):
            tmp_vertices = []
            p = (-1,1+cube_size,1)
            count = 0
            for i in range(0, size):
                p = (-1, p[1]-offset-cube_size, p[2])

                for j in range(0, size):
                    start_index = len(self.vertices) + len(tmp_vertices)
                    tmp_vertices.append(Point3D(p[0],p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+cube_size,p[1],p[2]))
                    tmp_vertices.append(Point3D(p[0]+cube_size,p[1]-cube_size,p[2]))
                    tmp_vertices.append(Point3D(p[0],p[1]-cube_size,p[2]))
                    self.faces.append((start_index,start_index+1,start_index+2,start_index+3))

                    self.colors.append(color_bank[cube[c][count]])

                    p = (p[0]+cube_size+offset, p[1], p[2])
                    count += 1

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
                if face_transformations[c][0] == 'x':
                    self.vertices.append(tmp_vertices[i].rotateX(face_transformations[c][1]))
                elif face_transformations[c][0] == 'y':
                    self.vertices.append(tmp_vertices[i].rotateY(face_transformations[c][1]))
                elif face_transformations[c][0] == 'z':
                    self.vertices.append(tmp_vertices[i].rotateZ(face_transformations[c][1]))
                else:
                    self.vertices.append(tmp_vertices[i])


if __name__ == "__main__":
    #colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 165, 0)]
    #Simulation().run()

    m = Cube(2)
    c = ThreeD_Cube(None)
    c.test(m.state)