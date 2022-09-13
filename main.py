import pygame, os, button, objects, sys, carMechanics

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 100)

WIDTH, HEIGHT = 1000, 500
ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)




#getting images for game
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.jpg")), 
    (WIDTH, HEIGHT))

PARK_VERTICAL = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "park.png")), (PARK_WIDTH, PARK_HEIGHT))

ROAD = pygame.image.load(os.path.join("assets", "road.png"))
ROAD_ONE = pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT))
ROAD_TWO = pygame.transform.rotate(pygame.transform.scale(ROAD ,(ROAD_WIDTH, ROAD_HEIGHT * 3)), 90)

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

def check_car_in_parking_space(car, left, right, bottom, top):
    #print(f"car: {car.rect.left, car.rect.right, car.rect.bottom, car.rect.top}")
    if car.rect.left > left and car.rect.right < right and car.rect.bottom < bottom and car.rect.top > top:
        return True    
            

def end_screen(did_user_win):
    #creating text object
    if did_user_win == False:
        text = font.render('Game Over', True, WHITE, RED)
        back_col = RED
    else:
        text = font.render('Game Complete!', True, WHITE, GREEN)
        back_col = GREEN
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 3)

    while True:
        WIN.fill(back_col)
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

def draw_level_two():
    #Creating car object
    car = carMechanics.PlayerCar((235, 75))
    
    while True:
        clock.tick(FPS)
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(ROAD_TWO, (200 , HEIGHT - ROAD_WIDTH - ROAD_HEIGHT))
        WIN.blit(ROAD_ONE, (200 , 50))
        p = pygame.Rect(725, HEIGHT - ROAD_WIDTH - ROAD_HEIGHT - PARK_HEIGHT, PARK_WIDTH, PARK_HEIGHT)
        WIN.blit(PARK_VERTICAL, (p.x, p.y))

       
         
        #draw car
        car.move_player(WIN)

        if quit2_btn.draw(WIN):
            main_menu()

        if check_car_in_parking_space(car, 725, 800, 200, 50):
            end_screen(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def draw_level_one():
    #Creating car object
    car = carMechanics.PlayerCar((150, 400))   
    while True:
        clock.tick(FPS)
        WIN.blit(objects.BACKGROUND_ONE, (0, 0))
        WIN.blit(objects.BACKGROUND_ONE_OUTLINE, (0, 0))

        #draw car
        car.move_player(WIN)
        
         
        
        if car.collide(objects.BACKGROUND_ONE_MASK) !=None:
            end_screen(False)

        if quit2_btn.draw(WIN):
            main_menu()

        if check_car_in_parking_space(car, 778, 860, 80, 5):
            draw_level_two()

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