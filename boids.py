import pygame
import math
import random
from pygame.locals import *

running = False
birdList = []

clock = pygame.time.Clock()
width=600
height=600
PI = math.pi

screen = pygame.display.set_mode([width, height])

pygame.init()

class Bird(object):

    angle = 0
    vel = 2
    size = 10
    birds = []
    shape = [[],[],[]]
    movement = 0
    center = [0,0]
    angularVel = .08
    turnDist = 30
    ID = 0

    def __init__(self, x, y, angle, ID):
        print("new bird!\n")
        super(Bird, self).__init__()
        self.center = [x,y]
        self.angle = angle
        self.movement = pygame.math.Vector2(self.vel*math.cos(self.angle),self.vel*math.sin(self.angle))
        self.ID = ID

    def dAndVecTo(self, bird2):
        b2center = bird2.center
        distance = math.sqrt(math.pow(self.center[0]-b2center[0],2)+math.pow(self.center[0]-b2center[0],2))
        return [distance,math.cos(distance), math.sin(distance)]

    def draw(self):
        p1 = [self.center[0]+self.size*math.cos(self.angle),          self.center[1]+self.size*math.sin(self.angle)]
        p2 = [self.center[0]+self.size*math.cos(self.angle+(2*PI/3)+.2), self.center[1]+self.size*math.sin(self.angle+(2*PI/3)+.2)]
        p3 = [self.center[0]+self.size*math.cos(self.angle-(2*PI/3)-.2), self.center[1]+self.size*math.sin(self.angle-(2*PI/3)-.2)]
        self.shape[0] = p1
        self.shape[1] = p2
        self.shape[2] = p3
        pygame.draw.polygon(screen, 1, self.shape)

    def updateAngle(self):
        for bird in self.birds:
            dAndVec = self.dAndVecTo(bird)
            if self.ID == 1:
                print(self.movement.angle_to(vector))
            if dAndVec[0]<self.turnDist:
                vector = Vector2(dAndVec[1], dAndVec[2])
                if self.movement.angle_to(vector) > 180:
                    self.angle = self.angle + self.angularVel
                if self.movement.angle_to(vector) < 180:
                    self.angle = self.angle - self.angularVel
        #bounds
        if self.center[0] > width-self.turnDist and (self.angle >= 0 and self.angle <= PI):
            self.angle = self.angle + self.angularVel
        if self.center[0] > width-self.turnDist and (self.angle > PI):
            self.angle = self.angle - self.angularVel
        if self.center[0] < self.turnDist and (self.angle <= PI):
            self.angle = self.angle - self.angularVel
        if self.center[0] < self.turnDist and (self.angle > PI):
            self.angle = self.angle + self.angularVel
        if self.center[1] > height-self.turnDist and (self.angle >= 3*PI/2 or self.angle <= PI/2):
            self.angle = self.angle - self.angularVel
        if self.center[1] > height-self.turnDist and (self.angle >= PI/2 and self.angle < 3*PI/2):
            self.angle = self.angle + self.angularVel
        if self.center[1] < self.turnDist and (self.angle <= PI/2 or self.angle > 3*PI/2):
            self.angle = self.angle + self.angularVel
        if self.center[1] < self.turnDist and (self.angle > PI/2 and self.angle <= 3*PI/2):
            self.angle = self.angle - self.angularVel
        #for bird in birds:
            #if
        if self.angle > 2*PI:
            self.angle = self.angle - 2*PI
        if self.angle < 0:
            self.angle = self.angle + 2*PI

    def update(self, birds):
        self.updateAngle()
        self.movement = pygame.math.Vector2(self.vel*math.cos(self.angle),self.vel*math.sin(self.angle))
        self.center[0] = self.center[0] + self.movement.x
        self.center[1] = self.center[1] + self.movement.y
        if self.center[0] < -50:
            self.center[0] = width + 50
        elif self.center[0] > width + 50:
            self.center[0] = -50;
        if self.center[1] > height+50:
            self.center[1] = -50
        elif self.center[1]< -50:
            self.center[1] = height + 50
        self.draw()

def run():
    running = True
    while running:
        clock.tick(60)
        pygame.draw.rect(screen, pygame.Color("#AAAAAA"), [0,0, width, height])
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                return
        for bird in birdList:
            bird.update(birdList)

        pygame.display.flip()

def start():
    for i in range(50):
        x = random.randrange(100,width-100,1)
        y = random.randrange(100,height-100,1)
        angle = random.random()*(2*PI)
        birdList.append(Bird(x,y, angle, i))
    run()

start()
