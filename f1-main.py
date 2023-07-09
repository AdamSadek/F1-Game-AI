import pygame
import sys
import math

# initialize pygame
pygame.init()

# window size
HEIGHT = 1920
WIDTH = 1080

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# new track layout - Lebanon GP
track_layout = [
    (200, 210),
    (500, 210),
    (600, 110),
    (700, 110),
    (800, 210),
    (1000, 210),
    (1000, 410),
    (900, 510),
    (700, 510),
    (600, 610),
    (500, 610),
    (400, 510),
    (200, 510),
    (100, 410),
    (100, 310),
    (200, 210)
]

# create window
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("F1 GAME AI")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    # this will draw the track
    pygame.draw.lines(window, BLACK, False, track_layout, 20)



    pygame.display.flip()
    clock.tick(60)
