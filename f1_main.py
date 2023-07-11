# pylint: disable=missing-module-docstring,missing-class-docstring,import-error,missing-module-docstring,import-error
import sys
import pygame
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
    Driver(RED, startingPos, 2, 1),
    Driver(BLUE, startingPos, 1, 1),
    Driver(GREEN, startingPos, 3, 1),
    Driver((150,8,111), startingPos, 4, 1),
    Driver((100,230,200), startingPos, 5, 1),
    Driver((91,230,41), startingPos, 7, 1)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    # drawing track
    pygame.draw.lines(window, BLACK, True, track_layout, 15)

    # update and draw drivers when moving
    Movement.move(window, drivers, track_layout, startingPos)

    pygame.display.flip()
    clock.tick(60)
