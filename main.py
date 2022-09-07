import pygame
import os

WIDTH, HEIGHT = 1000, 500
ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150
BLACK = (0, 0, 0)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.jpg")), 
    (WIDTH, HEIGHT))


ROAD = pygame.image.load(os.path.join("assets", "road.png"))
PARK = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "park.png")), (PARK_WIDTH, PARK_HEIGHT)), 90)
ROAD_ONE = pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT))
ROAD_TWO = pygame.transform.rotate(pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT * 3)), 90)

BOUNDARY_ONE = pygame.Rect(199, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT, 1, 300)
BOUNDARY_TWO = pygame.Rect(299, HEIGHT - ROAD_HEIGHT, 1, 200)
BOUNDARY_THREE = pygame.Rect(199, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH, ROAD_HEIGHT * 3 - PARK_WIDTH * 2, 1)
BOUNDARY_FOUR = pygame.Rect(299, HEIGHT - ROAD_HEIGHT, ROAD_HEIGHT * 3 - ROAD_WIDTH, 1)
BOUNDARY_FIVE = pygame.Rect(799, 125, 1, ROAD_WIDTH + PARK_WIDTH)
BOUNDARY_SIX = pygame.Rect(650, 125, PARK_HEIGHT, 1)
BOUNDARY_SEVEN = pygame.Rect(650, 125, 1, PARK_WIDTH)

boundaries = [BOUNDARY_ONE, BOUNDARY_TWO, BOUNDARY_THREE, BOUNDARY_FOUR, BOUNDARY_FIVE, BOUNDARY_SIX, BOUNDARY_SEVEN]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(ROAD_ONE, (200 , HEIGHT - ROAD_HEIGHT))
    WIN.blit(ROAD_TWO, (200 , HEIGHT - ROAD_WIDTH - ROAD_HEIGHT))
    WIN.blit(PARK, (650, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_WIDTH))
    for bound in boundaries:
        pygame.draw.rect(WIN, BLACK, bound)
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()    
    pygame.quit()

if __name__ == "__main__":
    main()