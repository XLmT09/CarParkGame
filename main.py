import pygame, os, button, objects, sys, carMechanics
pygame.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150
BLACK = (0, 0, 0)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.jpg")), 
    (WIDTH, HEIGHT))
START_IMG = pygame.image.load("assets\start.png").convert_alpha()
QUIT_IMG = pygame.image.load("assets\quit.png").convert_alpha()
QUIT2_IMG = pygame.image.load("assets\quit2.png").convert_alpha()
ROAD = pygame.image.load(os.path.join("assets", "road.png"))
PARK = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "park.png")), (PARK_WIDTH, PARK_HEIGHT)), 90)
ROAD_ONE = pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT))
ROAD_TWO = pygame.transform.rotate(pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT * 3)), 90)

clock = pygame.time.Clock()

start_btn = button.Button(375, 100, START_IMG, 1)
quit_btn = button.Button(375, 250, QUIT_IMG, 1)
quit2_btn = button.Button(0, 0, QUIT2_IMG, 0.05)

car = carMechanics.PlayerCar(40, 40, 1)   
player_list = pygame.sprite.Group()
player_list.add(car)

def draw_level_one():
    run = True
    clock.tick(FPS)
    while run:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(ROAD_ONE, (200 , HEIGHT - ROAD_HEIGHT))
        WIN.blit(ROAD_TWO, (200 , HEIGHT - ROAD_WIDTH - ROAD_HEIGHT))
        WIN.blit(PARK, (650, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_WIDTH))
        
        for bound in objects.lvl1_boundaries:
            pygame.draw.rect(WIN, BLACK, bound)

        player_list.draw(WIN)
        car.move()
        if quit2_btn.draw(WIN):
            main_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit()
    sys.exit()

def main_menu():
    clock.tick(FPS)
    run = True
    while run:
        WIN.fill((153, 204, 255))

        if start_btn.draw(WIN):
            draw_level_one()
        if quit_btn.draw(WIN):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit()
    sys.exit()

        #draw_level_one()    
if __name__ == "__main__":
    main_menu()