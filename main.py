import pygame, os, button, objects, sys, carMechanics
pygame.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150

#getting images for game
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.jpg")), 
    (WIDTH, HEIGHT))
ROAD = pygame.image.load(os.path.join("assets", "road.png"))
PARK = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "park.png")), (PARK_WIDTH, PARK_HEIGHT)), 90)
ROAD_ONE = pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT))
ROAD_TWO = pygame.transform.rotate(pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT * 3)), 90)

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 100)

#Buttons==========================================================
#Getting button images
START_IMG = pygame.image.load("assets\start.png").convert_alpha()
QUIT_IMG = pygame.image.load("assets\quit.png").convert_alpha()
QUIT2_IMG = pygame.image.load("assets\quit2.png").convert_alpha()
RESET_IMG = pygame.image.load("assets/reset.png").convert_alpha()
#Creating button objects
start_btn = button.Button(375, 100, START_IMG, 1)
quit_btn = button.Button(375, 250, QUIT_IMG, 1)
quit_btn_lose_screen = button.Button(250, 300, QUIT_IMG, 1)
quit2_btn = button.Button(0, 0, QUIT2_IMG, 0.05)
reset_btn = button.Button(550, 300, RESET_IMG, 1)

def check_car_in_parking_space(car, p):
    #print(f"car: {car.rect.left, car.rect.right, car.rect.bottom, car.rect.top} \n park: {p.left, p.right, p.bottom, p.top}")
    if car.rect.top < p.right and car.rect.left > p.top and car.rect.bottom > p.left and car.rect.right < p.bottom:
        return True    
            

def end_screen(did_user_win):
    if did_user_win == False:
        text = font.render('Game Over', True, WHITE, RED)
    else:
        text = font.render('Game Complete!', True, WHITE, GREEN)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 3)
    while True:
        if did_user_win == False:
            WIN.fill(RED)
        else:
            WIN.fill(GREEN)
        WIN.blit(text, textRect)

        if reset_btn.draw(WIN):
            draw_level_one()
        if quit_btn_lose_screen.draw(WIN):
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def draw_level_one():
    #Creating car object
    car = carMechanics.PlayerCar(250, 400, 1)   
    player_list = pygame.sprite.Group()
    player_list.add(car)
    while True:
        clock.tick(FPS)
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(ROAD_ONE, (200 , HEIGHT - ROAD_HEIGHT))
        WIN.blit(ROAD_TWO, (200 , HEIGHT - ROAD_WIDTH - ROAD_HEIGHT))
        #WIN.blit(PARK, (650, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_WIDTH))
        p = pygame.Rect(650, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_WIDTH, PARK_WIDTH, PARK_HEIGHT)
        WIN.blit(PARK, (p.x, p.y))
        player_list.draw(WIN)
        car.move()
        
        for bound in objects.lvl1_boundaries:
            pygame.draw.rect(WIN, BLACK, bound)
            if(bound.colliderect(car)):
                end_screen(False)
            
        if quit2_btn.draw(WIN):
            main_menu()
        if check_car_in_parking_space(car, p):
            end_screen(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main_menu():
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

if __name__ == "__main__":
    main_menu()