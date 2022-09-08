from operator import truediv
import pygame
import os
from utils import  scale_image, blit_rotate_center, rot_center

#WIDTH, HEIGHT = 500,500
#WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_caption("PARKING GAME")
#greenCar = scale_image(pygame.image.load(os.path.join('assets', 'GreenCar.png')),0.1)
#FPS = 120

class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y, vel):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = scale_image(pygame.image.load(os.path.join('assets', 'GreenCar.png')).convert(), 0.1)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = vel
    
    def rotate(self, left= False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.vel
        if keys[pygame.K_a]:
            self.rect.x -= self.vel
        if keys[pygame.K_w]:
            self.rect.y -= self.vel
        if keys[pygame.K_s]:
            self.rect.y += self.vel
        
#    def draw(self,win):
#        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
#        pygame.display.update()

#def draw(win, images, player_car):
#    for img, pos in images:
#        win.blit(img, pos)
#    player_car.draw(win)
#    pygame.display.update()


#run = True
#clock = pygame.time.Clock()
#player_car = PlayerCar(4, 4, greenCar, (180,200))

# while run:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             break
    
#     #keys = pygame.key.get_pressed()
#     car.move()
#     #if keys[pygame.K_d]:
#     #    car.rotate(right=True)
#     pygame.display.update()
# pygame.quit()

