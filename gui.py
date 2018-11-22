'''
    Team 4 - Ben Duggan & Connor Altic
    11/3/18
    Class with main gui class
'''

# from beginnersMethod import *
from ThreeD_Cube import *

class GUI():

    def __init__(self, map, player=True, width=None, height=None, threeD=True):
        self.map = map
        self.player = player

        self.buttons = [[["F ", pygame.Rect(100, 100, 50, 50)], ["F2", pygame.Rect(100, 100, 50, 50)], ["F'", pygame.Rect(100, 100, 50, 50)]]]

        pygame.init()
        if width is None or height is None:
            self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.RESIZABLE)
        else:
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        pygame.display.set_caption('CubeAI')
        pygame.time.Clock().tick(50)

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        if threeD:
            self.threeD = ThreeD_Cube(self.screen)
        else:
            self.threeD = None

    def scramble(self, times, pause=0):
        for i in range(times):
            #self.map.scramble(1)
            self.update()
            time.sleep(pause)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                # Controls
                if keys[pygame.K_a]:
                    if self.threeD != None:
                        self.threeD.autoRotate = True
                if keys[pygame.K_m]:
                    if self.threeD != None:
                        self.threeD.autoRotate = False
                if keys[pygame.K_v]:
                    if self.threeD != None:
                        self.threeD = None
                    else:
                        self.threeD = ThreeD_Cube(self.screen)

                # Prime
                if keys[pygame.K_1]:
                    if keys[pygame.K_f]:
                        self.map.makeMove((0,3))
                        self.map.printMap()
                        print("F'")
                    if keys[pygame.K_u]:
                        self.map.makeMove((1,3))
                        print("U'")
                    if keys[pygame.K_r]:
                        self.map.makeMove((2,3))
                        print("R'")
                    if keys[pygame.K_d]:
                        self.map.makeMove((3,3))
                        print("D'")
                    if keys[pygame.K_l]:
                        self.map.makeMove((4,3))
                        print("L'")
                    if keys[pygame.K_b]:
                        self.map.makeMove((5,3))
                        print("B'")
                    if keys[pygame.K_x]:
                        self.map.makeMove((6,3))
                        print("X'")
                    if keys[pygame.K_y]:
                        self.map.makeMove((7,3))
                        print("Y'")
                    if keys[pygame.K_z]:
                        self.map.makeMove((8,3))
                        print("Z'")

                # Move twice
                elif keys[pygame.K_2]:
                    if keys[pygame.K_f]:
                        self.map.makeMove((0,2))
                        self.map.printMap()
                        print("F2")
                    if keys[pygame.K_u]:
                        self.map.makeMove((1,2))
                        print("U2")
                    if keys[pygame.K_r]:
                        self.map.makeMove((2,2))
                        print("R2")
                    if keys[pygame.K_d]:
                        self.map.makeMove((3,2))
                        print("D2")
                    if keys[pygame.K_l]:
                        self.map.makeMove((4,2))
                        print("L2")
                    if keys[pygame.K_b]:
                        self.map.makeMove((5,2))
                        print("B2")
                    if keys[pygame.K_x]:
                        self.map.makeMove((6,2))
                        print("X2")
                    if keys[pygame.K_y]:
                        self.map.makeMove((7,2))
                        print("Y2")
                    if keys[pygame.K_z]:
                        self.map.makeMove((8,2))
                        print("Z2")
                else:
                    if keys[pygame.K_f]:
                        self.map.makeMove((0,1))
                        self.map.printMap()
                        print("F")
                    if keys[pygame.K_u]:
                        self.map.makeMove((1,1))
                        print("U")
                    if keys[pygame.K_r]:
                        self.map.makeMove((2,1))
                        print("R")
                    if keys[pygame.K_d]:
                        self.map.makeMove((3,1))
                        print("D")
                    if keys[pygame.K_l]:
                        self.map.makeMove((4,1))
                        print("L")
                    if keys[pygame.K_b]:
                        self.map.makeMove((5,1))
                        print("B")
                    if keys[pygame.K_x]:
                        self.map.makeMove((6,1))
                        print("X")
                    if keys[pygame.K_y]:
                        self.map.makeMove((7,1))
                        print("Y")
                    if keys[pygame.K_z]:
                        self.map.makeMove((8,1))
                        print("Z")

            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.buttons)):
                    if self.buttons[i][1].collidepoint(event.pos):
                        print('Collission')
            '''

        if self.threeD != None:
            self.threeD.update(self.map.state, [(255, 0, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 165, 0)])
            self.threeD.draw()
        else:
            self.screen.fill((0, 0, 0))
            self.draw2DCube()
            self.drawButtons()
            pygame.display.update()

    def draw2DCube(self):
        cube = self.map.state
        #print(cube)
        # Cube size param
        offset = (200, 25)
        cubeletSize = 30
        gap = 2
        size = int(math.log(len(cube[0]), 2)) #What demention is used
        colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 165, 0)] #Color of each cube: red, yellow, blue, white, green, orange
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
                    pygame.draw.rect(self.screen, colors[cube[c][count]], [offset[0]+f[0]+j*(cubeletSize+gap), offset[1]+f[1]+i*(cubeletSize+gap), cubeletSize, cubeletSize])
                    count += 1

    def drawButtons(self):
        pass
        #for i in self.buttons:
            #pygame.draw.rect(self.screen, (255,255,255), i[1])


if __name__ == "__main__":
    print('Testing GUI')
    m = Map(3)

    g = GUI(map=m, player=True, width=800, height=600, threeD=True)

    g.update()

    time.sleep(1)

    #m.makeMove((0,2))

    #g.scramble(10, 0.3)
    m.printMap()

    while True:
        g.update()




