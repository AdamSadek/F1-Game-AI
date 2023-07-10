import pygame
import sys
import math
from drivers import Driver

# initialize pygame
pygame.init()

# window size
HEIGHT = 1920
WIDTH = 1080

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (30, 144, 255)

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

# Create drivers
driver1 = Driver(RED, track_layout[0], speed=2)
driver2 = Driver(BLUE, track_layout[1], speed=3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)


    # draw the track outline
    pygame.draw.lines(window, BLACK, True, track_layout, 15)

    # Update and draw drivers
    # driver1.update()
    driver1.draw(window)
    # driver2.update()
    driver2.draw(window)

    pygame.display.flip()
    clock.tick(60)
