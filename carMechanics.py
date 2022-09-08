from operator import truediv
import pygame
import time
import math
import os
from utils import  scale_image, blit_rotate_center, rot_center


GreenCar = scale_image(pygame.image.load(os.path.join('assets', 'GreenCar.png')),0.1)

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PARKING GAME")

FPS = 60


class AbstractCar:
    
    def __init__(self, max_vel,  rotation_vel):
        self.img = self.IMG

        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
    
    def rotate(self, left= False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self,win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        pygame.display.update()
    


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
images = []
player_car = PlayerCar(4,4)





while run:
    clock.tick(FPS)

    draw(WIN, images, player_car )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)

pygame.quit()

