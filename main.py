import pygame, os, button
WIDTH, HEIGHT = 1000, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150
BLACK = (0, 0, 0)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.jpg")), 
    (WIDTH, HEIGHT))
START_IMG = pygame.image.load("assets\start.png").convert_alpha()
QUIT_IMG = pygame.image.load("assets\quit.png").convert_alpha()

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

start_btn = button.Button(350, 100, START_IMG, 1)
quit_btn = button.Button(350, 250, QUIT_IMG, 1)

def draw_level_one():
    run = True
    while run:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(ROAD_ONE, (200 , HEIGHT - ROAD_HEIGHT))
        WIN.blit(ROAD_TWO, (200 , HEIGHT - ROAD_WIDTH - ROAD_HEIGHT))
        WIN.blit(PARK, (650, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_WIDTH))
        for bound in boundaries:
            pygame.draw.rect(WIN, BLACK, bound)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    pygame.quit()

def main_menu():
    run = True
    while run:
        WIN.fill((255, 255, 0))

        if start_btn.draw(WIN):
            draw_level_one()
        if quit_btn.draw(WIN):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit()

        #draw_level_one()    
if __name__ == "__main__":
    main_menu()