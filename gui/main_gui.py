'''
    Team 4 - Ben Duggan & Connor Altic
    11/24/18
    Class with main gui class
'''

import pygame
from gui.ThreeD_Cube import *
from Cube import *

class GUI():

    def __init__(self, cube, player=True, width=None, height=None, threeD=True):
        self.cube = cube
        self.player = player
        self.state_list = None
        self.move_history = []
        self.info_box_text = [[('State list: ', (0,0,0))], [('Move history: ',(0,0,0))], [('Key: ',(0,0,0))]]

        self.buttons = [[["F ", pygame.Rect(100, 100, 50, 50)], ["F2", pygame.Rect(100, 100, 50, 50)], ["F'", pygame.Rect(100, 100, 50, 50)]]]

        pygame.init()
        if width is None or height is None:
            self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.RESIZABLE)
        else:
            self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        pygame.display.set_caption('CubeAI')
        pygame.time.Clock().tick(50)

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 15)

        if threeD:
            self.threeD = ThreeD_Cube(self.screen)
        else:
            self.threeD = None

    def scramble(self, times, pause=0):
        for i in range(times):
            self.cube.scramble(1)
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

                # Arrow keys
                if keys[pygame.K_RIGHT]:
                    if self.state_list != None and self.state_num < len(self.state_list)-1:
                        self.state_num += 1
                        self.makeMove(self.state_list[self.state_num][0])
                if keys[pygame.K_LEFT]:
                    if self.state_list != None and self.state_num > 0:
                        self.state_num -= 1
                        self.makeMove(self.state_list[self.state_num][0])

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

        if self.threeD != None:
            self.threeD.update(self.cube.state, [(255, 0, 0), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (255, 165, 0)])
            self.threeD.draw()
            self.renderText()
            pygame.display.update()
        else:
            self.screen.fill((0, 0, 0))
            self.draw2DCube()
            self.renderText()
            pygame.display.update()

    def draw2DCube(self):
        cube = self.cube.state
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


    def makeMove(self, move):
        self.move_history.append(move)
        if self.state_list != None and move == self.state_list[self.state_num]:
            print('move num')

        self.cube.makeMove(move)
        print('Made move: ' + str(move))

        # Add to move history
        if len(self.info_box_text[1]) >= 3:
            # There is at least 2 moves present
            if len(self.info_box_text[1][1][0]) == 0:
                self.info_box_text[1][1] = (self.info_box_text[1][2][0] + ', ', (0,0,0))
            else:
                self.info_box_text[1][1] = (self.info_box_text[1][1][0] + self.info_box_text[1][2][0] + ', ', (0,0,0))
            self.info_box_text[1][2] = (str(move), (0,0,255))
        else:
            # This is the first move
            self.info_box_text[1].append(('', (0,0,0)))
            self.info_box_text[1].append((str(move), (0,0,255)))

    def moveList(self, states):
        self.cube.state = self.cube.decode(states[0][1])
        self.state_list = states
        self.state_num = 0
        self.info_box_text[0].append((str(states), (0,0,0)))


if __name__ == "__main__":
    print('Testing GUI')
    m = Cube(2)

    g = GUI(cube=m, width=800, height=600, threeD=False)
    g.moveList([((1,1),4314954162759849540), ((1,3),4314954162759849540)])

    g.update()

    time.sleep(1)

    #m.makeMove((0,2))

    #g.scramble(10, 0.3)
    m.printMap()

    while True:
        g.update()




