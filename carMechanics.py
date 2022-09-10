

from operator import truediv
from tkinter import HORIZONTAL, VERTICAL
import pygame
import time
import math
import os
from utils import  scale_image, blit_rotate_center, rot_center



GreenCar = scale_image(pygame.image.load(os.path.join('assets', 'GreenCar.png')),0.1)

GRASS = scale_image(pygame.image.load(os.path.join('assets', 'grass.jpg')),2.5)


WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
color = (255,0, 0)


pygame.display.set_caption("PARKING GAME")

FPS = 60
images = [(GRASS, (0,0))]

class AbstractCar:
    
    def __init__(self, max_vel,  rotation_vel):
        self.img = self.IMG

        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1 
    
    def rotate(self, left= False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self,win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        pygame.display.update()
    def move_forward(self):
        self.vel  = min(self.vel + self.acceleration, self.max_vel)
        self.move()
    def move_backward(self):
        self.vel  = min(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians)* self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal
    def reduce_speed(self):
        self.vel = max(self.vel -self.acceleration ,0)
        self.move()


class PlayerCar(AbstractCar):
    IMG = GreenCar
    START_POS = (180,200)

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    pygame.display.update() 


run = True
clock = pygame.time.Clock()

player_car = PlayerCar(4,4)


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_a]:
            player_car.rotate(left=True)
        if keys[pygame.K_d]:
            player_car.rotate(right=True)
        
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved :
        player_car.reduce_speed()

    if keys[pygame.K_s]:
        player_car.move_backward()



while run:
    clock.tick(FPS)

    draw(WIN, images, player_car )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break    
    move_player(player_car)
    
    

pygame.quit()

