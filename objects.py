import pygame, os
WIDTH, HEIGHT = 1000, 500
ROAD_WIDTH, ROAD_HEIGHT = 100, 200
PARK_WIDTH, PARK_HEIGHT = 75, 150

#Level one boundaries
BACKGROUND_ONE_OUTLINE =  pygame.transform.scale(pygame.image.load(os.path.join("Assets", 'OutlineLevel1.png')), (WIDTH, HEIGHT))
BACKGROUND_ONE_MASK = pygame.mask.from_surface(BACKGROUND_ONE_OUTLINE)


BOUNDARY_ONE = pygame.Rect(110, 0, 1, 500)
BOUNDARY_TWO = pygame.Rect(250, 0, 1, 90)
BOUNDARY_THREE = pygame.Rect(250, 202, 1, 300)
BOUNDARY_FOUR = pygame.Rect(250, 202, 800, 1)
BOUNDARY_FIVE = pygame.Rect(250, 90, 525, 1)
BOUNDARY_SIX = pygame.Rect(775, 0, 1, 90)
BOUNDARY_SEVEN = pygame.Rect(865, 0, 1, 90)
BOUNDARY_EIGHT = pygame.Rect(865, 90, 100, 1)

lvl1_boundaries = [BOUNDARY_ONE, BOUNDARY_TWO, BOUNDARY_THREE, BOUNDARY_FOUR, BOUNDARY_FIVE, BOUNDARY_SIX, BOUNDARY_SEVEN, BOUNDARY_EIGHT]

#Level 2 boundaries
BOUNDARY_ONE_TWO = pygame.Rect(200, HEIGHT - ROAD_HEIGHT, ROAD_HEIGHT * 3, 1)
BOUNDARY_TWO_TWO = pygame.Rect(200, HEIGHT - ROAD_HEIGHT * 2 - 50, 1, ROAD_HEIGHT + 50)
BOUNDARY_THREE_TWO = pygame.Rect(300, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH, ROAD_HEIGHT * 2 + 25, 1)
BOUNDARY_FOUR_TWO = pygame.Rect(200, HEIGHT - ROAD_HEIGHT * 2 - 50, ROAD_WIDTH, 1)
BOUNDARY_FIVE_TWO = pygame.Rect(725, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH - PARK_HEIGHT , 1, PARK_HEIGHT)
BOUNDARY_SIX_TWO = pygame.Rect(725, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH - PARK_HEIGHT , PARK_WIDTH, 1)
BOUNDARY_SEVEN_TWO = pygame.Rect(800, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH - PARK_HEIGHT , 1, PARK_HEIGHT + ROAD_WIDTH)
BOUNDARY_EIGHT_TWO = pygame.Rect(300, HEIGHT - ROAD_HEIGHT - ROAD_WIDTH * 2 - 50, 1, PARK_HEIGHT)

lvl2_boundaries = [BOUNDARY_ONE_TWO, BOUNDARY_TWO_TWO, BOUNDARY_THREE_TWO, BOUNDARY_FOUR_TWO, BOUNDARY_FIVE_TWO, 
BOUNDARY_SIX_TWO, BOUNDARY_SEVEN_TWO, BOUNDARY_EIGHT_TWO]