import pygame
import sys
import math
from drivers import Driver
from movement import Movement

# initialize pygame
pygame.init()

# window size
HEIGHT = 1920
WIDTH  = 1080

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (30, 144, 255)
GREEN = (34, 139, 34)


# new track layout - Lebanon GP
track_layout = [
    (200, 200),
    (500, 200),
    (600, 100),
    (700, 100),
    (800, 200),
    (1000, 200),
    (1000, 400),
    (900, 500),
    (700, 500),
    (600, 600),
    (500, 600),
    (400, 500),
    (200, 500),
    (100, 400),
    (100, 300),
    (200, 200)
]

# create window
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("F1 GAME AI")

clock = pygame.time.Clock()
startingPos = [200,200]

# creating drivers drivers
drivers = [
    Driver(RED, startingPos, 0.001),
    Driver(BLUE, startingPos, 0.001),
    Driver(GREEN, startingPos, 0.001)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)


    # draw the track outline
    pygame.draw.lines(window, BLACK, True, track_layout, 15)

    # update and draw drivers when moving
    # driver1.draw(window)
    # driver2.draw(window) 
    Movement.move(window, driver1, track_layout, startingPos)
    # Movement.move(window, driver2, track_layout, startingPos)


    pygame.display.flip()
    clock.tick(60)
